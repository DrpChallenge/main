import csv
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import copy 
import math
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), ''))

MAP_PARENT_DIR = "./map/"

UNREAL_MAP = [
    "map_3x3",
    "map_5x4",
    "map_8x5",
    "map_10x6",
    "map_10x8",
    "map_10x10",
    "map_aoba00",
    "map_aoba01",
]

class MapMake():

	def __init__(self, agent_num, start_ori_array, goal_array, map_name):
		print('MapMake initialized')
		self.agent_num = agent_num

		base_nodes = [0,2]
		self.base_nodes = base_nodes
		self.fig1 = plt.figure()
		self.ax3 = self.fig1.add_subplot(111)
		self.map_name = map_name
		map_dir = MAP_PARENT_DIR+map_name
		node_file_name, edge_file_name = map_dir+'/node', map_dir+'/edge'
		csv_nodes_number,csv_nodes_pos,csv_edges, csv_edges_weights = self.read_nodes_csv(node_file_name, edge_file_name)
		self.G, self.pos, self.edge_labels = self.Graph_initial(csv_nodes_number, csv_nodes_pos, csv_edges, csv_edges_weights)
		# self.n_nodes = len(self.G.nodes())
		if self.agent_num > len(csv_nodes_number) :
			print('Error: The number of agents exceeds the maximum numberof nodes on the graph')
			self.sta_code = 0
			self.close()
			sys.exit(0)
		else:
			print('Mal Environment initialized')

		print('Agent numbers', self.agent_num)

    # assignd by user
		self.input_start_ori_array = copy.deepcopy(start_ori_array)
		self.input_goal_array = copy.deepcopy(goal_array)
		
		self.start_ori_array = copy.deepcopy(self.input_start_ori_array)
		self.goal_array = copy.deepcopy(self.input_goal_array)
		
		if self.input_start_ori_array==[]:
			self.random_start()
		if self.input_goal_array==[]:
			self.random_goal()
		
		self.base_nodes = base_nodes

		print('Start node for each agent', self.start_ori_array)
		print('Goal node for each agent', self.goal_array)

		#self.start1_ori,self.goal1=0,5
		#self.start2_ori,self.goal2=3,4

	def random_start(self):
		self.G_nodes_copy = copy.deepcopy(list(self.G.nodes()))
		self.start_ori_array = []
		# G_nodes_copy=copy.deepcopy(list(self.G.nodes()))
		for i in range(self.agent_num):
			random_node = np.random.choice(self.G_nodes_copy)
			self.start_ori_array.append(random_node)
			self.G_nodes_copy.remove(random_node)
  
	def random_goal(self):
		self.goal_array = []
		# G_nodes_copy=copy.deepcopy(list(self.G.nodes()))
		for i in range(self.agent_num):
			random_node = np.random.choice(self.G_nodes_copy)
			self.goal_array.append(random_node)
			self.G_nodes_copy.remove(random_node)

	def read_nodes_csv(self, node, edge):
		csv_nodes_source = []
		csv_edges_source = []
		current_path = os.path.join(os.path.dirname(__file__), '')
		with open(current_path+node+'.csv') as f:
			reader = csv.reader(f)
			for row in reader:
				csv_nodes_source.append(row)

		with open(current_path+edge+'.csv') as f:
			reader = csv.reader(f)
			for row in reader:
				csv_edges_source.append(row)

		csv_nodes_source.remove(csv_nodes_source[0])#remove title row
		csv_edges_source.remove(csv_edges_source[0])#remove title row
		#About nodes
		csv_nodes_number = [int(i[0]) for i in csv_nodes_source]
		csv_nodes_pos = dict()
		for node in csv_nodes_source:
			#csv_nodes_pos[int(node[0])]=[ float(node[1]),float(node[2]) ]
			if self.map_name in UNREAL_MAP:
				csv_nodes_pos[int(node[0])] = [round(float(node[1]),2), round(float(node[2]),2)]
			else:
				csv_nodes_pos[int(node[0])] = [round(float(node[1])*1e5,2), round(float(node[2])*1e5,2)]
		
		#About edges
		csv_edges = []
		csv_edges_weights = []
		for i in range(len(csv_edges_source)):
			row = csv_edges_source[i]
			source = int(row[0])
			distention = int(row[1])
			#error
			distance = np.sqrt(((csv_nodes_pos[source][0]-csv_nodes_pos[distention][0])**2)+((csv_nodes_pos[source][1]-csv_nodes_pos[distention][1])**2))
			csv_edges.append((source, distention))
			csv_edges_weights.append((source, distention, distance))

		#print(csv_nodes_number)  #[0, 1, 2, 3, 4, 5, 6]
		#print(csv_nodes_pos)     #{0: (0.0, 5.0), 1: (2.0, 10.0), 2: (2.0, 0.0),....
		#print(csv_edges)         #[(0, 1), (0, 2), (1, 2), (1, 3), (2, 4),....
		#print(csv_edges_weights) #[(0, 1, 5.4), (0, 2, 5.4), (1, 2, 10.0),....
		return csv_nodes_number, csv_nodes_pos, csv_edges, csv_edges_weights

	def Graph_initial(self, csv_nodes_number ,csv_nodes_pos ,csv_edges ,csv_edges_weights):
		G = nx.Graph()  # Undirected Graph
		G_g = nx.Graph()               
		G.add_nodes_from(csv_nodes_number)                                 
		G.add_edges_from(csv_edges)
		self.pos = csv_nodes_pos
		G.add_weighted_edges_from(csv_edges_weights) #(始点，終点，重み)でエッジを設定
		self.edge_labels = {(i, j): int(w['weight']) for i, j, w in G.edges(data=True)} #エッジラベルの描画時に'weight'の表示を無くすための工夫
		self.G=G


		return self.G, self.pos, self.edge_labels


	def draw_weighted_graph(self, G ,pos):
		nx.draw_networkx_nodes(G, pos, node_size=500, node_color='skyblue',edgecolors='skyblue') #ノードを描画
		nx.draw_networkx_edges(G, pos, width=1) #エッジを描画
		nx.draw_networkx_labels(G, pos) #（ノードの）ラベルを描画
		nx.draw_networkx_edge_labels(G, pos, edge_labels=self.edge_labels) #エッジのラベルを描画
		#nx.draw_networkx_node_labels(G, pos, node_labels=node_labels) #エッジのラベルを描画
		nx.draw_networkx(self.G, with_labels = True,pos=self.pos,alpha=0.2, node_size=170, node_color='lightblue')
      

	def plot_map_dynamic(self, delay ,obs_old, obs, goal_array, agent_num, joint_action_old, reach_account, step, episode):# a must be a angle !!!list!!!
		self.agent_num = agent_num
		
		#for i in range(self.goods):
			#ax3.scatter(  self.pos[self.base_nodes[0]][0]-0.5, self.pos[self.base_nodes[0]][1]-i*1.3 , alpha=1, s=500, marker='*',c='grey')
		for base_node in self.base_nodes:
			self.ax3.scatter(self.pos[base_node][0], self.pos[base_node][1], alpha=1, s=1500, marker='1', c='steelblue')
		
		c = [(i+1)/self.agent_num  for i in range(self.agent_num)]
		#print("c",c)

		for i in range(self.agent_num):
		
			sc = self.ax3.scatter(obs[i][0], obs[i][1] ,alpha=1, s=600 ,c=c[i], cmap='rainbow', vmin=0, vmax=1)
			self.ax3.annotate(str(joint_action_old[i]), (obs[i][0], obs[i][1] ), size = 12, color = "white")

			if self.pos[goal_array[i]]!=7777:
				self.ax3.scatter(self.pos[obs[i][3]][0], self.pos[obs[i][3]][1], alpha=1, s=700, c=c[i], cmap='rainbow', vmin=0, vmax=1)
			
			#if s[i][0] == self.pos[ s_old[i][2] ] and self.agent_carry_goods_array[i]==1:
			
			#ax3.scatter(  s[i][0][0], s[i][0][1] , alpha=1, s=500, marker='*',c='grey')
			#self.agent_carry_goods_array[i]=0
		
			#print( s_old[i], s[i])
			if [obs_old[i][0], obs_old[i][1]]==[ obs[i][0], obs[i][1]]: #dont change positions
				if [obs[i][0], obs[i][1]]==self.pos[obs[i][3]] : #goal
					self.ax3.annotate('reach1', (obs[i][0]-0.2, obs[i][1]+0.2))     
				else:
					self.ax3.annotate('wait1', (obs[i][0]-0.2, obs[i][1]+0.2))
				
				
			# arrow
			"""
			if  [obs_old[i][0], obs_old[i][1]]!=self.pos[obs[i][3]]:

			arrow_length=1
			self.ax3.annotate('', xy=[obs_old[i][0]+arrow_length*np.cos(angle[i]/57 ),obs_old[i][1]+arrow_length*np.sin(angle[i]/57 )] , xytext=[obs_old[i][0], obs_old[i][1]],
						arrowprops=dict(shrink=0, width=3, headwidth=8, 
										headlength=10, connectionstyle='arc3',
										facecolor='gray', edgecolor='gray')
						)
			
			"""

		#plt.xlim(-40,160) #x軸範囲指定
		#plt.ylim(-10,185) #y軸範囲指定

		#plt.gcf().text(0.02, 0.5, "reach_n:"+str(reach_account), fontsize=10)
		self.ax3.text(-5, 0, "reach_n:"+str(reach_account), fontsize=10)
		self.ax3.text(-5, 3, "step_n:"+str(step), fontsize=10)
		self.ax3.text(-5, 6, "episode_n:"+str(episode), fontsize=10)

		

		self.draw_weighted_graph(self.G, self.pos)
		plt.grid() #グリッド
		#xtick=np.arange(-1,12, 1)
		#plt.xticks(xtick)
		plt.pause(delay)  #do not need 'plt.show()' to show
		plt.cla() #clear axis not plt

	def get_avail_action_fun(self, obs_i, current_start, current_goal, goal_i):
		#if s==self.pos[goal_i] and goal_i==0:
		if [obs_i[0],obs_i[1]]==self.pos[goal_i]:
			#return ['null']
			return [goal_i]

		action_set = []
		#print(s,pos.values())
		#print("[obs_i[0],obs_i[1]] pos.values()",[obs_i[0],obs_i[1]],self.pos.values())
		if str([obs_i[0],obs_i[1]]) in [str(ele) for ele in self.pos.values()]: #s=(0.0, 5.0)
			#print("it currently at node")
			node = [k for k, v in self.pos.items() if str(v) == str([obs_i[0],obs_i[1]])][0]  #node 0
			#print("current node",node)
			for edge in self.G.edges():
				if node in edge:
					if list(edge)[0] not in action_set and list(edge)[0]!=node:
						action_set.append(list(edge)[0])

					if list(edge)[1] not in action_set and list(edge)[1]!=node :
						#action_set.append(list(edge)[1])
						action_set.append(list(edge)[1])
			action_set.append(node)

		else:
			#print("it currently NOT at node")
			# action_set=[current_start ,current_goal]
			action_set = [current_goal]


		return action_set

	def collision_detect(self, obs_prepare):
		collision_flag = 0
		for i in range(self.agent_num-1):
			pos_i = [obs_prepare[i][0], obs_prepare[i][1]]
			#print("pos_i",i,pos_i)
			for j in range(i+1, self.agent_num):
				pos_j = [obs_prepare[j][0], obs_prepare[j][1]]
				#print("pos_j",j,pos_j)
				distance_ij = math.dist(pos_i, pos_j) 
				#print( "distance i j",distance_ij)

				if distance_ij<5:
					collision_flag = 1
					print('!!!collision!!! with agent',i,j)
		
		return collision_flag
"""
if __name__ == '__main__':
    Map=MapMake()
    csv_nodes_number,csv_nodes_pos,csv_edges,csv_edges_weights=Map.read_nodes_csv('node','edge')
    G, pos, edge_labels = Map.Graph_initial(csv_nodes_number,csv_nodes_pos,csv_edges,csv_edges_weights)
    
    Map.plot_map(pos) # a must be a angle !!!list!!!
"""

