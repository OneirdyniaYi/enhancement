# author='lwz'
# coding:utf-8
# !/usr/bin/env python3
# http://mnemstudio.org/path-finding-q-learning-tutorial.htm
# http://blog.csdn.net/maggie_zhangxin/article/details/73481417
# 强化学习案例2 网格移动
import numpy as np
from numpy import inf


link = []
# 奖励表  行代表行动前的位置  列代表行动（即到达哪一个房间）
# 不能可能到达的区域设置为-inf
#     上  下  左  右
R = [[10, 10, 10, 10],
     [-1,  0,  0,  0],
     [-1,  0,  0,  0],
     [ 0,  0, -1,  0],
     [ 0,  0,  0,  0],
     [ 0,  0,  0, -1],
     [ 0, -1, -1,  0],
     [ 0, -1,  0,  0],
     [ 0, -1,  0, -1]
     ]
R = np.array(R)

#      上  下 左 右
Link = [[9, 9, 9, 9],
        [2, 5, 1, 3],
        [3, 6, 2, 3],
        [1, 7, 4, 5],
        [2, 8, 4, 6],
        [3, 9, 5, 6],
        [4, 7, 7, 8],
        [5, 8, 7, 9],
        [6, 9, 8, 9]
        ]
Link = np.array(Link) - 1

T = np.ones(R.shape) * (1.0 / R.shape[1])  # 转移概率 初始状态 四个方向转移概率一样

# 矩阵Q的行代表智能体当前的状态，列代表到达下一个状态的可能的动作。
# 因为智能体在最初对环境一无所知，因此矩阵Q被初始化为0。在这个例子中，为了阐述方便，
# 我们假设状态的数量是已知的（设为6）。如果我们不知道有多少状态时，矩阵Q在最初被设为只有一个元素。
# 如果新的状态一旦被发现，对矩阵Q增加新的行和新的列非常简单。
# Q-学习的转换规则非常简单，为下面的式子：
# Q(state, action)=R(state, action) + Gamma * Max(Q[next state, all actions])

gamma = 0.90            # learning parameter
alpha = 0.1
q = np.zeros(R.shape)      # initialize Q as zero,q的行数和列数等于矩阵R的。
q1 = np.ones(R.shape) * inf  # initialize previous Q as big number

count = 0              # counter
position = np.array(range(R.shape[0]))
state_n = R.shape[0]   # 状态数量
action_n = R.shape[1]  # 动作数量

'''
利用矩阵Q的算法如下：
1、设置当前状态=初始状态；
2、从当前状态开始，寻找具有最高Q值的动作；
3、设置当前状态=下一个状态；
4、重复步骤2和3，直到当前状态=目标状态。
'''
iter = 0

while iter < 500000:
    iter += 1
    state = np.random.randint(0, state_n)           # 取1到9的随机数的第一个数
    action = np.random.randint(0, action_n)
    next_state = Link[state, action]
    next_action = np.argmax(q[next_state, :])
    delta = gamma * q[next_state, next_action] - q[state, action] + R[state, action]
    q[state, action] += alpha * delta

    if np.sum(abs(q1-q)) < 0.000001 and np.sum(q) > 0:
        if count > 50000:
            print(iter, count)
            break          # for
        else:
             count += 1  # set counter if deviation of q is small

        print(np.round(q, 2))
    else:
        q1 = q
        count = 0


print('迭代次数：{}'.format({iter}))
print(np.round(T, 2))
print(np.round(q1, 2))



