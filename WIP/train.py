#to add to data -> kirby health as health, level_progress as level_progress, score as score

#import libraries

#import files
import 

ACTION_SPACE = []

env = retro.make('KirbysDreamLand-GB',STATE_FILE)
env.reset()
env = wrappers.SkipFrame(env, skip=4)
env = wrappers.GrayScaleObservation(env)
env = wrappers.ResizeObservation(env, shape=84)
if gym.__version__ < '0.26':
    env = wrappers.FrameStack(env, num_stack=4, new_step_api=True)
else:
    env = wrappers.FrameStack(env, num_stack=4)

use_cuda = torch.cuda.is_available()
print(f"Using CUDA: {use_cuda}")
print()

save_dir = Path("checkpoints") / datetime.datetime.now().strftime("%Y-%m-%dT%H-%M-%S")
save_dir.mkdir(parents=True)

KB1 = KirbyBoss1(state_dim=(4, 84, 84), ACTION_SPACE, save_dir=save_dir)

log = logger.MetricLogger(save_dir)

episodes = 100
for e in range(episodes):
    state = env.reset()

    # Play the game!
    while True:

        # Run agent on the state
        action = KB1.act(state)

        # Agent performs action
        next_state, reward, done, trunc, info = env.step(action)

        # Remember
        KB1.cache(state, next_state, action, reward, done)

        # Learn
        q, loss = mario.learn()

        # Logging
        log.log_step(reward, loss, q)

        # Update state
        state = next_state

        # Check if end of game
	#if boss1 defeated or dead
        if done or info["flag_get"]:
            break

    log.log_episode()

    if (e % 20 == 0) or (e == episodes - 1):
        log.record(episode=e, epsilon=KB1.exploration_rate, step=KB1.curr_step)
