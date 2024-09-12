# 50. mychain 함수 만들기

def mychain(*args):
    for big in args:
        for small in big:
            yield small

for one_item in mychain('abc', [1,2,3], {'a': 1, 'b': 2}):
    print(one_item)