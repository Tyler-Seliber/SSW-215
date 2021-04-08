def even_ind(str):
    odds = ''
    # Start at first odd index, skips every successive even index
    for i in range(1,len(str),2):
        odds += str[i]
    return odds

str = "Individual software engineering"
print(even_ind(str))