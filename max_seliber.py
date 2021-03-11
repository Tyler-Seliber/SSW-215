def max_len_name(first, last):
    lenFirst = len(first)
    lenLast = len(last)
    return max(lenFirst, lenLast)

firstName = input("Please enter your first name: ")
lastName = input("Please enter your last name: ")
print("The largest value of the length of my firstname and lastname is", max_len_name(firstName,lastName))