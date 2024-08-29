# 09. 처음과 마지막 요소 찾기

# 함수 - 시퀀스(리스트, 튜플, 문자열)을 입력받아 처음과 마지막 요소를 추출하고 둘을 결합해 원래 시퀀스로 리턴하는 함수
def firstlast(sequence):
    return sequence[:1] + sequence[-1:] # 어떤 시퀀스가 들어올지 모르고 원래 형태를 유지하기 위해 '추출'이 아니라 '슬라이싱'을 사용함

# 실행
# print(firstlast([100, 200, 300])) # 리스트
# print(firstlast((12, 34, 56, 78))) # 튜플
# print(firstlast('sequence')) # 문자열


# 함수 - 숫자로 구성된 리스트 또는 튜플을 매개변수로 받아 [홀수인_숫자의_합, 짝수인_숫자의_합] 형태의 리스트를 리턴하는 함수
def even_odd_sum(input_ints):
    output_even_odd_sum = [0, 0]
    
    for one_int in input_ints:
        if one_int % 2 == 0: # 짝수일 때
            output_even_odd_sum[1] += one_int
        else:
            output_even_odd_sum[0] += one_int
    
    return output_even_odd_sum

# 실행
# print(even_odd_sum([11, 22, 33, 44]))


# 함수 - 숫자로 구성된 리스트 또는 튜플을 매개변수로 받아, 받은 숫자들을 더하고 빼고 더하고 빼고를 번갈아가며 반복한 형태의 값을 출력하는 함수
def plus_minus(input_ints):
    output_sum = input_ints[0]

    # 더하기
    for one_int in input_ints[1::2]:
        output_sum += one_int
    
    # 빼기
    for one_int in input_ints[2::2]: 
        output_sum -= one_int

    return output_sum

# 실행
# print(plus_minus([10, 20, 30, 40, 50, 60]))


# 함수 - 
def test(*data):
    output_list = []
    empty_list = [[] for _ in range(len(data[0]))]

    for one_data in data: # 이터러블 하나씩 받는 거임 [10, 20, 30] 이런 식으로
        for index, one_thing in enumerate(one_data): # [10, 20, 30] 안의 10
            empty_list[index].append(one_thing)
    
    for index in range(len(empty_list)):
        output_list.append(tuple(empty_list[index]))

    return output_list

# 실행
print(test([10, 20, 30], 'abc'))