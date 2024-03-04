
# Codes of DRP Challenge ([Website](https://drp-challenge.com/#/overview))

## Outline

* [Installation](#installation)
* [Development](#development)
* [Evaluation](#evaluation)
* [Appendix](#appendix)

## Installation
This environment works in  `python==3.11.4`.
We recommend you create an exclusive environment like
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
Then it will show the following GUI if you run `policy_tester.py`.

<img src = assets\img\drpexample.png width="25%">

Success :tada::tada: Let's start to develop algorithms for DRP challenge!

<a id="development"></a>

## Development  

#### ``policy/policy.py``
In this competition, participants are expected to develop ``policy/policy.py``, which is essentially a mapping from input(``observation``) to output (``joint action``) at each step. 

- `observation (obs)`: This object is divided into two parts: `self-position` and `goal position`.  `self-position` represents the agent's current location and `goal position` represents the agent's destination. The element represents the information of node "n". When an agent exists in node "n", the nth element of obs is set to 1. 
- `joint action`: The joint action represents the current destination node of each agent. It will not move unless the agent's adjacent nodes are specified. 

<p align="center">
 <img src="assets/img/policy.png" width="65%" >
</p>

#### Step and Episode

Every time each agent takes action, increases step count.
In other words, every time the ``step`` function is excused, the number of steps increases by one.

The episode ends upon conflict, exceeding 100 steps, or all agents reaching goals and restarting with a new environment ( If not specified indications, only the positions of the start and goal change.).


#### Goal
The goal in this competition is to minimize [score](#score) without collision happens.
You can test your developed (``policy/policy.py``) by loading it in ``policy_tester.py``.

<a id="evaluation"></a>

## Evaluation

We use three maps for evaluations: ``map_3x3``, ``map_aoba01``, ``map_shibuya``.

<p align="center">
  <img src="assets/img/map3_3.png" width="30%" >
  <img src="assets/img/map_aoba01.png" width="30%" >
  <img src="assets/img/map_shibuya.png" width="30%" >
</p>


Each map will be evaluated on various drone numbers and various start-goal pairs.
We call one pattern (fixed map, number of drones, and start-goal pair) as a problem and there are a totally of 30 problems which are defined in ``score/problems.py``. (Participants are forbidden to alter this file.)

<a id="score"></a>

#### Score for each problem

The score is determined by the total number of steps each agent takes to reach the goal. If agents collide, all agents that have not reached the goal yet are considered to have taken the maximum number of steps, which is 100 steps. The objective is to **minimize** the summation of all agents' steps taken.

We simulated 10 episodes of the same problem, and the score for each problem is the average of the scores.

#### Final score of all problems

The final score is the sum of the scores of the 30 problems.

Once your (``policy/policy.py``) has been deployed, you can run ``calculate_score.py``, which will outputs a json file (``your_team_name.json``) including the score (named ``final_score``).


Please refer to [this file](score\problems.py) for more detailed information about the problems. 

<a id ="appendix"></a>

## Appendix

Please refer to [this page](assets\markdown\appendix.md) to get more detailed information about the DRP environment. 