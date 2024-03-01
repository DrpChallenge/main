import gym
import policy.policy as policy

def policy_test(policy, agent_num, map_name, reward_list, start, goal, render):
    """This function tests policy function.  

    Args:
        policy : policy function
        agent_num(int): set agent number(min 2 max 30)
        map_name (str): set map_name ("map_3x3","map_aoba01","map_osaka"is available)
        reward_list (dict): set reward list
        start (list): set start node
        goal (list): set  goal node
        render (bool): whether visualize environment state

    """
    assert agent_num == len(start) and agent_num == len(goal),"The number of elements in start and goal list does not match with agent_num."
    assert not any(element in start for element in goal),"The elements of goal and start must not match."
    env = gym.make(
        "drp_env:drp-" + str(agent_num) + "agent_" + map_name + "-v2",
        state_repre_flag="onehot_fov",
        reward_list=reward_list,
        goal_array=goal,
        start_ori_array=start,
    )
    obs = env.reset()
    print("obs",obs,type(obs),)
    print("action_space", env.action_space)
    print("observation_space", env.observation_space)
    done_all = False
    while not done_all:
        if render == True:
            env.render()  # optional
        actions = policy(obs, env)  # policy:input n_obs,env return each agent's action
        obs, reward, done, info = env.step(actions)
        print("obs", obs)
        print("actions", actions, "reward", reward, "done", done)
        print("info", info)
        done_all = all(done)
        env.get_obs()
    
if __name__ == "__main__":
    agent_num = 3
    map_name = "map_shibuya"
    reward_list = {"goal": 100, "collision": -10, "wait": -10, "move": -1}
    goal = [3, 6,1]
    start = [0, 2,4]
    render = True
    policy_test(
        policy=policy.policy,
        agent_num=agent_num,
        map_name=map_name,
        reward_list=reward_list,
        goal=goal,
        start=start,
        render=render,
    )