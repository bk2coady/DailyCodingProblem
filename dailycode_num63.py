Status = "Finished"
#Daily Coding Challenge #63

'''
Given a 2D matrix of characters and a target word, write a function that 
returns whether the word can be found in the matrix by going left-to-right, 
or up-to-down.

For example, given the following matrix:

[['F', 'A', 'C', 'I'],
 ['O', 'B', 'Q', 'P'],
 ['A', 'N', 'O', 'B'],
 ['M', 'A', 'S', 'S']]
and the target word 'FOAM', you should return true, since it's the leftmost 
column. Similarly, given the target word 'MASS', you should return true, since 
it's the last row.
'''
def WordSearch(arr, word):
	for row in range(len(arr)):
		for col in range(len(arr[0])):
			if WordFind(arr, col, row, word):
				print("Found", word, "with first letter in row", row+1, "and column", col+1)
				return True
	print("Word not found.")
	return False


#Note: this only cycles from the initial starting point through all the directions
#If it finds the word, it returns True
#Does not cycle through every possible solution, so we create WordSearch above

def WordFind(arr, col, row, word):
	#Step 1: Set the cancel condition
	if arr[row][col] != word[0]:
		return False 
	#Step 2: What are you iterating through?
	#In this case, step through each advancement according to the x and y directions
	#Adding an x and y array allows you to add or take away direction vectors
	#this will loop through each possible direction based on the starting point (row, col)
	for i in range(len(x)):
		#rd is the starting row to be searched through
		#rd will be iterated through in the function without affecting row
		#row gets passed to the function from outside
		rd = row + x[i]
		#cd is th starting column to be searched through
		#same as rd above
		cd = col + y[i]
		#set a for loop to search for each letter of the word in the grid
		for k in range(1, len(word)):
			#if you go outside the boundaries, quit looking (it's not there)
			#these breaks are the critical insight - no sense looking where the word is not
			if (rd >= len(arr) or rd < 0 or cd >= len(arr[0]) or cd < 0):
				break
			#if the word no longer matches the characters in the grid, quit looking
			if arr[rd][cd] != word[k]:
				break
			#if you pass the line above, you must have found the next letter
			#increase where you are looking according to next direction vector
			#ie if looking down a column x[0], y[0] = (0,1)
			#then rd and cd increment accordingly and the loop repeats
			#if the next letter is not found, 
			#the cycle breaks and increments to next direction
			rd += x[i]
			cd += y[i]
			#if you make it to the end of the cycle, you must have found all the letters!
			#len(word) must be -1 because k starts at 0
			#if the number of cycles (k) = len(word) -1, you must have found all letters
			#then it should return True 
			if k == len(word)-1:
				return True 
	#if you cycle through EVERYTHING and do not find the word, 
	#it does not exist in the grid starting from row, col
	#then return False
	return False 


def MasterWordSearch(arr, word):
	for row in range(len(arr)):
		for col in range(len(arr[0])):
			if arr[row][col] == word[0]:
				if len(word) == 1:
					print("Found", word, "with first letter in row", row+1, "and column", col+1) 
					return True 
				for i in range(len(x)):
					rd = row + x[i]
					cd = col + y[i]
					for k in range(1, len(word)):
						if (rd >= len(arr) or rd < 0 or cd >= len(arr[0]) or cd < 0):
							break
						if arr[rd][cd] != word[k]:
							break
						rd += x[i]
						cd += y[i]
						if k == len(word)-1:
							print("Found word", word, " in row", row+1, "and column", col+1) 
							return True 






x = [-1, 0, 1, 0]
y = [0, -1, 0, 1]


arr = [['F', 'A', 'C', 'I'],
 ['O', 'B', 'Q', 'P'],
 ['A', 'N', 'O', 'B'],
 ['M', 'A', 'S', 'S'],
 ['T', 'E', 'S', 'T']]

word1 = "FOAM"
word2 = "MASS"
word3 = "TEST"

WordSearch(arr, "BONA")
MasterWordSearch(arr, "A")
