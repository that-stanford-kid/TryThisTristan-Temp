"""
Patrick ONeil
Example for QLearning Agent implimentation to find optim with reward state via q-table
"""
import numpy as np
import sympy
import cmath
import matplotlib.pyplot as plt
import pandas as pd
import random

rewards_all_episodes = []
#for episode in range(num_episodes):
# initialize new episode parameters

#	for step in range(max_steps_per_episode):
		# exploration-exploitation trade-off
		# take new action
		# update q-table
		# set new state
		# add new reward

# exploration rate decay
	# add current episode reward to total reward list
#		for episode in range(num_episodes):
#			state = env.reset()
#			done != True
#			rewards_current_episode = 0

#	for step in range(max_steps_per_episode):
#		...
# for step in range(max_steps_per_episode):

#	exploration_rate_threshold = random.uniform(0, 1)
#	if exploration_rate_threshold > exploration_rate:
#		action = np.argmax(q_table[state,:])
#	else:
#		action = env.action_space.sample()
#	...
# new_state, reward, done, info = env.step(action)
# update q-table for q(s,a)
# q_table[state, action] = q_table[state, action] * (1 - learning_rate) + \
#	learning_rate * (reward + discount_rate * np.max(q_table[new_state, :]))
# state = new_state
# rewards_current_episode += reward
#if done == True:
#	break
# exploration rate decay 
#exploration_rate = min_exploration_rate + \
#	(max_exploration_rate - min_exploration_rate)

#rewards_all_episodes.append(rewards_current_episode)
# calculate and print the avg reward per thousands
#rewards_per_thousand_episodes = np.split(np.array(rewards_all_episodes), num_episodes)
count = 1000

print("*****Average reward per thousands episode*****\n")
#for r in rewards_per_thousand_episodes:
#	print(count, ": ", str(sum(r/1000)))
#	count += 1000
# print updated q_table
print("\n\n*****q_table*****\n")
#print(q_table)

"""
*****Q-table*****
[[0.57804676 0.51767675 0.50499139 0.47330103]
[0.07903519 0.16544989 0.16052137 0.45023559]
[0.37592905 0.18333739 0.18905787 0.17227745]
[0.01504804 0. 		   0. 		  0.		]
[0.59422496 0.42787803 0.43837162 0.45604075]
[0. 		0. 		   0. 		  0. 		]
[0.18140221 0.13794979 0.31651935 0.09308381]
[0. 		0. 		   0. 		  0. 		]
[0.43529839 0.32298132 0.36007182 0.64475741]
[0.33698531 0.75303211 0.42246585 0.50627733]
[0.65743421 0.48185693 0.32179817 0.35823251]
[0. 		0. 		   0. 		  0.		]
[0. 		0.	 	   0. 		  0. 		]
[0.53127669 0.63965638 0.86112718 0.53141807]
[0.68753949 0.94078659 0.76545158 0.71566071]
[0.			0.		   0.		  0.		]]
"""

# traversal functions in synthetic enviornment
environment_matrix = [[None, 0],
				[-100, 0],
				[0, 0],
				[0, 0],
				[0, 0],
				[0, 100],
				[0, 0],
				[100, 0],
				[0, 0],
				[0, None]]
q_matrix = [[0, 0],
		[0, 0],
		[0, 0],
		[0, 0],
		[0, 0],
		[0, 0],
		[0, 0],
		[0, 0],
		[0, 0],
		[0, 0]]
win_loss_states = [0,6]

def getAllPossibleNextAction(current_pos):
	step_matrix = [x != None for x in environment_matrix[current_pos]]
	action = []
	if(step_matrix[0]):
		action.append(0)
	if(step_matrix[1]):
		action.append(1)
	return(action)

def isGoalStateReached(current_pos):
	return (current_pos in [6])

def getNextState(current_pos, action):
	if (action == 0):
		return current_pos - 1
	else:
		return current_pos + 1

def isGameOver(current_pos):
	return current_pos in win_loss_states
	return True
	

discount = 0.9
learning_rate = 0.01921

for _ in range(1001):
	# get starting_pos or place
	current_pos = random.choice([0,1,2,3,4,5,6,7,8,9])
	# while goal state !== reached s
	while(not isGameOver(current_pos)):
		# get * proba future states from current_step
		possible_actions = getAllPossibleNextAction(current_pos)
		# select any one act randomly
		action = random.choice(possible_actions)
		# find the best next state corresponding to action select
		next_state = getNextState(current_pos, action)
		# update q_matrix
		q_matrix[current_pos][action] = q_matrix[current_pos][action] + learning_rate * (environment_matrix[current_pos][action] + discount * max(q_matrix[next_state]) - q_matrix[current_pos][action])
		# move or get next best state
		current_pos = next_state
	# print status

	print("Image = Sectors, Categories, Match", _ , " win_loss_states," ' ''Retail' " exploration_rate_threshold\n")

print('GoalStateReached')
print(q_matrix)
print("...Training is done...")
print(current_pos)

print("...Patricks AI...")
