"""
This is an example of using DQN from pfrl (a deep reinforcement 
learning library using PyTorch) to development.
you should install pfrl firstly.
$ pip install pfrl
"""
import pfrl
import torch
import torch.nn
import gym
import numpy as np
import matplotlib.pyplot as plt


drone_num = 3
map_name = "map_aoba01"
reward_list = {
    "goal": 100,
    "collision": -10,
    "wait": -10,
    "move": -1,
}

env = gym.make(
    "drp_env:drp-" + str(drone_num) + "agent_" + map_name + "-v2",
    state_repre_flag="onehot_fov",
    reward_list=reward_list,
)

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

# The OBS space in the Aoba map consists of 18 BoxSpaces, each with [0,100]×[0,100]

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
agent_array = [pfrl.agents.DQN(
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
) for age in range(env.n_agents)]

episodes = 10
reward_array,average_rewards=[],[]
for i in range(1, episodes + 1):
    obs = env.reset()
    reward = 0  # return (sum of rewards)
    t = 0  # time step
    done = False
    while not done:
        #env.render()  # Uncomment to watch the behavior in a GUI window
        actions = []
        for age in range(env.n_agents):
            action = agent_array[age].act(obs[age])
            actions.append(action)
        obs, r, done, info= env.step(actions) 
        print(f"obs:{obs},actions:{actions},r:{r},done:{done},info:{info}")              
        done = all(done)
        reward += sum(r)
        t += 1
         
        for age in range(env.n_agents):
            agent_array[age].observe(obs[age],r[age],done,False)

    reward_array.append(reward)
    batch_size=10
    if i % batch_size == 0:
        #print('Episode:', i, 'Total Reward:', reward)
        average_reward = np.mean(reward_array[-batch_size:])
        average_rewards.append(average_reward)
        
print('Finished.')

##Show reward figure 
# plt.plot(reward_array)
# x = np.arange(batch_size, episodes + 1, batch_size)
# plt.plot(x, average_rewards, marker='o')
# plt.show()

#save model
for i in range(drone_num):
    agent_array[i].save(f"./models/sample_model{i}")