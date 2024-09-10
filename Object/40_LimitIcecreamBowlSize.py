# 40. 아이스크림 통의 크기 제한하기

# [메인 문제]
class Scoop():
    def __init__(self, flavor):
        self.flavor = flavor

class Bowl():
    max_scoops = 3

    def __init__(self):
        self.scoops = []

    def add_scoops(self, *new_scoops):
        for one_scoop in new_scoops:
            if len(self.scoops) < Bowl.max_scoops:
                self.scoops.append(one_scoop)
    
    def __repr__(self):
        return '\n'.join(scoop.flavor for scoop in self.scoops)

s1 = Scoop('chocolate')
s2 = Scoop('vaniila')
s3 = Scoop('persimmon')

b = Bowl()
b.add_scoops(s1, s2)
b.add_scoops(s3)
# print(b)



# [추가 문제]

class Person():
    population = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.population += 1
    
   
p1 = Person('p1', 20)
p2 = Person('p2', 21)
p3 = Person('p3', 21)
p4 = Person('p4', 22)
p5 = Person('p5', 23)

print(str(Person.population))
print(str(p1.population))
