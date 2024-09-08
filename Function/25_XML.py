# 25. XML 생성기 만들기

'''
* 파이썬 함수의 특징
1. 함수는 객체라서, 일반 데이터처럼 다룰 수 있음. -> 다른 자료 구조 내부에 저장해서 사용 가능
2. 같은 이름의 함수를 여러 개 정의할 수 없음. -> 시그니처(함수 이름, 매개변수 개수, 매개변수 종류)가 다르면 여러 개 정의할 수 있는 다른 언어와 다름.
'''

# [메인 문제]
def myxml(tagname, content='', **kwargs):
    output = ''.join([f'{key}="{value}"' for key, value in kwargs.items()])
    return f"<{tagname} {output}>{content}</{tagname}>"

# 실행
# print(myxml('tagname', 'hello', a=1, b=2, c=3))


# [추가 문제]
# 매개변수로 여러 개의 숫자를 입력받고, 이를 모두 곱해서 리턴하는 multiplyAll 함수를 만들기

def multiplyAll(*args): 
    output = args[0]
    for one_int in args[1:]:
        output *= one_int
    
    return output

print(multiplyAll(1, 2, 3, 4, 5, 6, 7))

