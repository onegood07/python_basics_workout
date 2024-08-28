# 05. 피그 라틴 단어 만들기

# 파이썬의 철학이라 할 수 있는 '반복하지 마라'를 기억하고 파이썬 프로그램은 짧아야 함.
# 코드를 작성하다가 반복되는 부분이 보이고, 긴 표현식 또는 문장을 작성하고 있다면 파이썬스러운 코드를 쓸 수 있도록 해야함.

def pig_latin(word):
    # 단어가 모음으로 시작한다면 끝에 way를 추가
    # 단어가 다른 글자로 시작한다면 첫 글자를 마지막으로 옮긴 뒤에 끝에 'ay'를 추가

    if word[0] in 'aeiou':
        pig_latin_word = word + 'way'
    else:
        pig_latin_word = word[1:] + word[0] + 'ay'
    return pig_latin_word

word = input('피그 라틴 단어를 입력하세요: ')
print(pig_latin(word))