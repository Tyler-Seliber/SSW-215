# Part 2

def sum_sequence(sum, start = 1):
    
    arr = [1] * sum
    if arr[0] != sum:
        print(arr)
        return (str(arr[0]+arr[1]) + ' '+ sum_sequence(sum - 1) + ' ')
    else:
        return '\n'  

k = 4
print(sum_sequence(k))