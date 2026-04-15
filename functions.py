#Name:          Lucas Hasting
#Class:         MA 395
#Date:          4/14/2026
#Instructor:    Dr. Mark Terwilliger
#Description:   Course Project - functions for normalization, reward, simultanious action (new_step)
#               https://raw.githubusercontent.com/lixado/PyBoy-RL/main/README/report.pdf
#               https://en.wikipedia.org/wiki/Feature_scaling

#min-max norm
def min_max_normalization(x, old_min, old_max, new_min, new_max):
    return ((x - old_min) / (old_max - old_min) * (new_max - new_min) + new_min)

#reward function
def GetReward(previousGameState, currentGameState):
        if currentGameState["boss_health"] == 0 and previousGameState["boss_health"] > 0:
            return 10000

        if currentGameState["boss_health"] < previousGameState["boss_health"]:
            return 1000

        if currentGameState["kirby_health"] < previousGameState["kirby_health"] and currentGameState["kirby_health"] == 1:
            return -100

        if currentGameState["kirby_health"] == 0 and previousGameState["kirby_health"] != 0:
            return -1000

        if currentGameState["kirby_health"] > 0 and currentGameState["game_state"] == 6 and previousGameState["game_state"] != 6:  # if reached warpstar
            return 1000

        if currentGameState["boss_health"] == 0 and previousGameState["boss_health"] == 0 and currentGameState["game_state"] != 6:  # if boss is dead or not active, punish for not moving right
            if currentGameState["kirby_x_scrol"] < previousGameState["kirby_x_scrol"]:  # moving left
                return -1

            if currentGameState["kirby_x_scrol"] == 68:  # moving most left
                return -5

            #if currentGameState["level_progress"] != previousGameState["level_progress"] and current_kirby["kirby_x_scroll"] == 68:  # moving most left
            #    return -5

            if currentGameState["kirby_x"] == previousGameState["kirby_x"] and currentGameState["kirby_y"] == previousGameState["kirby_y"] and currentGameState["kirby_x_scrol"] != 68 and currentGameState["kirby_x_scrol"] != 76:  # standing still
                return -1

            #if currentGameState["level_progress"] == previousGameState["level_progress"]:  # standing still
            #    return -1

            if currentGameState["kirby_x_scrol"] == 76:  # moving most right
                return 5
            return 1  # moving right
        else:
            if currentGameState["score"] > previousGameState["score"]:
                return 100
        return 0

#simultanious action implemention
def new_step(self, env, action):
        #get info for env step
        state, reward, done, trunc, info_old = env.step(action=0)

        #make action for 0.5 seconds
        for i in range(32):
                observation, reward, done, trunc, info_new = env.step(action=action)

        #reward 
        reward = GetReward(info_old, info_new)

        return observation, reward, done, info_new
