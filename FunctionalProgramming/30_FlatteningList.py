# 30. 리스트 평탄화하기

# [메인 문제]
def flatten(input_list):
    return [x 
            for one_list in input_list 
            for x in one_list]

# 실행
# print(flatten([[1, 2], [3, 4]]))


# [추가 문제]
def flatten_odd_ints(input_list):
    return [int(x)
            for one_list in input_list 
            for x in one_list
            if int(x) % 2 == 1]

# 실행
print(flatten_odd_ints([[1, 2], [3, 4]]))