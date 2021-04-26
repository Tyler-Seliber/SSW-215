# Part 1

def sum_trio(numSet, sum, list = []):
    # trio = []
    # intermediate_sum = 0
    if len(list) == 3:
        return list
    x = numSet[1]
    list.append(x)
    if sum - x == numSet[1]:
        list.append(sum_trio(numSet[1:], numSet[1], list))
    else:
        return list
        

numSet = [3, 7, 4, 0, 9, 5, 1, 2]
sum = 7
print(sum_trio(numSet, sum))