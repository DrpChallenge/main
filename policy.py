import gym
import random

### submission information ####
TEAM_NAME = "KunwooLee" 
#must be the same as the name registered on the DRP website (or the team name if participating as a team).
##############################

def policy(n_obs, env): #Random Policy 
    actions = []
    for agi in range(env.agent_num):
        _, avail_actions = env.get_avail_agent_actions(agi,env.n_actions)
        actions.append(random.choice(avail_actions))

    return actions