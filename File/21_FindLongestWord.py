# 21. 파일에서 가장 긴 단어 찾기

# [메인 문제]
# 파일을 읽어들이고 가장 긴 단어를 찾기
import os

def find_longest_word(filename):
    longest_word = ''

    with open(filename) as file:
        for line in file:
            words = line.split()
            for word in words:
                if len(word) > len(longest_word):
                    longest_word = word
    
    return longest_word

def find_all_longest_words(dirname):
    # 딕셔너리 컴프리헨션(Dictionary Comprehension)은 파이썬에서 제공하는 간결하고 직관적인 방식으로, 반복문과 조건문을 사용하여 딕셔너리를 생성하는 방법
    return {
        filename:
        find_longest_word(os.path.join(dirname, filename))
        for filename in os.listdir(dirname)
        if os.path.isfile(os.path.join(dirname, filename))
    }

# print(find_all_longest_words('/Users/kdk/Desktop/books'))

'''
딕셔너리 컴프리헨션?
딕셔너리 컴프리헨션을 사용하면, 반복문을 사용해 키와 값을 하나씩 생성하여 딕셔너리를 만들 수 있음
기본형: {key_expression: value_expression for item in iterable}
뒤에 if와 같은 조건문 추가도 가능함
'''


# [추가 문제]
# HTTP 서버의 로그 파일을 읽어 들이고 응답코드 202와 304 등의 요청이 몇 번 왔는지 정리하여 출력하기
# for문과 if문을 활용해서 응답코드의 인덱스를 찾아봄 -> 8번 인덱스가 응답코드
def count_http_response_codes(filename):
    respones_codes = {}

    with open(filename) as file:
        for line in file:
            one_line = line.split()
            code = one_line[8]
            respones_codes[code] = respones_codes.get(code, 0) + 1
                
    return respones_codes

print(count_http_response_codes('/Users/kdk/Desktop/mini-access-log.txt'))