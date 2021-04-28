def square_array(arr):
    arr_sq = []
    for i in arr:
        arr_sq.append(i ** 2)
    return arr_sq

arr = [1,2,3,4,5,6,7,8,9,10]
print(f'Array = {arr}')
arr_sq = square_array(arr)
print(f'Array Squared = {arr_sq}')