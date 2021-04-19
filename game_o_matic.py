import random

# Part 1

# rand_numbers = []
# dodecahedron_results = [0] * 12

# for i in range(0,10000):
#     r = random.randint(1,12)
#     rand_numbers.append(r)
#     dodecahedron_results[r-1] += 1

# print(dodecahedron_results)

# Part 2

def addPlayer(player_list, name, inventory):
    player_list[name] = inventory
    print(f'Welcome, {name}.')

def removePlayer(player_list, name):
    player_list.pop(name)
    print(f'So long, {name}.')

def printPlayerInventories(player_list):
    print('Current player inventories:')
    for p in player_list.keys():
        print('\t' + p + ':')
        for i in player_list[p].items():
            print(f'\t\t{i[1]} {i[0]}')

def addToInventory(player_list, player, item, amount):
    # Adds amount to item in player's inventory. If item does not exist, add it to player's inventory and set the quantity to amount.
    player_list[player][item] = player_list[player].setdefault(item, 0) + amount
    print(f'{player} has received {amount} {item}.')

def removeFromInventory(player_list, player, item, amount):
    # Prevent having negative amount of items, or quickly remove all items
    if ((player_list[player][item] - amount) < 0) or (amount == -1):
        amount = player_list[player][item]
        # Removes the item from the inventory if the amount is zero
        player_list[player].pop(item)
    else:
        player_list[player][item] -= amount
    print(f'{player} has lost {amount} {item}.')

players = dict()

addPlayer(players, 'Gandolf', {'food': 5, 'grapefruit': 10, 'green potions': 7, 'red potions': 8, 'spells of enchantment': 10})
addPlayer(players, 'Frodo', {'food': 0, 'kiwi': 5, 'wands of confusion': 7, 'green potions': 8})
addPlayer(players, 'Sauron', {'bat wings': 5, 'evil spells': 10, 'fire wands': 5})

printPlayerInventories(players)

# Test the three capabilities required by the assignment
addToInventory(players, 'Gandolf', 'food', 18)
removeFromInventory(players, 'Gandolf', 'green potions', -1)
addToInventory(players, 'Sauron', 'spider eyes', 4)
removeFromInventory(players, 'Sauron', 'bat wings', 3)
removePlayer(players, 'Frodo')
addPlayer(players, 'Windelschleppitis', players['Gandolf'].copy())

printPlayerInventories(players)