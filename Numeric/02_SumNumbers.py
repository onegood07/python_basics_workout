# 02. 숫자 더하기

# 함수 - python의 sum 함수 구현해보기
def making_sum(*numbers): # *(전개 연산자)는 몇 개의 인자를 받을 건지 미리 설정하지 않고도 모든 경우를 처리 가능함, 모든 인수를 튜플 형태로 묶음
    # sum 함수와 같은 역할 수행
    result = 0
    for number in numbers: 
        result += number
    return result

# 실행
print(f"sum 함수 구현해보기: {making_sum(100, 200, 300, 400)}")


# 함수 - 매개변수로 숫자 리스트를 받고, 숫자의 평균을 계산하는 함수
def input_numbers_list_mean(numbers_list):
    numbers_sum = 0
    for number in numbers_list:
        numbers_sum += number

    mean = numbers_sum / len(numbers_list)
    return mean

# 실행
test_numbers_list = [100, 200, 300, 400]
print(f"{test_numbers_list} 리스트의 평균은 {input_numbers_list_mean(test_numbers_list)}입니다.")


# 함수 - 단어(문자열)로 구성된 리스트를 매개변수로 받고 (가장 짧은 단어 길이, 가장 긴 단어 길이, 단어 길이의 평균) 형태의 튜플 리턴하는 함수
def input_list_return_tuple(strings):
    # 변수 - 순서대로 가장 짧은 단어 길이, 가장 긴 단어 길이, 단어 길이의 평균을 담을 변수
    short_str_len = 100
    long_str_len = 0
    mean_str_len = 0

    # 계산 - 가장 짧은 단어, 가장 긴 단어 길이
    for str in strings:
        if len(str) > long_str_len:
            long_str_len = len(str)

        if len(str) < short_str_len:
            short_str_len = len(str)
        
        mean_str_len += len(str)
    
    # 계산 - 단어 길이의 평균
    mean_str_len = mean_str_len / len(strings)

    return (short_str_len, long_str_len, mean_str_len) # 튜플로 return

# 실행
test_strings_list = ['apple', 'banana', 'mango', 'grape', 'shinemuscat', 'peach']
print(f"튜플로 변환한 결과: {input_list_return_tuple(test_strings_list)}")



def input_any_list_return_sum(input_list):
    input_list_sum = 0
    
    for item in input_list:
        if type(item) == int or type(item) == float:
            input_list_sum += item
        elif type(item) == str:
            if item.isdigit():
                input_list_sum += int(item)
    
    return input_list_sum

test_any_list = ['apple', 'kdk', 1, 90, 3.14, '9', '71', 3, 'hello']
print(input_any_list_return_sum(test_any_list))