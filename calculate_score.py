import gym
import time
import json
from datetime import datetime

import policy.policy as submitted
import score.problems as problems

### Parameters
TEST_EPI_NUM = 100
###############

def calculate_score(instances, policy):
    """
    Once your policy has been developed, 
    you can run this file without any edition.

    It outputs the following 4 criterias for each problem in a json file
    1. runtime: mean of the runtime per each episode
    2. distance: mean of total moving distance of every agents
    3. time_step: mean of the termination time step of each episode
    4. goal_rate: goal rate

    However, we only take "time_step" of each problem as the final evaluation index.

    """
    scores = []
    for instance in instances:
        map_name = instance["map"]
        agent_num = instance["agent_num"]
        start_arr = instance["start"]
        goal_arr = instance["goal"]

        # make environment
        env = gym.make(
            "drp_env:drp-" + str(agent_num) + "agent_" + map_name + "-v2",
            state_repre_flag="onehot_fov",
            goal_array=goal_arr,
            start_ori_array=start_arr,
        )

        # recore runtime of each episode
        time_record = []
        goal_rate_list = []
        subtotal_score_same_environment = []
        # run environment with submitted policy
        for epi in range(TEST_EPI_NUM):
            start_time = time.time()
            n_obs = env.reset()
            goal_checker = False
            goal_step =  [None] * agent_num
            while not goal_checker:
                actions = policy(n_obs, env)
                n_obs, reward, done, info = env.step(actions)
                goal_checker = all(done)
                for i in range(agent_num):
                    if reward[i] == 100: #goal
                        goal_step[i] = info["step"]
                    elif reward[i] == -50: #collision
                        if goal_step[i] == None:
                            goal_step[i] = 100
            for i in range(agent_num):
                if goal_step[i] == None:
                    goal_step[i] = 100
            pos = env.get_pos_list()
            goal_agent = 0
            for i in range(len(pos)):
                if (
                    pos[i]["type"] == "n" and pos[i]["pos"] == goal_arr[i]
                ):  # if agent goal
                    goal_agent += 1  # max(goal_agent)=agent_num
            goalrate = goal_agent / agent_num
            end_time = time.time()
            time_record.append(end_time - start_time)
            goal_rate_list.append(goalrate)
            subtotal_score_same_environment.append(sum(goal_step))

        # calculate score from logs in environment
        score = {"instance_id": instance["id"]}

        mean_runtime = 0.0
        sum_runtime = 0.0

        mean_distance = 0.0
        sum_distance = 0.0

        mean_timestep = 0.0
        sum_timestep = 0.0

        goalrate = 0.0
        # goalcount = 0
        distance = []
        
        for epi in range(TEST_EPI_NUM):
            log = env.get_log(epi + 1)
            sum_runtime += time_record[epi]
            sum_distance += sum(log["distance_from_start"])
            sum_timestep += log["termination_time"]
            # if log["result"] == "goal": # if goal_count  + 1 if "all" agent goal
            #     goalcount += 1
            distance.append(1/sum(log["distance_from_start"]))
        list_of_score = []
        for i in range(len(goal_rate_list)):
            list_of_score.append(distance[i] * goal_rate_list[i])
        mean_runtime = sum_runtime / TEST_EPI_NUM
        mean_distance = sum_distance / TEST_EPI_NUM
        mean_timestep = sum_timestep / TEST_EPI_NUM
        goalrate = sum(goal_rate_list) / TEST_EPI_NUM
        mean_goal_step = sum(subtotal_score_same_environment) / TEST_EPI_NUM
        score["runtime"] = mean_runtime
        score["distance"] = mean_distance
        score["time_step"] = mean_timestep
        score["goal_rate"] = goalrate
        score["goal_count"] = goal_rate_list.count(1.0)
        score["subtotal_score"] = mean_goal_step
        scores.append(score)
        # delete env
        del env
    subtotal_scores = [score["subtotal_score"] for score in scores]
    final_score = sum(subtotal_scores) / len(subtotal_scores)
    score_dict = {
        "Author": submitted.TEAM_NAME,
        "Scored time": str(datetime.now().strftime("%Y-%m-%H-%M-%S")),
        "Score": scores,
        "final score": final_score,
    }

    json_filename = submitted.TEAM_NAME + ".json"
    with open(json_filename, "w") as f:
        json.dump(score_dict, f, indent=4)
    return scores,final_score

if __name__ == "__main__":
    scores,final_score = calculate_score(problems.instances, submitted.policy)
