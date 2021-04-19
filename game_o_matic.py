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

def printPlayerInventories(player_list):
    for p in player_list.keys():
        print(p, end=':\n')
        for i in player_list[p].items():
            print(f'\t{i[1]} {i[0]}')
        # print(p.values())
        # for i in p:
        #     print(i)

players = dict()
players['Gandolf'] = {'food': 5, 'grapefruit': 10, 'green potions': 7, 'red potions': 8, 'spells of enchantment': 10}
players['Frodo'] = {'food': 0, 'kiwi': 5, 'wands of confusion': 7, 'green potions': 8}
players['Sauron'] = {'bat wings': 5, 'evil spells': 10, 'fire wands': 5}

printPlayerInventories(players)
# print(players.items())

