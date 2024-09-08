# 33. 값 변환하기

# [메인 문제]
def transform_values(func, dic):
    return { key: func(value)
            for key, value in dic.items()
    }

# d = {'a': 1, 'b': 2, 'c': 3}
# print(transform_values(lambda x: x*x, d))



# [추가 문제]
def ex_transform_values(func1, func2, dic):
    return { key: func1(value)
            for key, value in dic.items()
            if func2(key, value)
    }

def in_key_and_value(key, value):
    if key in 'aeiou' and value%2 == 0:
        return True
    
    return False
    
dic = {'a': 1, 'b': 2, 'c': 3, 'e': 4}
print(ex_transform_values(lambda x: x*x, in_key_and_value, dic))

