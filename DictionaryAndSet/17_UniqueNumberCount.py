# 17. 서로 다른 숫자의 개수 찾기

# 함수 - 매개변수로 정수가 들어있는 리스트를 받아 서로 다른 숫자의 개수를 리턴하는 함수
def how_many_different_numbers(ints_list):
    unique = set(ints_list)
    return len(unique)

# 실행
input_list = [1, 2, 3, 4, 2, 3, 4]
print(how_many_different_numbers(input_list))


''' 
* 기억할 점
- 딕셔너리의 키(key)는 숫자 또는 문자열처럼 해시로 만들 수 있어야 함
- 딕셔너리의 값(value)으로는 모든 것을 지정할 수 있음
- 딕셔너리의 키는 해당 딕셔너리 내부에서 유일함
- for 반복문 또는 내포를 활용하여 딕셔너리의 키를 기반으로 반복할 수 있음
'''