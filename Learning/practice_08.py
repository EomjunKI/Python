# 08.01 Class

class Profile:
    def __init__(self, name, title):    # method
        self.name = name    # attribute
        self.title = title
        print(f'This singer is {self.name}.')
        print(f'This singer sing {self.title}')

singer_1 = Profile('Elijah Woods', '24/7, 365') # instance
singer_2 = Profile('Tape Machines', '3D Print')