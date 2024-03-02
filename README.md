
# Introduction to DRP Environment

# Index
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

> [!NOTE]
> If this is your first time reading this introduction, you can skip from section 4 (Representation of Agent's Current Position) to section 7 (Agent Observation and Action).

> [!CAUTION]
> The method of calculating the score has changed as of 3/01.

> [!NOTE]
> This DRP Challenge web site is [this link](https://drp-challenge.com/#/overview).Please check.

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
The goal is to maximize [score](#score)).
You can test your developed (``policy/policy.py``) by loading it in ``policy_tester.py``.

<a id="calculate_score"></a>

### Calculate score

When you want to calculate the score , please run ``calculate_score.py``.
Once the execution finishes , you can get json files containing the score(named ``final_score``).
The environment information  used for  score calculating is in ``score/problems.py``. Participants are forbidden from changing this file.

<a id="score"></a>

#### The ways of calculating score

> [!CAUTION]
> The method of calculating the score has changed as of 3/01.

The score is determined by the total number of steps each agent takes to reach the goal. If agents collide, agents that have not reached the goal are considered to have taken the maximum number of steps, which is 100 steps. The objective is to minimize this number of steps.

Under the same environment settings, execute 100 runs, where the average score across these runs becomes the subtotal score. Repeat the same procedure for all environment settings, and the total of these scores becomes the final score.

<img src = assets\img\score.png width="85%">

<a id="policy.py"></a>

### policy.py

Policy function takes each agent's position information as input and generates the corresponding action for each agent.**Participants can add other functions and files to customize environment( unless change the fundamental behavior of the agents and the environment ) but ensure that the format calls the policy function when submitting. Policy function may be associated with a class.**

These following code is example of policy.py.

```
import gym
import random

### submission information ####
TEAM_NAME = "KunwooLee"
##############################

def policy(n_obs, env): 
    #Random Policy 
    actions = []
    for agi in range(env.agent_num):
        _, avail_actions = env.get_avail_agent_actions(agi,env.n_actions)
        actions.append(random.choice(avail_actions))

    return actions
```
``TEAM_NAME`` must be the same as the name registered on the DRP website (or the team name if participating as a team). 


<a id="Problem"></a>

### Problem
We use several maps for calculate score: ``map_3x3``, ``map_aoba01``,``map_shibuya``.
We randomly choose agent's start/ goal node so that some problems  may be impossible to reach their goal.
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

<!-- 
## The minimum Configuration

```
​#import necessary module
import gymnasium as gym
from stable_baselines3 import PPO
# Setting Environment
env=gym.make("drp_env:drp-2agent_map_3x3-v2", state_repre_flag = "onehot_fov")

n_obs=env.reset()
print("n_obs", n_obs, type(n_obs),)
print("action_space", env.action_space)
print("observation_space", env.observation_space)

for _ in range(50):
    env.render() # Visualization of Movement

    actions = []
    for agi in range(env.agent_num):
        _, avail_actions = env.get_avail_agent_actions(agi,env.n_actions)
        actions.append(random.choice(avail_actions))

    n_obs, reward, done, info = env.step(actions)

    print("actions", actions, "reward", reward, done)
    print("info", info)
    print("n_obs", n_obs)

    input("Press ENTER to continue")
```

#### Setting Environment
* Generate the environment using `env = gym.make()`.([Further details are elaborated in another section.](#2-variables-for-gymmake))
```
drp_env:drpSB-{agent_num}agent_{map_name}-v1
```
``agent_num``: Number of agents, can be set from 1 to 6 (refer to Drp_env/init.py).
``map_name``: Specify the name of the available map.
* Regarding currently available maps (refer to ``Drp_env/init.py``):
    "map_3x3" 
    "map_aoba01"
    "map_paris"
    are available

are usable.
* It is also possible to set new rewards (reward: the reward obtained when an agent takes an action, see [below](#reward) for details). -->

<!-- #### Visualization of Movement
Check how the trained model behaves in practice.
In this Drp environment, the simulation ends when a drone collides with another drone or when all agents reach their goals.

<a id="example_some_varibales_and_function"></a>

```
vec_env = model.get_env()
obs = vec_env.reset() #Setting init
done = False
while done == False:
    env.render()
    actions = []
    for agi in range(env.agent_num):
        _, avail_actions = env.get_avail_agent_actions(agi,env.n_actions)
        actions.append(random.choice(avail_actions))

    n_obs, reward, done, info = env.step(actions)
``` -->
<!-- 
Alternatively, it can be segmented by steps or other criteria. -->

<a id ="environment"></a>

### The Drone Delivery Routing Problems Environment

<a id ="file"></a>

#### 1.File Structure
<pre>
main
├── README.md
├── drp_env
│   ├── __init__.py
│   ├── drp_env.py 
│   ├── EE_map.py
│   ├── map
│   └── state_repre
├──  for_epymarl
├──  score
│       ├──  problems.py
├──policy_tester.py
├──policy
│     └──  policy.py
└── calculate_score.py
</pre>

name                              |  description
----------------------------------|------------------------------------------------------------------------------------
drp_env                           |  the directory for package __drp_env__
for_epymarl                       |  files required to work with epymarl
score                             |  files required to calculate score
policy                            |  your workspace

Directories/files in drp_env:

name                              |  description
----------------------------------|------------------------------------------------------------------------------------
\_\_init\_\_.py                   |  register environments
drp_env.py                        |  environment with gym structure
EE_map.py                         |  process related to network structure
map                               |  csv files about map information
state_repre                       |  manage observation of environments

Important files relate to this competition
name                              |  description
----------------------------------|------------------------------------------------------------------------------------
policy_tester.py                     |  test your policy.py code 
score/problems.py                  |  Information about the map we use to calculate the score
score/calculate_score.py                |  calculate the score using policy.py
policy/policy.py                         |  returns agent's action according to the environment


<a id ="variable"></a>

#### 2. Variables for gym.make()

* `speed`: Represents the speed of all agents movement. Default is 5.

* `start_ori_array`: Starting positions. If not specified, they are randomly chosen.

* `goal_array`: Goal positions. If not specified, they are randomly chosen. Don't conflict with `start_ori_array`.

* `visu_delay`: Settings for the render function ( visualization of drone locations ). Default is 0.3.

* `reward_list`: Rewards given when an action is taken by the drone. Default: `{"goal": 100, "collision": -10, "wait": -10, "move": -1}` 

* `collision`: Default is "terminated." If changed to "bounceback," the 'done' in the step function becomes False when collision is detected.

<a id ="functions"></a>

#### 3. Functions in the DRP Environment

- `get_avail_agent_actions`: Searches for actions available to the agent

- `reset`: Sets the initial values and destination for the agent. If not specified, random nodes are set.

- `reward`: Sets the reward for each agent. Note that it doesn't directly return the values defined in `reward_list`.(Please see [below](#reward))

- `render`: Visualizes the state of agents at each step.

- `close`: `print('Environment CLOSE')`

- `get_pos_list`: Returns the current positions and states of all agents in a dictionary-list format.

- `step`: [Please see below](#step)

- `get_log` : the results of each run can be displayed.

<!-- The following example uses some of these functions.

```
import gym
import random

def policy(n_obs, env):  # Random Policy
    actions = []
    for agi in range(env.agent_num):
        _, avail_actions = env.get_avail_agent_actions(agi, env.n_actions)
        actions.append(random.choice(avail_actions))

    return actions

env = gym.make("drp_env:drp-2agent_map_3x3-v2", state_repre_flag="onehot_fov")
for epi in range(3):
    n_obs = env.reset()
    goal_checker = False
    while not goal_checker:
        env.render()
        actions = policy(n_obs, env)
        n_obs, _, done, _ = env.step(actions)
        goal_checker = all(done)
        print(env.get_pos_list())
for epi in range(3):
    log = env.get_log(epi + 1)
    print(log) 

``` -->

> [!NOTE]
> If this is your first time reading this introduction, you can skip from section 4 (Representation of Agent's Current Position) to section 7 (Agent Observation and Action).


<a id ="position"></a>

#### 4. Representation of Agent's Current Position

- `Node number`: Defined by the map being used. The node numbers in the rendered representation correspond to the node numbers.
- `Edge number`: Consists of the numbers of the two nodes at both ends of the edge. If there is an edge between node 3 and node 5, the edge number is (3, 5).

<a id ="obs"></a>

- `Observation (obs)`: Primarily represented as a numpy.array. This object divide into two parts : `self position` and `goal position`.  `self position` represents where the agent is and `goal position` represents where the agent`s goal is.
The element represents the information of node "n". When an agent exists in node "n", the nth element of obs is set to 1. 
<!-- When an agent exists between node "n" and node "n+1", the sum of the "n" and "n+1" elements of obs becomes 1. In this case, the ratio of the distances between node "n+1" and the agent and node "n" and the agent is reflected in the numbers of the respective elements.  -->

<a id ="step"></a>

#### 5. The Step Function

The Step function, roughly speaking, is a function that takes a list containing the actions (node numbers) taken by each agent at this step as input and reflects the environment after taking those actions. As output, it returns information such as the positions of each agent and whether they have reached their goals.

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

<a id = "reward"></a>

#### 6. Definition of Each Action and Processing of Corresponding Rewards

* Wait: Agent can be "wait" state only when it is in node. 
* Collision:Agents are considered to have collided if the distance between each agent is less than or equal to 5.
* Goal:The step at which a drone reaches its destination is referred to as the "goal" step. An agent that has reached its goal continues to be in a "wait" state at that destination until the environment is done .  

Rewards are modified based on the values defined in `reward_list`. "goal" rewards are as defined in `reward_list`. For other actions, rewards are the values defined in `reward_list` multiplied by __the agent's speed__.

<a  id = observation></a>

#### 7. Agent Observation and action 

Be careful, each agent usually doesn't know the information of other agents. Only when agents are on adjacent edges, they know each other's locations. When an agent is on an edge, it cannot change directions. This means that the agent cannot backtrack when it is on an edge and another agent came to agent's destination node.

<a  id = end></a>

#### 8. The condition which environment is done

If the environment meets any of these condition, the environment is done at the step when it happens.

- Collision happens.
- The number of steps over 100.
- All agents reach goal.

<a  id = map></a>

#### 9. Plan view of maps

#### map_3x3
<img src = assets\img\map3_3.png width="55%">

#### map_aoba01
<img src = assets\img\map_aoba01.png width="55%">

#### map_shibuya
<img src = assets\img\map_shibuya.png width="55%">


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
