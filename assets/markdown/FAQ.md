# Frequently Asked Questions

## Contents

* [Installation](#installation)
* [AAMAS participation](#aamas)
* [Drone Behavior](#drone)


<a id="installation"></a>

### Installation

#### Q1
Can python be anything other than ``3.11.4``?

#### A1
If the environment is running, it should be fine, not limited to ``3.11.4`` in particular. I can't guarantee since I haven't actually run it, but it should work for ``3.8`` or higher. If you change the Python version, you'll need to prepare correct the module versions.

### AAMAS participation

#### Q1
If my team is invited to attend the DRP competition meeting at AAMAS, do we have to register for AAMAS?

#### A1
DRP competition participants can attend the meeting.
If you want to attend online, No registration for AAMAS is required.
In contrast, for in-person participants, as competitions are a part of the main AAMAS program, a ticket to attend the main program of AAMAS is necessary.  
Teams will be invited if they are selected as [finalists](https://drp-challenge.com/#/guidelines) at May 3.
<!-- Once finalists are selected, we are going to ask whether they will attend AAMAS virtually or in person. -->

#### Q2
When and where is the DRP competition at AAMAS ?

#### A2
It is going to take place on May 9 . 
We will inform you via email once we are notified by AAMAS organizers.

#### Q3
Would the DRP competition organizers assist with my travel and/or accommodation if I participate in the DRP competition meeting at AAMAS?

#### A3
Regrettably, We cannot help with travel and/or lodging fee.

<a id="drone"></a>

### Drone Behavior

#### Q1 
Can a drone do "wait" action while being at the edge?

#### A1
Yes.

#### Q2 
Why did the green agent "wait" action for 2 steps in node 8 at [Pattern1](https://github.com/DrpChallenge/main/blob/main/assets/img/score_1.png)?

#### A2
From an optimal viewpoint, there is no need to wait for  2 steps in node 8.
We just showed a possibility.

#### Q3
In [Pattern1](https://github.com/DrpChallenge/main/blob/main/assets/img/score_1.png), when orange drone starts from node 3 and goes to node 0, the distance is 17, the number of move steps is 4, which results in 20. 
How to interpret this fact?

#### A3
When 3 steps passed, Orange drone is in the middle of node 0 and 3.
(Two more distances short of node 0.)
When this drone do "move" action to node 0 at fourth steps, it moves 2 unit distances and reach node 0, although it can move 5 unit distances.
At that time, it is not possible to move to another node ( such as node 2 or 4) just because the fourth step can move the remaining three unit distances.

#### Q4 
There are 2 possible actions for the agent, wait and move, and when an agent wants to decide on its action, will it happen when it is in the node or can it make a decision when moving between two nodes

#### A4
The action is to choose one of the nodes to move, rather than just move and wait.
As illustrated in the description of [joint_action](https://github.com/DrpChallenge/main?tab=readme-ov-file#development), if it chooses a non-adjacent node , it will wait at the current position (node or edge). If the node chosen is an adjacent node, it will move one step forward to the node.


