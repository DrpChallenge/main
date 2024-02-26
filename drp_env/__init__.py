# register
from gym.envs.registration import register
from itertools import product

agent_num = range(1,30)
speed = 5
start_ori_array = []
goal_array = []
visu_delay = 0.3
reward_list = {"goal": 100, "collision": -10, "wait": -10, "move": -1}

time_limit = 100
collision = "terminated"

map_list = [
    "map_3x3",
    "map_5x4",
    "map_8x5",
    "map_10x6",
    "map_10x8",
    "map_10x10",
    "map_aoba00",
    "map_aoba01",
    "map_kyodai",
    "map_osaka",
    "map_paris",
    "map_shibuya",
    "map_shijo",
]

for an, map_name in product(agent_num, map_list):
    register(
        id="drp-{0}agent_{1}-v2".format(an, map_name),
        #entry_point="gym_vrp.envs:VrpEnv",
        entry_point="drp_env.drp_env:DrpEnv",
        kwargs={
            "agent_num": an,
            "speed": speed,
            "start_ori_array": start_ori_array,
            "goal_array": goal_array,
            "visu_delay": visu_delay,
            "time_limit": time_limit,
            "collision": collision,
            "map_name": map_name,
            "reward_list": reward_list,
        },
    )

neargridmap_list = [
    "map_3x3",
    "map_5x4",
    "map_8x5",
    "map_10x6",
    "map_10x8",
    "map_10x10",
]

state_value = {
    "goal": 10,
    "neighbor": 0.1,
    "around": 0.1,
}

for an, map_name in product(agent_num, map_list):
    register(
        id="drpDT-{0}agent_{1}-v2".format(an, map_name),
        #entry_point="gym_vrp.envs:VrpEnv",
        entry_point="drp_env.DTenv.v2_goalcenter.env_wrapper:DtEnv",
        kwargs={
            "agent_num": an,
            "speed": speed,
            "start_ori_array": start_ori_array,
            "goal_array": goal_array,
            "visu_delay": visu_delay,
            "time_limit": time_limit,
            "collision": collision,
            "map_name": map_name,
            "reward_list": reward_list,
            "state_repre_flag": "DT",
            "state_value": state_value,
        },
    )

for an, map_name in product(agent_num, map_list):
    register(
        id="drpDT-{0}agent_{1}-v1".format(an, map_name),
        #entry_point="gym_vrp.envs:VrpEnv",
        entry_point="drp_env.DTenv.v1_startcenter.env_wrapper:DtEnv",
        kwargs={
            "agent_num": an,
            "speed": speed,
            "start_ori_array": start_ori_array,
            "goal_array": goal_array,
            "visu_delay": visu_delay,
            "time_limit": time_limit,
            "collision": collision,
            "map_name": map_name,
            "reward_list": reward_list,
            "state_repre_flag": "DT",
            "state_value": state_value,
        },
    )



agent_num = 2
speed = 5
start_ori_array = []
goal_array = []
visu_delay = 0.3
reward_list = {"goal": 100, "collision": -10, "wait": -10, "move": -1}

time_limit = 100
collision = "terminated"

map_list = [
    "map_3x3",
    "map_5x4",
    "map_8x5",
    "map_10x6",
    "map_10x8",
    "map_10x10",
    "map_aoba00",
    "map_aoba01",
    "map_kyodai",
    "map_osaka",
    "map_paris",
    "map_shibuya",
    "map_shijo",
]

for map_name in map_list:
    register(
        id="drpOA-{0}agent_{1}-v1".format(agent_num, map_name),
        #entry_point="gym_vrp.envs:VrpEnv",
        entry_point="drp_env.OneAgentEnv.env_wrapper:OAEnv",
        kwargs={
            "agent_num": agent_num,
            "speed": speed,
            "start_ori_array": start_ori_array,
            "goal_array": goal_array,
            "visu_delay": visu_delay,
            "time_limit": time_limit,
            "collision": collision,
            "map_name": map_name,
            "reward_list": reward_list,
        },
    )