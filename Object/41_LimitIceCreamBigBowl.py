# 41. 더 큰 아이스크림 통 만들기

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
            if len(self.scoops) < self.max_scoops:
                self.scoops.append(one_scoop)
    
    def __repr__(self):
        return '\n'.join(scoop.flavor for scoop in self.scoops)
    
# Bowl 부모 클래스, BigBowl이 자식 클래스
class BigBowl(Bowl):
    max_scoops = 5

s1 = Scoop('chocolate')
s2 = Scoop('vaniila')
s3 = Scoop('persimmon')
s4 = Scoop('4')
s5 = Scoop('5')

b = BigBowl()
b.add_scoops(s1, s2)
b.add_scoops(s3)
b.add_scoops(s4, s5)
print(b)




# [추가 문제]
class Loaf():
    def __init__(self, calories, carbohydrates, sodium, sugar, fat):
        self.calories = calories
        self.carbohydrates = carbohydrates
        self.sodium = sodium
        self.sugar = sugar
        self.fat = fat

    def get_nutrition(self, count):
        nutrients = {'calories': self.calories, 
                     'carbohydrates': self.carbohydrates,
                     'sodium': self.sodium, 
                     'sugar': self.sugar, 
                     'fat': self.fat}

        return {key: value * count for key, value in nutrients.items()}