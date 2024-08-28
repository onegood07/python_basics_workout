# 08. 문자열 정렬하기

# 함수 - 문자열을 입력받아 문자열을 유니코드 순서로 정렬한 새로운 문자열을 만들어 리턴하는 함수
def strsort(str):
    return ''.join(sorted(str)) # 리스트를 유니코드 순서로 정렬하고 문자열로 만들기

# 실행
# str = input('문자열을 입력하세요: ')
# print(strsort(str))


# 함수 - 여러 개의 단어로 이루어진 문자열이 주어졌을 때, 각 단어별로 알파벳 순서로 정렬하는 함수
def sort_letters_in_words(str):
    output = []
    split_str_list = str.split()

    for word in split_str_list:
        output.append(''.join(sorted(word)))
    
    return ', '.join(output) 

# 실행
str = input('문자열을 입력하세요: ')
print(sort_letters_in_words(str))