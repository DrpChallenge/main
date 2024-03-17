# Reinforcement Learning Implementation Example using PFRL Library

## Introduction
In this example, we demonstrate how to implement reinforcement learning using the PFRL library (a deep reinforcement learning library using PyTorch). We provide two scripts: `train_by_pfrl.py` for training a reinforcement learning agent using the DQN algorithm and `policy_prfl.py` for executing a trained policy.
### Dependencies
Before running the script, make sure to install the PFRL library using pip:
```
$ pip install pfrl
```
## `train_by_pfrl.py`

1. **Q-Function**: We define a neural network model called `QFunction` using PyTorch, which serves as the Action value function (a.k.a. Q-function) approximator for the DQN algorithm.

2. **Fully Decentralized Control**: We configure the DQN agent using PFRL. Each drone in the environment has its own agent (an independent Q-Function), and we create an array of agents accordingly, which corresponds to a fully decentralized control.

3. **Training Loop**: We run training episodes where the agents interact with the environment, collect experiences, and update their Q-values. The training loop consists of multiple episodes, each comprising interactions with the environment, actions selection, and agent updates.

4. **Model Saving**: After training, we save the trained models for each drone. 

## `policy_prfl.py`

5. **Model Loading**: After runing `train_by_pfrl.py`, a folder called `models` would be generated which save the trained models for each drone. In the policy function, we load the trained models  for each drone and use them to select actions based on the observations.

## Conclusion
This example demonstrates how to use the PFRL library to implement reinforcement learning, specifically the DQN algorithm, for a scenario involving multiple drones navigating a map environment. The `train_by_pfrl.py` script handles training, while `policy_prfl.py` demonstrates how to execute the trained policy.

I hope that this example helps readers.
