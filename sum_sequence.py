# Part 2

# This was a challenging assignment.
# I have very little experience with recursion and had a much harder time than expected trying to think through the logic.
# My friend David Treder had attempted to give me a good starting basis, but I still wasn't able to figure it out.

# I had found a solution to this problem online, and even looking through that it is difficult for me to comprehend what is actually going on.
# The code below is heavily based on the online solution I had found.
# I slightly refactored the code to be neater and more efficient (in my opinion).
# The original code can be found at https://www.geeksforgeeks.org/print-all-non-increasing-sequences-of-sum-equal-to-a-given-number/

# Print array arr[0..n-1]
def printArr(arr, n):
    print(*arr[:n])

# Recursive Function to generate all non-increasing sequences with sum sum arr[] --> Elements of current sequence intermediate_sum --> Current Sum index --> Current index in arr[]
def sum_sequence(sum, arr = None, intermediate_sum = 0, index = 0):

    # arr used to store the intermediate values
    if arr is None:
        arr = [0] * sum
        
    # If current sum is equal to sum, then we found a sequence
    if (intermediate_sum == sum):  
        printArr(arr, index)
        return

	# Try placing all numbers from 1 to sum - intermediate_sum at current index
    num = 1
	
	# The placed number must also be smaller than previously placed numbers and it may be equal to the previous stored value, i.e., arr[index-1] if there exists a pevious number
    while (num <= sum - intermediate_sum and (index == 0 or num <= arr[index - 1])):

		# Place number at index
        arr[index] = num
        sum_sequence(sum, arr, intermediate_sum + num, index + 1)
	
		# Try next number
        num += 1

k = 4
sum_sequence(k)