# 18. 마지막 줄 추출하기

# [메인 문제]
# 모듈 - 파일을 유사하게 구현할 수 있는 StringIO를 사용
from io import StringIO

# 가상의 파일 생성
fakefile = StringIO('''
nobody:*:-2:-2::0:0:Unprivileged User:/var/empty:/usr/bin/false
root:*:0:0::0:0:System Administrator:/var/root:/bin/sh
daemon:*:1:1::0:0:System Services:/var/root:/usr/bin/false
''')

# 함수 - 파일을 읽어 마지막 줄을 추출하는 함수
def get_final_line(filename):
    final_line = ''
    for current_line in fakefile:
        final_line = current_line
    return final_line

# print(get_final_line('/etc/passwd'))


# [추가 문제]
# 덱스트 파일을 읽어 들이고 한 줄씩 반복문을 돌리면서 정수만 포함하고 있는 단어를 찾아서 더한 뒤 출력하는 함수 만들기
WORDFILE = StringIO(''' 
apple
hello
3987
hi
3040              
''')

def get_int_word():
    output_sum = 0

    for word in WORDFILE:
        word = word.strip() # StringIO 객체는 각 줄에 개행 문자(\n)를 포함하므로 제거해야함
        if word.isdigit():
            output_sum += int(word)
    
    return output_sum

# 실행
print(get_int_word())


# [추가 문제]
# 텍스트 파일을 읽어 들이고 한 줄씩 반복문을 돌리면서 모음이 몇 개 있는지 세고 출력하는 함수 만들기

import collections

VOWELWORDFILE = StringIO(''' 
apple
hello
hi
how
are
you
good         
''')

def count_vowel_word():
    for line in VOWELWORDFILE:
       vowel_count = 0
       line = line.strip()
       word_dic = collections.Counter(line)

       if not line:
           continue

       for key, value in word_dic.items(): # if any(char in vowel_set for char in word_dic): 이런 형식도 가능함
           if key in 'aeiou':
               vowel_count += 1

       print(vowel_count)

# 실행
count_vowel_word()