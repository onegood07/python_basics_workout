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