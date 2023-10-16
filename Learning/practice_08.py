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