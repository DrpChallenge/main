import numpy as np
import gym

from drp_env.state_repre.wrapper.hrs_hot_file import hrs_hot_func

class HeuOnehot:
    def __init__(self, env) -> None:
        self.env = env

    def get_obs_box(self):
        n_nodes = len(self.env.G.nodes)
        obs_box=gym.spaces.Box(np.zeros(n_nodes), np.array([100]*n_nodes))
        return obs_box

    def calc_obs(self):
        return hrs_hot_func(self.env, self.env.obs)