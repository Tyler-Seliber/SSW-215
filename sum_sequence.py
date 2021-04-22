# Part 2

def sum_sequence(sum, start = 1):
    
    arr = [1] * sum
    if arr[0] != sum:
        print(arr)
        return sum_sequence(sum - 1) + ' '
    else:
        return '\n'
    print(arr)

    # if sum != 1:
    #     return str(start) + ' ' + str(sum_sequence(sum - 1))
    # elif start != sum:
    #     return '\n' + sum_sequence(sum, start + 1)
    # else:
    #     return ''
    

k = 4
print(sum_sequence(k))