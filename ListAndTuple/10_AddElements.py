# 10. 아무거나 더하기

# 함수 - + 연산자를 갖는 자료형(숫자, 문자열, 리스트, 튜플 등)을 매개변수로 받게 확장한 함수
def add_elements(*args):
    if not args:
        return args
    
    ouput = args[0]
    for item in args[1:]:
        ouput += item
    
    return ouput

# 실행
# print(add_elements())
# print(add_elements(10, 20, 30, 40))
# print(add_elements('a', 'b', 'c', 'd'))
# print(add_elements([10, 20, 30], [40, 50, 60], [70, 80, 90]))


# 함수 - add_elements와 비슷하고, *args 앞에 매개변수를 하나 더 받아, 그 매개변수보다 큰 요소만 더해서 리턴하는 함수
def add_elements_bigger_than(big_element, *args):
    count = len(args)
    start_index = 0

    # 가장 처음으로 big_element보다 큰 요소 찾기 (시작점)
    while count:
        for index, item in enumerate(args):
            count -= 1
            if big_element < item:
                output = item
                start_index = index
                break
           
    # 해당 요소부터 시작해 big_element보다 크면 더하기
    for item in args[start_index + 1:]:
        if big_element < item:
            output += item
    
    return output

# 실행
print(add_elements_bigger_than(10, 5, 20, 30, 6))
print(add_elements_bigger_than('c', 'd', 'c', 'b', 'h'))


# 함수 - 여러 개의 매개변수를 받아 정수 또는 정수로 변환할 수 있는 값만 더해서 리턴하는 함수
def sum_numeric(*args):
    output = 0

    for item in args:
        if type(item) == int:
            output += item
        elif item.isdigit():
            output += int(item)
    
    return output

print(sum_numeric(10, 20, 'a', '30', 'bcd'))
print(sum_numeric(1, '3', 'ad'))