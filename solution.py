# From https://www.geeksforgeeks.org/print-all-non-increasing-sequences-of-sum-equal-to-a-given-number/

# Python3 program to generate all non-increasing sequences of sum equals to x

# Utility function to print array arr[0..n-1]
def printArr(arr, n):

	for i in range(0, n):
		print(arr[i], end = " ")
		
	print("")


# Recursive Function to generate all non-increasing sequences with sum x arr[] --> Elements of current sequence curr_sum --> Current Sum curr_idx --> Current index in arr[]
def generateUtil(x, arr, curr_sum, curr_idx):

# If current sum is equal to x, then we found a sequence
	if (curr_sum == x):

		printArr(arr, curr_idx)
		return


	# Try placing all numbers from 1 to x-curr_sum at current index
	num = 1
	
	# The placed number must also be smaller than previously placed numbers and it may be equal to the previous stored value, i.e., arr[curr_idx-1] if there exists a pevious number
	while (num <= x - curr_sum and (curr_idx == 0 or num <= arr[curr_idx - 1])):

		# Place number at curr_idx
		arr[curr_idx] = num
	
		# Recur
		generateUtil(x, arr, curr_sum + num, curr_idx + 1)
	
		# Try next number
		num += 1



# A wrapper over generateUtil()
def generate(x):

	# Array to store sequences on by one
	arr = [0] * x
	generateUtil(x, arr, 0, 0)


# Driver program
x = 4
generate(x)

# This code is contributed by Smitha.