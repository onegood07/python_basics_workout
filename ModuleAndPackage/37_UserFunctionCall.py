# 37. 함수 호출을 사용자에게 맡기기 - 실행 파일

from menu import menu

def func_a():
    return "A"

def func_b():
    return "B"

return_value = menu(a=func_a, b=func_b)
print(f'결과는 {return_value}')