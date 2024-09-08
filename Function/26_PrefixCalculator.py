# 26. 전위 표기법 계산기 만들기

# [메인 문제]
'''
딕셔너리를 활용할 수 있다는 점이 큰 깨달음. 함수를 데이터로 취급하여 다른 자료 구조 내부에 저장해서 활용 가능하다는 점이 신기.
'''
import operator

def calc(to_solve):
    operations = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv,
        '**': operator.pow,
        '%': operator.mod
    }

    op, first, second = to_solve.split()
    return operations[op](int(first), int(second))

# 실행
# print(calc('+ 1 2'))


# [추가 문제]
'''이번 예제를 확장해서 수식에 3개 이상의 피연산자를 지정할 수 있게 구현해보기.
왼쪽부터 오른쪽 순서대로 연산자들이 적용하게 만들기'''

def many_calc(args):
    operations = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv,
        '**': operator.pow,
        '%': operator.mod
    }

    using_list = args.split()

    op = using_list[0]
    using_ints = [int(x) for x in using_list[1:]]

    output = using_ints[0]

    for one_int in using_ints:
        output = operations[op](output, one_int)

    return output

print(many_calc('+ 1 2 3 4 5 6'))