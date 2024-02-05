import gym
import random

env=gym.make("drp_env:drp-2agent_map_3x3-v2", state_repre_flag = "onehot_fov")

n_obs=env.reset()
print("n_obs", n_obs, type(n_obs),)
print("action_space", env.action_space)
print("observation_space", env.observation_space)

for _ in range(50):
    env.render()

    actions = []
    for agi in range(env.agent_num):
        _, avail_actions = env.get_avail_agent_actions(agi,env.n_actions)
        actions.append(random.choice(avail_actions))

    n_obs, reward, done, info = env.step(actions)

    print("actions", actions, "reward", reward, done)
    print("info", info)
    print("n_obs", n_obs)

    input("Press ENTER to continue")

