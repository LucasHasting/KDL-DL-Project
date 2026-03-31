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

from functions import GetReward
import gym
from gym.spaces import Box
import numpy as np
import torch
from torchvision import transforms as T

class SkipFrame(gym.Wrapper):
    def __init__(self, env, skip):
        """Return only every `skip`-th frame"""
        super().__init__(env)
        self._skip = skip

    def step(self, action):
        """
            Simultanious action implemention
        """
        #get info for env step XXX
        state, reward, done, info_old = self.env.step(ACTION_SPACE_MAP[1])

        #make action for 0.5 seconds XXX
        for i in range(32):
                observation, reward, done, info_new = self.env.step(action=action)

        #reward 
        reward = GetReward(info_old, info_new)

        return observation, reward, done, info_new

class GrayScaleObservation(gym.ObservationWrapper):
    def __init__(self, env):
        super().__init__(env)
        obs_shape = self.observation_space.shape[:2]
        self.observation_space = Box(low=0, high=255, shape=obs_shape, dtype=np.uint8)

    def permute_orientation(self, observation):
        # permute [H, W, C] array to [C, H, W] tensor
        observation = np.transpose(observation, (2, 0, 1))
        observation = torch.tensor(observation.copy(), dtype=torch.float)
        return observation

    def observation(self, observation):
        observation = self.permute_orientation(observation)
        transform = T.Grayscale()
        observation = transform(observation)
        return observation


class ResizeObservation(gym.ObservationWrapper):
    def __init__(self, env, shape):
        super().__init__(env)
        if isinstance(shape, int):
            self.shape = (shape, shape)
        else:
            self.shape = tuple(shape)

        obs_shape = self.shape + self.observation_space.shape[2:]
        self.observation_space = Box(low=0, high=255, shape=obs_shape, dtype=np.uint8)

    def observation(self, observation):
        transforms = T.Compose(
            [T.Resize(self.shape, antialias=True), T.Normalize(0, 255)]
        )
        observation = transforms(observation).squeeze(0)
        return observation

class ResetCompatWrapper(gym.Wrapper):
    def reset(self, **kwargs):
        kwargs.pop("seed", None)
        kwargs.pop("options", None)

        result = self.env.reset(**kwargs)

        # New Gym API returns (obs, info)
        if isinstance(result, tuple):
            obs, info = result
            return obs   # return only observation

        return result
