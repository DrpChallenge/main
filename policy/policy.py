import gym
import random

### submission information ####
TEAM_NAME = "your_team_name" 
#TEAM_NAME must be the same as the name registered on the DRP website 
#(or the team name if participating as a team).
##############################

def policy(obs, env): #Random Policy 
    actions = []
    for agi in range(env.agent_num):
        #get_avail_agent_actions is used to get all the availble actions at current step
        _, avail_actions = env.get_avail_agent_actions(agi,env.n_actions)
        actions.append(random.choice(avail_actions))

    return actions