## Do not change!!!!!

'''
Problem information 
map_name            |number of drone| number of problem
--------------------|---------------|-------------------
map_3x3             |  2            | 3
map_3x3             |  3            | 4
map_3x3             |  4            | 3
map_aoba01          |  4            | 3
map_aoba01          |  6            | 4
map_aoba01          |  8            | 3
map_shibuya         |  8            | 3
map_shibuya         |  10           | 4
map_shibuya         |  12           | 3
'''

instances = [
    { 
        "id": 1,
        "map": "map_3x3",
        "drone_num": 2,
        "start": [0,2],
        "goal": [5,6]
    },
    {
        "id": 2,
        "map": "map_3x3",
        "drone_num": 2,
        "start": [2,7],
        "goal": [0,4]
    },
    {
        "id": 3,
        "map": "map_3x3",
        "drone_num": 2,
        "start": [1,7],
        "goal": [3,6]
    },
    {
        "id": 4,
        "map": "map_3x3",
        "drone_num": 3,
        "start": [4,2,3],
        "goal": [7,6,1]
    },
    {
        "id": 5,
        "map": "map_3x3",
        "drone_num": 3,
        "start": [6,3,5],
        "goal": [2,1,8]
    },
    {
        "id": 6,
        "map": "map_3x3",
        "drone_num": 3,
        "start": [7, 1, 8],
        "goal": [6, 0, 5]
    },
    {
        "id": 7,
        "map": "map_3x3",
        "drone_num": 3,
        "start": [1, 3, 0],
        "goal": [4, 7, 6]
    },
    {
        "id": 8,
        "map": "map_3x3",
        "drone_num": 4,
        "start": [3,2,1,8],
        "goal": [0,7,6,4]
    },
    {
        "id": 9,
        "map": "map_3x3",
        "drone_num": 4,
        "start": [5,0,2,1],
        "goal": [8,3,6,7]
    },
    {
        "id": 10,
        "map": "map_3x3",
        "drone_num": 4,
        "start": [3, 8, 2, 7],
        "goal": [6, 4, 0, 5]
    },
    {
        "id": 11,
        "map": "map_aoba01",
        "drone_num": 4,
        "start": [12, 10, 0, 15],
        "goal": [11, 14, 3, 9]
    },
    {
        "id": 12,
        "map": "map_aoba01",
        "drone_num": 4,
        "start": [11, 9, 2, 7],
        "goal": [8, 12, 15, 10]
    },
    {
        "id": 13,
        "map": "map_aoba01",
        "drone_num": 4,
        "start": [6, 8, 12, 16],
        "goal": [ 14, 3, 5, 0]
    },
    {
        "id": 14,
        "map": "map_aoba01",
        "drone_num": 6,
        "start": [16, 10, 1, 2, 5, 8],
        "goal": [ 7, 3, 0, 14, 15, 9]
    },
    {
        "id": 15,
        "map": "map_aoba01",
        "drone_num": 6,
        "start": [1, 2, 0, 4, 16, 12],
        "goal": [10, 13, 17, 14, 7, 5]
    },
    {
        "id": 16,
        "map": "map_aoba01",
        "drone_num": 6,
        "start": [14, 4, 11, 7, 13, 16],
        "goal": [ 12, 5, 0, 2, 1, 10]
    },
    {
        "id": 17,
        "map": "map_aoba01",
        "drone_num": 6,
        "start": [9, 12, 10, 2, 8, 15],
        "goal": [ 7, 3, 14, 16, 13, 1]
    },
    {
        "id": 18,
        "map": "map_aoba01",
        "drone_num": 8,
        "start": [7, 6, 10, 13, 2, 0, 17, 3],
        "goal": [16, 11, 4, 14, 15, 9, 12, 8]
    },
    {
        "id": 19,
        "map": "map_aoba01",
        "drone_num": 8,
        "start": [2, 15, 3, 17, 14, 13, 8, 10],
        "goal": [ 16, 12, 9, 6, 5, 11, 7, 0]
    },
    {
        "id": 20,
        "map": "map_aoba01",
        "drone_num": 8,
        "start": [11, 0, 15, 1, 3, 17, 4, 2],
        "goal": [ 10, 16, 7, 12, 14, 6, 13, 5]
    },
    {
        "id": 21,
        "map": "map_shibuya",
        "drone_num": 8,
        "start": [5, 18, 6, 12, 27, 17, 3, 9],
        "goal": [14, 21, 8, 26, 13, 25, 22, 23]
    },
    {
        "id": 22,
        "map": "map_shibuya",
        "drone_num": 8,
        "start": [20, 13, 15, 17, 12, 3, 24, 19],
        "goal":  [7, 2, 21, 4, 23, 27, 16, 14]
    },
    {
        "id": 23,
        "map": "map_shibuya",
        "drone_num": 8,
        "start":  [14, 25, 16, 1, 23, 2, 0, 6],
        "goal":  [17, 12, 22, 26, 9, 13, 5, 7]
    },
    {
        "id": 24,
        "map": "map_shibuya",
        "drone_num": 10,
        "start":[26, 9, 23, 12, 22, 2, 11, 0, 10, 27],
        "goal": [1, 24, 8, 18, 19, 5, 25, 4, 17, 3]
    },
    {
        "id": 25,
        "map": "map_shibuya",
        "drone_num": 10,
        "start":  [16, 4, 5, 18, 7, 11, 9, 14, 21, 3],
        "goal":  [23, 1, 25, 13, 19, 26, 22, 20, 12, 24]
    },
    {
        "id": 26,
        "map": "map_shibuya",
        "drone_num": 10,
        "start":   [25, 1, 13, 18, 24, 16, 7, 10, 2, 6],
        "goal":  [17, 23, 21, 3, 5, 8, 11, 12, 20, 26]
    },
    {
        "id": 27,
        "map": "map_shibuya",
        "drone_num": 10,
        "start":  [3, 15, 18, 5, 19, 6, 25, 13, 11, 23],
        "goal": [20, 9, 21, 22, 16, 17, 2, 4, 14, 7]
    },
    {
        "id": 28,
        "map": "map_shibuya",
        "drone_num": 12,
        "start":[13, 3, 17, 23, 4, 22, 12, 10, 19, 8, 16, 0],
        "goal":  [26, 7, 14, 18, 15, 2, 25, 11, 21, 9, 27, 6]
    },
    {
        "id": 29,
        "map": "map_shibuya",
        "drone_num": 12,
        "start":[18, 21, 27, 11, 23, 22, 17, 13, 24, 9, 2, 5],
        "goal": [4, 10, 0, 6, 26, 15, 7, 19, 12, 8, 14, 1]
    },
    {
        "id": 30,
        "map": "map_shibuya",
        "drone_num": 12,
        "start":[20, 12, 9, 11, 18, 7, 13, 2, 3, 21, 16, 6],
        "goal":  [5, 15, 27, 19, 23, 22, 10, 24, 4, 25, 0, 17]
    },
]
