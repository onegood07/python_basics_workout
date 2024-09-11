# 43. 동물원의 동물 만들기

class Animal():
    def __init__(self, color, numbers_of_legs):
        self.species = self.__class__.__name__
        self.color = color
        self.numbers_of_legs = numbers_of_legs
    
    def __repr__(self):
        return f"{self.color} {self.species}, {self.numbers_of_legs} legs"
        
    
class Sheep(Animal):
    def __init__(self, color):
        super().__init__(color, 4)

class Wolf(Animal):
    def __init__(self, color):
        super().__init__(color, 4)

class Snake(Animal):
    def __init__(self, color):
        super().__init__(color, 0)

class Parrot(Animal):
    def __init__(self, color):
        super().__init__(color, 2)
        