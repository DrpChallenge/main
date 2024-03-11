import gym
from policy.policy import policy
# from example.policy_prfl import policy

def policy_evaluation(policy, drone_num, map_name, reward_list, start, goal, render):
    if not start or goal:
        assert drone_num == len(start) and drone_num == len(
            goal
        ), "The number of elements in start and goal list does not match with drone_num."
        assert not any(
            element in start for element in goal
        ), "The elements of goal and start must not match."
    print("drp_env:drp-" + str(drone_num) + "agent_" + map_name + "-v2")
    env = gym.make(
        "drp_env:drp-" + str(drone_num) + "agent_" + map_name + "-v2",
        state_repre_flag="onehot_fov",
        reward_list=reward_list,
        goal_array=goal,
        start_ori_array=start,
    )
    obs = env.reset()
    print(f"observation_space:{env.observation_space}")
    print(f"action_space:{env.action_space}")

    done_all = False
    while not done_all:
        if render == True:
            env.render()
        print(f"obs:{obs}")  # current global observation
        actions = policy(obs, env)  # policy:input n_obs,env return each drone's action
        obs, reward, done, info = env.step(
            actions
        )  # transfer to next state once joint action is taken
        print(f"obs:{obs}, actions:{actions}, reward:{reward}, done:{done},info:{info}")
        done_all = all(done)
        env.get_obs()


if __name__ == "__main__":
    drone_num = 3  # the number of drones (min:2 max:30)
    map_name = "map_aoba01"  # the map name (available maps: "map_3x3","map_aoba01","map_osaka" )

    # reward_list is individual reward function where
    # "goal: 100" means one drone will obtain 100 rewards once it reach its goal.
    # Similarly, "collision"/"wait"/"move" are rewards when a collision happens/one drone wait one step/moves one step;
    reward_list = {
        "goal": 100,
        "collision": -10,
        "wait": -10,
        "move": -1,
    }  # Developers can freely to alter the reward function (rewards are not used as evaluation index)

    # If the start and goal are empty lists, they are randomly selected.
    start = [0,2,4,]  # drone1's start: node 0;  drone2's start: node 2;  drone3's start: node 4;
    goal = [3,6,1,]  # drone1's goal: node 3;  drone2's goal: node 6;  drone3's goal: node 1;
    render = True  # Choose whether to visualize

    """
    policy_evaluation() function is used to evaluate the "policy" developed by participants
    participants are expected to develop "policy",
    which is essentially a mapping from input(global observation) to output(joint action) at each step
    """
    policy_evaluation(
        policy=policy,  # this is an example policy
        drone_num=drone_num,
        map_name=map_name,
        reward_list=reward_list,
        goal=goal,
        start=start,
        render=render,
    )
