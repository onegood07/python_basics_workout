# 28. 숫자 결합하기

# [메인 문제]
def join_numbers(input_range):
    output = [str(x) 
              for x in range(input_range)]

    return ','.join(output)

# 실행
print(join_numbers(15))


# [추가 문제]
def zero_to_ten_join_numbers(ints_list):
    output = [
        str(x)
        for x in ints_list
        if 0 <= x and x <= 10
    ]

    return ','.join(output)

# 실행
print(zero_to_ten_join_numbers([-1, 0, 9, 3, 4, 5, 234, 53]))