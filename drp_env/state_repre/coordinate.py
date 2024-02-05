import numpy as np
import gym

class Coordinate:
    def __init__(self, env) -> None:
        self.env = env

    def get_obs_box(self):
        n_nodes = len(self.env.G.nodes)
        obs_box=gym.spaces.Box(np.zeros(4), np.array([100,100,n_nodes,n_nodes]))
        return obs_box

    def calc_obs(self):
        return self.env.obs