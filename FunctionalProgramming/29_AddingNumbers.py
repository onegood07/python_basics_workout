# 29. 숫자 더하기

# [메인 문제]
'''
def sum_numbers(seq):
    output = 0
    split_seq = seq.split()
    for one in split_seq:
        if one.isdigit():
            output += int(one)
    
    return output

input_seq = input('문자열을 입력하세요: ')
print(sum_numbers(input_seq))
'''

# 제너레이터 활용
def sum_numbers(seq):
    return sum(int(num)
               for num in seq.split() 
               if num.isdigit())

# 실행
# input_seq = input('문자열을 입력하세요: ')
# print(sum_numbers(input_seq))



# [추가 문제]
people = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 18},
    {"name": "Charlie", "age": 35},
    {"name": "Diana", "age": 13},
    {"name": "Eve", "age": 40}
]

def are_you_minor():
    return [{'name': one_dic['name'], 
             'age': one_dic['age'], 
             'age_in_months': one_dic['age'] * 12} 
            for one_dic in people
            if one_dic['age'] < 20
           ]

print(are_you_minor())