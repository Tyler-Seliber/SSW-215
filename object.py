from datetime import date
class Computer:
    # Create Computer object from given specs
    def __init__(self, make, model, size, year, processor, graphics, memory, storage):
        self.make = make
        self.model = model
        self.size = size
        self.year = year
        self.processor = processor
        self.graphics = graphics
        self.memory = memory
        self.storage = storage

    # Calculate computer's age
    def computer_age(self):
        current_year = date.today().year
        print(f'Your {self.year} {self.make} {self.model} is {current_year - self.year} year(s) old.') 
    
    # Format the object to neatly print it's information and stricts
    def __str__(self):
        return (f'Specs for your {self.year} {self.make} {self.model} {self.size}: \n\tProcessor: {self.processor})\n\tGraphics: {self.graphics}\n\tMemory: {self.memory}\n\tStorage: {self.storage}')

macbook = Computer('Apple', 'MacBook Pro', '16-inch', 2019, 'Intel Core i9', 'AMD Radeon Pro 5500M / Intel UHD Graphics 630', '32 GB', '2 TB')
print(macbook)
macbook.computer_age()