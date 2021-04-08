def word_order(str):
    sequence = str.split(', ')
    # From https://www.w3schools.com/python/ref_list_sort.asp
    sequence.sort()
    unique_sequence = []
    for i in sequence:
        if i not in unique_sequence:
            unique_sequence.append(i)
    return unique_sequence

str = 'apple, mango, carrot, apple, orange, mango, berry'
print(*word_order(str), sep = ', ')