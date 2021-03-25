def char_index(str):
  index_list = []
  index = 0
  search_char = 'r'
  
  for ch in str:
    
    if ch == search_char:
      index_list.append(index)
    
    index += 1
  
  return index_list

fruits = 'Mango banana apple pear Banana grapes strawberry Apple pear mango banana Kiwi apple mango strawberry'
index_list = char_index(fruits)

print('The index values of each occurrences of \'r\' in the string are', end=' ') ## print without new line
print(*index_list, sep = ', ')