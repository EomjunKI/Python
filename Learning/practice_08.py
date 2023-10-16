# 08.01 Class

class Profile:
    def __init__(self, name, title):    # method
        self.name = name    # attribute
        self.title = title
        print(f'This singer is {self.name}.')
        print(f'This singer sing {self.title}')

singer_1 = Profile('Elijah Woods', '24/7, 365') # instance
singer_2 = Profile('Tape Machines', '3D Print')

# 08.02 Inheritance

class Detailed_profile(Profile):    # sub class (super class_1, super class_2)
    def __init__(self, name, title, age):
        Profile.__init__(self, name, title)
        self.age = age

    def information(self):
        print(f'Name : {self.name}')
        print(f'Title : {self.title}')
        print(f'age = {self.age}')

singer_1 = Detailed_profile('Elijah Woods', '24/7, 365', 42)
singer_1.information()

# 08.03 Super

class Detailed_profile_2(Profile):
    def __init__(self, name, title, genre):
        super().__init__(name, title)   # remove self
        self.genre = genre

# 08.04 Quiz

'''
Write a program for real estate transaction.
However, you must meet the following requirements.

Output sample
3 items for sale in total.
Manhattan Studio Apartment For Rent $1450/mo
Brooklyn 1 Bed Apartment For Rent $1850/mo
New Jersey Town House For Sale $1289000
'''

class House:
    def __init__(self, location, house_type, deal_type, price):
        self.location = location
        self.house_type =  house_type
        self.deal_type = deal_type
        self.price = price

    def show_detail(self):
        print(f'{self.location:<15}{self.house_type:<20}{self.deal_type:<10}${self.price:<10}')

houses = []
house_1 = House('Manhattan', 'Studio Apartment', 'For Rent', '1450/mo')
houses.append(house_1)
house_2 = House('Brooklyn', '1 Bed Apartment', 'For Rent', '1850/mo')
houses.append(house_2)
house_3 = House('New Jersey', 'Town House', 'For Sale', '1289000')
houses.append(house_3)

print(f'{len(houses)} items for sale in total.')
for house in houses:
    house.show_detail()