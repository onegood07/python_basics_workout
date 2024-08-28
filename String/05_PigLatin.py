# 05. 피그 라틴 단어 만들기

# 파이썬의 철학이라 할 수 있는 '반복하지 마라'를 기억하고 파이썬 프로그램은 짧아야 함.
# 코드를 작성하다가 반복되는 부분이 보이고, 긴 표현식 또는 문장을 작성하고 있다면 파이썬스러운 코드를 쓸 수 있도록 해야함.

# 함수 - 피그 라틴 단어 만들기 함수
# 피그 라틴 단어란? 영어권 국가의 어린이들이 사용하는 비밀 언어로 아래와 같은 규칙이 있음.
    # 단어가 모음(aeiou)으로 시작한다면 끝에 way를 추가
    # 단어가 다른 글자로 시작한다면 첫 글자를 마지막으로 옮긴 뒤에 끝에 'ay'를 추가

def pig_latin(word):
    if word[0] in 'aeiou': # 문자열이 시퀀스라서 in과 같은 연산자를 사용할 수 있음
        pig_latin_word = word + 'way' 
        # return f'{word}way' # 더하기도 가능하지만, 이렇게 return과 f-문자열을 활용해서 하는 것도 가능함
    else:
        pig_latin_word = word[1:] + word[0] + 'ay'

    return pig_latin_word

word = input('피그 라틴 단어를 입력하세요: ')
print(pig_latin(word))
