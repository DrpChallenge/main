#return the evaluation values for each node for each agent according to current state
#the evaluation values based on the shortest path after choosing avalable actions.
import numpy as np
import networkx as nx

def hrs_hot_func(env,n_obs):
    hrs_hot=np.zeros( ( env.agent_num,  len(list(env.G.nodes())) ) )

    for agi in range(env.agent_num):
        available_action_i=env.get_avail_agent_actions(agi, env.n_actions)[1]
        shortest_path_distance_dict={}
        #fixed agent agi
        for ava_action_j in available_action_i:
            #distance to node of ava_action_j
            current_x1,current_y1=n_obs[agi][0],n_obs[agi][1]
            x=round(env.pos[int(ava_action_j)][0],2)-current_x1
            y=round(env.pos[int(ava_action_j)][1],2)-current_y1
            dist_to_ava_action_j=round(np.sqrt( np.square(x) + np.square(y) ),2)

            #length_after_ava_action
            shortest_path_length_after=nx.shortest_path_length(env.G, source=ava_action_j, target=env.goal_array[agi], weight='weight')
            
            #total distance
            shortest_path_distance=round(shortest_path_length_after+dist_to_ava_action_j,2)

            #plus waiting time if there exist
            if str([n_obs[agi][0],n_obs[agi][1]]) in [str(ele) for ele in env.pos.values()]: #s=(0.0, 5.0)
                node=[k for k, v in env.pos.items() if str(v) == str([n_obs[agi][0],n_obs[agi][1]]) ][0]  #node 0
                if str(node)==str(ava_action_j):
                    #print("wait")
                    shortest_path_distance+=env.speed

            #print("shortest_path_distance",shortest_path_distance)
            shortest_path_distance_dict[ava_action_j]=round(shortest_path_distance,2)
            
        #print(shortest_path_distance_dict)
        shortest_path_distance_dict_rate=dict(zip(available_action_i, [min(shortest_path_distance_dict.values())/act for act in shortest_path_distance_dict.values()]))
        for ava_action_j in available_action_i:
            hrs_hot[agi][ava_action_j]=shortest_path_distance_dict_rate[ava_action_j]
    
    return hrs_hot

