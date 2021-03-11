def prod_len_name(first, last):
    lenFirst = len(first)
    lenLast = len(last)
    return lenFirst * lenLast

firstName = input("Please enter your first name: ")
lastName = input("Please enter your last name: ")
print("The product of the value of the lengths of my firstname and lastname is ", prod_len_name(firstName,lastName))