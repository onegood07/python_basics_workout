# 45. 동물원 만들기

class Zoo():
    def __init__(self):
        self.cages = []
    
    def add_cages(self, *input_cages):
        for one_cage in input_cages:
            self.cages.append(one_cage)
    
    def __repr__(self):
        return '\n'.join(str(one_cage) for one_cage in self.cages)
    
    def animals_by_color(self, color):
        return [one_animal
                for one_cage in self.cages
                for one_animal in one_cage.animals
                if one_animal.color == color
        ]
    
    def animals_by_color(self, number_of_legs):
        return [one_animal
                for one_cage in self.cages
                for one_animal in one_cage.animals
                if one_animal.number_of_legs == number_of_legs
        ]
    
    def numbers_of_legs(self):
        return sum(one_animal.numbers_of_legs
                   for one_cage in self.cages
                   for one_animal in one_cage.animals)


class Cage():
    def __init__(self, id_number):
        self.animals = []
        self.id_number = id_number
    
    def add_animals(self, *in_animals):
        for animal in in_animals:
            self.animals.append(animal)
    
    def __repr__(self):
        output = f'Cage {self.id_number}\n'
        output += '\n'.join('\t' + str(animal) for animal in self.animals)

        return output

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
        
