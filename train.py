#to add to data -> kirby health as health, level_progress as level_progress, score as score

#import libraries
import retro
import time
import keyboard
import pandas as pd
import requests
import torch
#import gym
from pathlib import Path
import random, datetime, os
from gym.wrappers import FrameStack

#import files
from functions import GetReward, new_step, min_max_normalization
from kirbyBoss1 import kirbyBoss1 
from kirbyNet import KirbyNet 
from logger import MetricLogger
from wrappers import SkipFrame, GrayScaleObservation, ResizeObservation, ResetCompatWrapper

ACTION_SPACE_N = 15

ACTION_SPACE_MAP = {1: [0,0,0,0,0,0,0,0,0],
                2: [0,0,0,0,0,0,0,0,1],
                3: [1,0,0,0,0,0,0,0,0],
                4: [0,0,0,0,1,0,0,0,0],
                5: [0,0,0,0,0,1,0,0,0],
                6: [0,0,0,0,0,0,1,0,0],
                7: [0,0,0,0,0,0,0,1,0],
                8: [0,0,0,0,0,1,1,0,0],
                9: [0,0,0,0,1,0,1,0,0],
                10: [0,0,0,0,1,0,0,1,0],
                11: [0,0,0,0,0,1,0,1,0],
                12: [0,0,0,0,0,0,1,0,1],
                13: [0,0,0,0,0,0,0,1,1],
                14: [1,0,0,0,0,0,1,0,0],
                15: [1,0,0,0,0,0,0,1,0]}

FPS = 60

def new_render(env):
    time.sleep(1/FPS)
    env.render()

STATE_FILE = "begginning.state"
env = retro.make('KirbysDreamLand-GB',STATE_FILE)
env.reset()
env = ResetCompatWrapper(env)   # ← wrap base env FIRST
env = SkipFrame(env, skip=4)
env = GrayScaleObservation(env)
env = ResizeObservation(env, shape=84)
env = FrameStack(env, num_stack=4)
#--------------------------------------------------------------passed

use_cuda = torch.cuda.is_available()
print(f"Using CUDA: {use_cuda}")
print()

save_dir = Path("checkpoints") / datetime.datetime.now().strftime("%Y-%m-%dT%H-%M-%S")
save_dir.mkdir(parents=True)

KB1 = kirbyBoss1(state_dim=(4, 84, 84), action_dim=ACTION_SPACE_N, save_dir=save_dir)

log = MetricLogger(save_dir)

episodes = 2
for e in range(episodes):
    print(e)
    state = env.reset()

    # Play the game!
    while True:

        # Run agent on the state
        action = KB1.act(state)+1

        # Agent performs action
        next_state, reward, done, info = env.step(ACTION_SPACE_MAP[action])
        print(ACTION_SPACE_MAP[action], reward)

        # Remember
        #KB1.cache(state, next_state, action, reward, done)

        # Learn
        q, loss = KB1.learn()

        # Logging
        log.log_step(reward, loss, q)

        # Update state
        state = next_state

        # Check if end of game
	#if boss1 defeated or dead
        if keyboard.is_pressed('q'):
            break

        new_render(env)

    log.log_episode()

    if (e % 20 == 0) or (e == episodes - 1):
        log.record(episode=e, epsilon=KB1.exploration_rate, step=KB1.curr_step)
