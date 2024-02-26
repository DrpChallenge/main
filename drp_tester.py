import gym
import policy

def env_run(policy,agent_num,map_name,reward_list):
    env = gym.make(
            "drp_env:drp-" + str(agent_num) + "agent_" + map_name + "-v2",
            state_repre_flag="onehot_fov", 
            reward_list = reward_list
        )
    n_obs = env.reset()
    goal_checker = False
    while not goal_checker:
        env.render() #optional
        actions = policy(n_obs, env) #policy:input n_obs,env return each agent's action
        n_obs, reward, done, info = env.step(actions)
        print(n_obs)
        print("actions", actions, "reward", reward, "done",done)
        print("info", info)
        goal_checker = all(done)

if __name__ == "__main__":
    reward_list = {"goal": 100, "collision": -10, "wait": -10, "move": -1}
    env_run(policy.policy,2,"map_3x3",reward_list)