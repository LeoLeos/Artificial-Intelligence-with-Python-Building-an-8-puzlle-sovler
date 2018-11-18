'''
@Author: Leo
@Student number: 201641512142
@University: DongGuan University of Technology
@data: 2018.11.18
'''

from simpleai.search import astar, SearchProblem
import time

#记录开始运行时间点
start_time = time.process_time()

#继承SearchProblem类
class PuzzleSolver(SearchProblem):
    #定义动作
    def actions(self, state):
        rows = string_to_list(state)
        row_empty, col_empty = get_location(rows, '0')

        actions = []
        if row_empty > 0:
            actions.append(rows[row_empty - 1][col_empty])
        # 4x4维数字华容道，如要改变维度需要更改为 n-1
        if row_empty < 2:
            actions.append(rows[row_empty + 1][col_empty])
        if col_empty > 0:
            actions.append(rows[row_empty][col_empty - 1])
        # 4x4维数字华容道，如要改变维度需要更改为 n-1
        if col_empty < 2:
            actions.append(rows[row_empty][col_empty + 1])
        return actions

    def result(self, state, action):
        rows = string_to_list(state)
        row_empty, col_empty = get_location(rows, '0')
        row_new, col_new = get_location(rows, action)

        rows[row_empty][col_empty], rows[row_new][col_new] = rows[row_new][col_new], rows[row_empty][col_empty]
        return list_to_string(rows)

    def is_goal(self, state):
        return state ==GOAL

    #定义启发式函数
    def heuristic(self, state):
        rows = string_to_list(state)
        distance = 0
        for number in '123456780':
            row_new, col_new = get_location(rows, number)
            row_new_goal, col_new_goal = goal_positions[number]
            distance += abs(row_new - row_new_goal) + abs(col_new - col_new_goal)
        return distance

def list_to_string(input_list):
    return '\n'.join(['-'.join(x) for x in input_list])

def string_to_list(input_string):
    return [x.split('-') for x in input_string.split('\n')]

def get_location(rows, input_element):
    for i, row in enumerate(rows):
        for j, item in enumerate(row):
            if item == input_element:
                return i, j

#目标空间状态，每个元素只能一个符号代替,0表示空模块
GOAL = '''1-2-3
4-5-6
7-8-0'''

#初始空间状态，每个元素只能一个符号代替
INITIAL = '''1-2-4
7-8-6
5-3-0'''

#记录步数
count = 0
goal_positions = {}
rows_goal = string_to_list(GOAL)
#遍历每个元素，3x3维数字华容道，如要改变维度需要更改字符串
for number in '123456780':
    goal_positions[number] = get_location(rows_goal, number)
result = astar(PuzzleSolver(INITIAL))

for i, (action, state) in enumerate(result.path()):
    print()
    print('第', count, '步')
    count += 1
    if action == None:
        print('Initial configuration')
    elif i == len(result.path()) - 1:
        print('After moving', action, 'into the empty space. Goal achieved!')
    else:
        print('After moving', action, 'into the empty space')
    print(state)
end_time = time.process_time()

print()
print('运行时间', end_time - start_time, 's')

