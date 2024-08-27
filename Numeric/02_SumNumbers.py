# 02. 숫자 더하기

def making_sum(*numbers): # *(가변 인수)는 몇 개의 인자를 받을 건지 미리 설정하지 않고도 모든 경우를 처리 가능함, 모든 인수를 튜플 형태로 묶음
    # sum 함수와 같은 역할 수행
    result = 0
    for number in numbers: 
        result += number
    return result # return으로 함수의 결과를 반환

print(making_sum(10, 20, 30))
