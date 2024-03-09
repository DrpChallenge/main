import pfrl
import torch
import torch.nn
import gym
import numpy as np
import matplotlib.pyplot as plt
from problem import problems
import random

class QFunction(torch.nn.Module):

    def __init__(self, obs_size, n_actions):
        super().__init__()
        hidden_layer_n = 100
        self.l1 = torch.nn.Linear(obs_size, hidden_layer_n)
        self.l2 = torch.nn.Linear(hidden_layer_n, hidden_layer_n)
        self.l3 = torch.nn.Linear(hidden_layer_n, n_actions)

    def forward(self, x):
        h = x
        h = torch.nn.functional.relu(self.l1(h))
        h = torch.nn.functional.relu(self.l2(h))
        h = self.l3(h)
        return pfrl.action_value.DiscreteActionValue(h)

def policy(obs, env): 
    obs_size = env.observation_space[0].shape[0] # map_aoba01 has 18 nodes, current-position(18dimensions)+current-goal(18dimensions)=36
    n_actions = env.action_space[0].n # map_aoba01 has 18 nodes and each node corresponds to one action
    q_func = QFunction(obs_size, n_actions)
    print(f"obs_size:{env.observation_space[0].shape[0]}")
    print(f"n_actions:{env.action_space[0].n}")
    optimizer = torch.optim.Adam(q_func.parameters(), eps=1e-2)
    # Set the discount factor that discounts future rewards.
    gamma = 0.9
    explorer = pfrl.explorers.ConstantEpsilonGreedy(
        epsilon=0.1, random_action_func=env.action_space[0].sample)
    # DQN uses Experience Replay.
    replay_buffer = pfrl.replay_buffers.ReplayBuffer(capacity=10 ** 6)
    phi = lambda x: np.array(x, dtype=np.float32)
    # Set the device id to use GPU. To use CPU only, set it to -1.
    gpu = -1
    # Now create an agent for each drone to make a distribute controll.

    agent = pfrl.agents.DQN(
        q_func,
        optimizer,
        replay_buffer,
        gamma=0.9,
        explorer=explorer,
        replay_start_size=500,
        update_interval=1,
        target_update_interval=100,
        phi=phi,
        gpu=-1,
    )
    agent_array = [agent for age in range(env.n_agents)]
    actions = []
    for age in range(env.n_agents):
        if age < 3:
            agent.load(f"./models/sample_model{age}")
            action = agent.act(obs[age])
            actions.append(action)
    return actions
