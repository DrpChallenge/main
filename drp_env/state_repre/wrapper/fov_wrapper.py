import numpy as np
import networkx as nx

from drp_env.state_repre.wrapper.hrs_hot_file import hrs_hot_func

def neighbor_filter_obs(env, state_repre_flag):

    agent_num = env.agent_num
    n_act = env.n_actions
    all_onehot_obs = np.array(env.obs_onehot)
    onehot_obs = all_onehot_obs[:,:n_act]
    G = env.ee_env.G

    state = [0] * n_act
    pos_list = []

    # get all agent state and position
    for i, obs_i in enumerate(onehot_obs):
        edge_or_node = tuple([i for i, o in enumerate(obs_i) if o!=0])
        if len(edge_or_node)==1:
            node = edge_or_node[0]
            pos = {"type": "n", "pos": node}
            obs_i = np.array(obs_i)*agent_num
        else:
            edge = edge_or_node
            pos = {"type": "e", "pos": edge, "current_goal": env.current_goal[i], "current_start": env.current_start[i], "obs": obs_i}
        state += obs_i
        pos_list.append(pos)
    # print("state", state)
    # print("pos_list", pos_list)

    neighbor_filter = calc_neighbor_filter(pos_list, G, state, n_act, agent_num)

    if state_repre_flag=="coordinate2":
        return neighbor_filter
    elif state_repre_flag=="onehot_fov":
        obs = all_onehot_obs
    elif state_repre_flag=="heu_onehot_fov":
        obs = hrs_hot_func(env, env.obs)


    #print("ori_obs", obs)

    for i in range(agent_num):
        for j in range(n_act):
            #print(i,j,neighbor_filter[i][j])
            if neighbor_filter[i][j]<0:
                obs[i][j] = neighbor_filter[i][j]

    return obs

def get_nodes_to_be_consideration(agent_pos, graph):
    if agent_pos["type"]=="n":
        start_node = agent_pos["pos"]
        target_node = list(nx.neighbors(graph, start_node))
    elif agent_pos["type"]=="e":
        start_node = agent_pos["current_goal"]
        node_set = set(nx.neighbors(graph, start_node))
        node_set.discard(agent_pos["current_start"])
        target_node = list(node_set)
    return start_node, target_node

# return [ (0 or -1) * n_nodes ] * agent_num
# if there is another agent -> -1
def calc_neighbor_filter(pos_list, graph, state, n_act, agent_num):
    neighbor_list = []

    ###
    agent_goal_list = [0]*n_act
    for pos in pos_list:
        if pos["type"]=="e":
            agent_goal_list[pos["current_goal"]]+=1
    # print("agent_goal_list", agent_goal_list)
    ###

    for i in range(agent_num):
        goal_list = agent_goal_list.copy()
        pos_data = pos_list[i]
        start_node, target_nodes = get_nodes_to_be_consideration(pos_data, graph)
        c = [0]*n_act # (0 or -1) * n_nodes
        if pos_data["type"]=="e":
            # agent_goal_list[pos_data["current_goal"]]-=1 # priority???
            goal_list[start_node]-=1
            if state[start_node]>agent_num:
                c[start_node] = -1
            elif state[start_node]>0 and goal_list[start_node]>0:
                c[start_node] = -1
        elif pos_data["type"]=="n":
            for node in target_nodes:
                if state[node]>=agent_num or (state[node]>0 and state[start_node]>agent_num): # (an agent on node) or (an agent on edge(start_node, node))
                    c[node] = -1
                elif state[node]>0 and goal_list[node]>0: # an agent on edge(onehop-node, twohop-node) and its goal onehop-node
                    c[node] = -1
        ###
        # for i, goal in enumerate(agent_goal_list):
        #     if goal>0:
        #         c[i] = -1
        neighbor_list.append(c)
        ###


    return neighbor_list