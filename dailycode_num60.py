Status = "Finished"
#Daily Coding Challenge #60

'''
Given a multiset of integers, return whether it can be partitioned into two 
subsets whose sums are the same.

For example, given the multiset {15, 5, 20, 10, 35, 15, 10}, it would return 
true, since we can split it up into {15, 5, 10, 15, 10} and {20, 35}, which 
both add up to 55.

Given the multiset {15, 5, 20, 10, 35}, it would return false, 
since we can't split it up into two subsets that add up to the same sum.
'''

def betterSubsetSum(superset, goal):
    if goal == 0:
        return True 
    if (len(superset) == 0 and sum != 0):
        return False 
    if (superset[-1] > goal):
        return betterSubsetSum(superset[:-1], goal)
    if betterSubsetSum(superset[:-1], goal):
        return True
    if betterSubsetSum(superset[:-1], goal - superset[-1]):
        goal_set.append(superset[-1])
        return True

def partition(arr):
	if sum(arr) % 2 != 0:
		print("Array cannot be split.")
		return False 

	goal = sum(arr)/2
	remainder = arr

	if betterSubsetSum(arr, goal):
		print("Set 1:", goal_set)
		for i in range(len(goal_set)):
			remainder.remove(goal_set[i])
		print("Set 2:", remainder)
		return True 

	else: 
		print("No solution found.")
		return False 



goal_set = []
arr = [15, 5, 20, 10, 15, 10, 5]

partition(arr)
