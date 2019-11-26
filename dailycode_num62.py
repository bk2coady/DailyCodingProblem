#Daily Coding Problem #62

'''
Initial instructions:

There is an N by M matrix of zeroes. Given N and M, write a function to count the number of ways of starting at the top-left corner and getting to the bottom-right corner. You can only move right or down.

For example, given a 2 by 2 matrix, you should return 2, since there are two ways to get to the bottom-right:

Right, then down
Down, then right
Given a 5 by 5 matrix, there are 70 ways to get to the bottom-right.
'''

def N_M_recursion(N,M):
	if N <= 0 or M <= 0:
		return 0

	if N == 1 or M == 1:
		return 1

	return N_M_recursion(N-1,M) + N_M_recursion(N,M-1)

def N_M_master(N,M):
	size = 20
	arr = [[0 for i in range(size)] for j in range(size)]
	for i in range(size):
		for j in range(size):
			if i <= 0 and j <= 0:
				arr[i][j] = 0
			elif i == 0 or j == 0:
				arr[i][j] = 1
			else:
				arr[i][j] = arr[i-1][j] + arr[i][j-1]
	if N <= 0 or M <= 0:
		return 0
	return arr[N-1][M-1]

def N_M_P_recursion(N,M,P):
	if N <= 0 or M <= 0 or P <= 0:
		return 0

	if N == 1:
		return N_M_recursion(M,P)
	if M == 1:
		return N_M_recursion(N,P)
	if P == 1:
		return N_M_recursion(N,M)

	return N_M_P_recursion(N-1,M, P) + N_M_P_recursion(N,M-1, P) + N_M_P_recursion(N,M,P-1)

def N_M_P_master(N,M,P):
	size = 20
	arr = [[[0 for i in range(size)] for j in range(size)] for k in range(size)]
	for i in range(size):
		for j in range(size):
			for k in range(size):
				if i <= 0 and j <= 0 and k <= 0 :
					arr[i][j][k] = 0
				elif (i == 0 and j == 0) or (i == 0 and k == 0) or (j == 0 and k == 0):
					arr[i][j][k] = 1
				elif i == 0:
					arr[i][j][k] = arr[i][j-1][k] + arr[i][j][k-1]
				elif j == 0:
					arr[i][j][k] = arr[i-1][j][k] + arr[i][j][k-1]
				elif k == 0:
					arr[i][j][k] = arr[i-1][j][k] + arr[i][j-1][k]
				else:
					arr[i][j][k] = arr[i-1][j][k] + arr[i][j-1][k] + arr[i][j][k-1]
	if N <= 0 or M <= 0:
		return 0
	return arr[N-1][M-1][P-1]

print(N_M_recursion(11,12))
print(N_M_master(20,20))
print(N_M_P_recursion(5,2,2))
print(N_M_P_master(5,2,2))

