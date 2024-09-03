# 16. 두 딕셔너리의 차이 찾기

# 함수 - 세트를 활용하여 두 딕셔너리의 차이점을 찾아 리스트를 담은 딕셔너리 형태로 출력하는 함수
def dictdiff(first, second):
    output = {}
    all_keys = first.keys() | second.keys()

    for key in all_keys:
        if first[key] != second[key]:
            output[key] = [first.get(key), second.get(key)]
    
    return output

# 실행
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'a': 1, 'b': 2, 'c': 4}
print(dictdiff(dict1, dict2)) 



# 함수 - 짝수 개의 매개변수를 받고 이를 기반으로 딕셔너리를 만들어 리턴하는 함수, (인덱스가) 짝수 위치에 있는 매개변수가 딕셔너리의 키로 홀수 위치에 있는 매개변수가 딕셔너리의 값으로 들어감
# 예시) ('a', 1, 'b', 2) 입력 -> {'a': 1, 'b': 2} 출력
def pair_to_dict(*args):
    output = {}

    # 튜플도 슬라이싱 가능함. 짝수, 홀수 간격에 맞춰서 슬라이싱
    for even, odd in zip(args[0::2], args[1::2]): # zip을 사용하면 튜플을 동시에 순환할 수 있음 (유용함)
        output[even] = odd
    
    return output

# 실행
print(pair_to_dict('a', 1, 'b', 2))


# 함수 - 매개변수로 1개의 딕셔너리와 1개의 함수를 입력받아 매개변수로 받은 딕셔너리 값을 매개변수로 받은 함수에 전달하고 리턴값에 따라 키-값 쌍 분배
# 만약 함수가 True 리턴하면 키-값 쌍을 첫번째 딕셔너리에 넣고 False 리턴 시 두번째 딕셔너리에 넣고 (1번째_딕셔너리, 2번째_딕셔너리) 형태의 튜플을 리턴
def dict_partition(dictionary, function):
    output = ({}, {})

    for key, value in dictionary.items():
        if function(dictionary):
            output[0][key] = value
        else:
            output[1][key] = value

    return output

def vowel_in(dic):
    for key, value in dic.items():
        if key in 'aeiou':
            return True
    
    return False

# 실행
print(dict_partition({'a': 1}, vowel_in))