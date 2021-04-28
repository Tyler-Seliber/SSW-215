def print_inventory(inventory):
    print('Store name: ' + inventory.get('name'))
    print('Store address: ' + inventory.get('address'))
    print('Stock:')
    stock = inventory.get('stock')
    for i in stock:
        print(f"\t{i.get('author')}: \"{i.get('title')}\" (${i.get('price')})")

inventory = {
    'name': 'Barnes & Noble Booksellers',
    'address': '395 Route 3 East Clifton, NJ 07014',
    'stock': [
        { 'title': 'Sooley', 'author': 'John Grisham', 'price': 28.95 },
        { 'title': 'American Marxism', 'author': 'Mark R. Levin', 'price': 28.00 },
        { 'title': 'World Travel: An Irreverant Guide', 'author': 'Anthony Bourdain, Laurie Woolever', 'price': 35.00 },
        { 'title': 'The Bomber Mafia: A Dream, a Temptation, and the Longest Night of the Second World War', 'author': 'Malcolm Gladwell', 'price': 27.00 },
        { 'title': 'S.', 'author': 'J. J. Abrams, Doug Dorst', 'price': 45.00 }
    ]
}

print_inventory(inventory)