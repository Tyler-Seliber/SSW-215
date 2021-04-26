# Part 1

def sum_trio(numSet, sum, list = []):
    # print(list)
    if len(list) == 3 and sum == 0: #Trio found
        return [list]
    
    if not numSet or len(list) == 3: #Haven't found trio or 3 numbers aren't a trio, return nothing (start over)
        return []

    return sum_trio(numSet[1:], sum - numSet[0], [numSet[0]]+list) + sum_trio(numSet[1:], sum, list)


numSet = [3, 7, 4, 0, 9, 5, 1, 2]
sum = 7

print(sorted(list(map(sorted, sum_trio(numSet, sum)))))