import numpy as np
import gym

from drp_env.state_repre.wrapper.fov_wrapper import neighbor_filter_obs

class OnehotFov:
    def __init__(self, env) -> None:
        self.env = env

    def get_obs_box(self):
        n_nodes = len(self.env.G.nodes)
        obs_box=gym.spaces.Box(np.zeros(n_nodes*2), np.array([100]*(n_nodes*2)))
        return obs_box

    def calc_obs(self):
        return neighbor_filter_obs(self.env, "onehot_fov")