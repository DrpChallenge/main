
# Codes of DRP Challenge ([Website](https://drp-challenge.com/#/overview))

# Outline
* [Installation](#installation)
* [Usage  ](#usage)
    - [Calculate score](#calculate_score)
    - [Policy.py](#policy.py)
    - [Problem](#Problem)
<!-- * [The minimum Configuration](#Minimum) -->
* [The Environments](#environment)
    - [1. File Structure](#file)
    - [2. Variables for gym.make()](#variable)
    - [3. Functions in the Drp Environment](#functions)
    - [4. Representation of Agent's Current Position](#position)
    - [5. The Step Function](#step)
    - [6. Definition of Each Action and Processing of Corresponding Rewards](#reward)
    - [7. Agent Observation and action](#observation)
    - [8. The condition which environment is done](#end)
    - [9. Plan view of maps](#map)
<!-- * [Using Epymarl](#using-epymarl) -->
<!--
> [!NOTE]
> If this is your first time reading this introduction, you can skip from section 4 (Representation of Agent's Current Position) to section 7 (Agent Observation and Action).

> [!CAUTION]
> The method of calculating the score has changed as of 3/01.
-->

## Installation
This environment works in  `python==3.11.4` .
We recommend you to create an exclusive environment like
```
conda create -n drpdev python=3.11.4
conda activate drpdev    
```
before executing the following code.
```
git clone https://github.com/DrpChallenge/main.git
pip3 install -e ./main
pip3 install -r ./main/requirements.txt
```
Then it will show the following GUI, if you run `policy_tester.py` .

<img src = assets\img\drpexample.png width="25%">

Success :tada::tada: Let's start to develop algorithms for DRP challenge!

<a id="usage"></a>

## Development  

In this competition, participants are expected to develop (``policy/policy.py``), which is essentially a mapping from input(global state: includes all drones' obseravations) to output(joint action: includes all drones' actions) at each step. 

- `Observation (obs)`: Primarily represented as a numpy.array. This object divide into two parts : `self position` and `goal position`.  `self position` represents where the agent is and `goal position` represents where the agent`s goal is.
The element represents the information of node "n". When an agent exists in node "n", the nth element of obs is set to 1. 
<!-- When an agent exists between node "n" and node "n+1", the sum of the "n" and "n+1" elements of obs becomes 1. In this case, the ratio of the distances between node "n+1" and the agent and node "n" and the agent is reflected in the numbers of the respective elements.  -->

**Termination Condition** Current episode will terminate once it meets any of the following 3 conditions. 
- Collision happens.
- The number of steps over 100.
- All agents reach goal.

**Goal** 
The goal is to maximize [score](#score)) without collision happens.
You can test your developed (``policy/policy.py``) by loading it in ``policy_tester.py``.

<a id="calculate_score"></a>

## Evaluation
### Score for each problem
The score is determined by the total number of steps each agent takes to reach the goal. If agents collide, agents that have not reached the goal are considered to have taken the maximum number of steps, which is 100 steps. The objective is to minimize the summation of all drones' steps taken.

### Final score of all problems
We use three maps for evaluations: ``map_3x3``, ``map_aoba01``,``map_shibuya``.
<p align="center">
<img src = assets\img\map3_3.png width="25%">
<img src = assets\img\map_aoba01.png width="25%">
<img src = assets\img\map_shibuya.png width="25%">
</p>

Each map will be evaluated on various drone numbers and various start-goal pairs.
We call one pattern (fix map, drone number, and start-goal pair) as a problem, there are totally 30 problems which written in ``score/problems.py``,as shown in the following table. (Participants are forbidden to altering this file)


map_name                              |  number of agent| number of problem
----------------------------------|---------------------------------------|---------------------------------------------
map_3x3             |  2 | 3
map_3x3             |  3 | 4
map_3x3             |  4 | 3
map_aoba01          |  4 | 3
map_aoba01          |  6 | 4
map_aoba01          |  8 | 3
map_shibuya           |  8 | 3
map_shibuya           |  10 | 4
map_shibuya           |  12 | 3


Thus, the final score is the summation of 30 problems socres.
However, if collision happens, the score of that map will not be countted.

Once your (``policy/policy.py``) has been depolyed, you can run ``calculate_score.py``, which will outputs a json file (your_team_name.json) including the score (named ``final_score``).


<a id ="environment"></a>

## Additional Info

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
├──  score  
│       ├──  problems.py # 30 problems are fixed for evaluation
├──policy_tester.py  # test your developed policy 
├──policy # your workspace
│     └──  policy.py # your development
└── calculate_score.py  # output evaluation result in a json file
</pre>


<a id ="variable"></a>

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

* `start_ori_array`: Starting positions. If not specified, they are randomly generated.

* `goal_array`: Goal positions. If not specified, they are randomly generated. 

* `visu_delay`: Waiting time for one step. Default is 0.3s.

* `reward_list`: Rewards given when an action is taken by the drone. Default values are : `{"goal": 100, "collision": -10, "wait": -10, "move": -1}` 

* `collision`: Default is "terminated" mode where current episode terminate once collision happens. The another mode is  "bounceback," where the drones would bounceback when collision happens. 
  
* `time_limit`: We set one episode with maximum 100 steps. 

<a id ="functions"></a>

#### 3. The functions in class of 'env'  
Since the class of 'env' is also as an input passed to policy, there are many functions can be used.

- `env.get_avail_agent_actions()`: Searches for actions available for all drones
<!--

- `reset`: Sets the initial values and destination for the agent. If not specified, random nodes are set.

- `reward`: Sets the reward for each agent. Note that it doesn't directly return the values defined in `reward_list`.(Please see [below](#reward))

- `render`: Visualizes the state of agents at each step.

- `close`: `print('Environment CLOSE')`
- `step`: [Please see below](#step)

- `get_log` : the results of each run can be displayed.
-->

- `env.get_pos_list()`: Returns the current positions and states of all agents in a dictionary-list format.

- `env.G`: Returns the map informations including nodes and edges.　For example, `Node number`: is the node numbers in the rendered representation correspond to the node numbers. `Edge number`: Consists of the numbers of the two nodes at both ends of the edge. If there is an edge between node 3 and node 5, the edge number is (3, 5).



<a id ="step"></a>

#### 5. About env.step() 

- `Input`: action, which contains the actions (node numbers) taken by each agent.
- `Output`:
     - `obs`: [Please see above](#obs)
     - `reward`: Represents the each reward received by single agent.
     - `done` : Typically returns False. It becomes True when all drones reach the goal or when a collision occurs.
     -  `info`: The following list.
          - `goal`: Returns True if the agent has reached its goal, otherwise False.
          - `collision`: Returns True if a collision has occurred, otherwise False.
          - `timeup` : Returns True if the number of steps is larger than 100.
          - `distance_from_start` : Distance form start 
          - `step` : The number of steps from agent starts
          - `wait` : When agent be wait state, this count increases by one.


<a  id = using-epymarl></a>

<!-- ## Using Epymarl

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
