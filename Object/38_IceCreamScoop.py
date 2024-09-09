# 38. 아이스크림 스쿱 만들기

# [메인 문제]
class Scoop():
    def __init__(self, flavor):
        self.flavor = flavor
    
def create_scoop():
    scoops = [Scoop('chocolate'),
              Scoop('vaniila'),
              Scoop('persimmon')]
    
    for scoop in scoops:
        print(scoop.flavor)

create_scoop()


# [추가 문제]
class Beverage():
    def __init__(self, name, temperature= 75):
        self.name = name
        self.temperature = temperature

def create_beverage():
    beverages = [Beverage('water', 100),
                Beverage('juice', 10),
                Beverage('milk')]
    
    for beverage in beverages:
        print(beverage.temperature)

create_beverage()



