
## Appendix
* [1.File Structure](#file)
* [2. Default hyper-parameters in gym.make()](#gymmake)
* [3. The functions in class of 'env'](#functions)
* [4. env.step()](#step)

<a id ="file"></a>

### 1.File Structure

<pre>

main
├── README.md
├── drp_env # the directory for drp challenge environment
│   ├── __init__.py
│   ├── drp_env.py 
│   ├── EE_map.py
│   ├── map
│   └── state_repre
├──  problem  
│     └──  problems.py # 30 problems are fixed for evaluation
├──policy_tester.py  # test your developed policy # feel free to customize this file
├──policy # your workspace
│     └──  policy.py # your development
└── calculate_cost.py  # output evaluation result in a json file

</pre>


<a id ="gymmake"></a>

#### 2. Default hyper-parameters in gym.make()
Although drp env can be easily constructed by the following codes, there are other hyper-parameters about env can be customized.
```
    env = gym.make(
        "drp_env:drp-" + str(agent_num) + "agent_" + map_name + "-v2",
        state_repre_flag="onehot_fov",
        reward_list=reward_list,
        goal_array=goal,
        start_ori_array=start,
    )
```
You can be free to alter the following hyper-parameters in your development, but we will keep the default values to evaluate

* `speed`: Represents the distance of moving in one step (all drones have same speeds and default value is 5). 

* `start_ori_array`: Starting positions. If not specified (start_ori_array = []), they are randomly generated.

* `goal_array`: Goal positions. If not specified (goal_array = []), they are randomly generated. 

* `visu_delay`: Waiting time for one step. Default is 0.3s.

* `reward_list`: Rewards given when an action is taken by the drone. Default values are : `{"goal": 100, "collision": -10, "wait": -10, "move": -1}` 

* `collision`: Default is "terminated" mode where current episode terminate once collision happens. The another mode is  "bounceback," where the drones would bounceback when collision happens. 
  
* `time_limit`: We set one episode with maximum 100 steps. 

<a id ="functions"></a>

#### 3. The functions in class of 'env'  
Since the class of 'env' is also as an input passed to policy, there are many functions can be used.Please refer [this file](https://github.com/DrpChallenge/main/blob/main/drp_env/drp_env.py).

- `env.get_avail_agent_actions()`: Searches for actions available for all drones

- `env.get_pos_list()`: Returns the current positions and states of all agents in a dictionary-list format.

- `env.G`: Returns the map information including nodes and edges. Map is constructed by ``NetworkX`` so that you can utilize methods consistent with the usages of ``NetworkX`` ,if you want to obtain detail information about map.(Ex.``env.G.nodes``) 

- `step`: [Please see below](#step)

- `reset`: Sets the initial and destination node for the agent. If not specified, random nodes are set.

- `render`: Visualizes the state of agents at each step.

- `get_log` : the results of each episode can be displayed.

<!--

- `reset`: Sets the initial values and destination for the agent. If not specified, random nodes are set.

- `reward`: Sets the reward for each agent. Note that it doesn't directly return the values defined in `reward_list`.(Please see [below](#reward))

- `render`: Visualizes the state of agents at each step.

- `close`: `print('Environment CLOSE')`
- `step`: [Please see below](#step)

- `get_log` : the results of each episode can be displayed.
-->


<!-- For example, `Node number`: is the node numbers in the rendered representation correspond to the node numbers. `Edge number`: Consists of the numbers of the two nodes at both ends of the edge. If there is an edge between node 3 and node 5, the edge number is (3, 5). -->


<a id ="step"></a>

#### 4. env.step() 

- `Input`: joint action, which contains the actions (node numbers) taken by each agent.
- `Output`:
     - `obs`: each agent's observation
     - `reward`: Represents the each reward received by single agent.
     - `done` : Returns False. It becomes True when all drones reach the goal or when a collision occurs.
     -  `info`: The following list.
          - `goal`: Returns True if the agent has reached its goal, otherwise False.
          - `collision`: Returns True if a collision has occurred, otherwise False.
          - `timeup` : Returns True if the number of steps is larger than 100.
          - `distance_from_start` : Distance form start.
          - `step` : The number of steps from agent starts
          - `wait` : When agent be wait state, this count increases by one.


<!-- <a  id = using-epymarl></a>

## Using Epymarl

[epymarl](https://github.com/uoe-agents/epymarl) is a multi agent reinforcement learning framework.

You can use drp_env with epymarl

1. install epymarl
    ```
    git clone https://github.com/uoe-agents/epymarl
    ```

2. Replace ``epymarl/src/envs/__init__.py`` with ``drp/for_epymarl/envs/__init__.py``

3. Replace ``epymarl/src/config/envs/gymma.yaml`` with ``drp/for_epymarl/config/gymma.yaml``

4. Example of using drp_env

    ```
    python3 src/main.py --config=iql --env-config=gymma with env_args.time_limit=100 env_args.key="drp_env:drp-1agent_map_3x3-v2" env_args.state_repre_flag="onehot"
    ``` -->
