# 07. 우비두비 단어 만들기

# 우비두비란? 1970년대 유행한 Zoom이라는 어린이 프로그램에서 등장한 비밀 언어
# 우비두비의 규칙 - 모든 모음(aeiou) 앞에 'ub'를 붙임

# 함수 - 간단한 우비두비 단어 만들기 함수
def ubbi_dubbi(words):
    output_words = []

    for word in words:
        if word in 'aeiou':
            output_words.append(f"ub{word}")
        else:
            output_words.append(word)
    
    return ''.join(output_words)

# 실행
words = input('기본 우비두비 규칙으로 만들 단어 입력하기: ')
print(ubbi_dubbi(words))


# 함수 - 대문자화(첫 글자 대문자, 이후 소문자)한 단어가 입력되면 우비두비 결과도 대문자화로 처리하는 함수
def upper_ubbi_dubbi(words):
    if words[0].isupper() and words[1:].islower(): # 대문자화인지 확인, if문 and 사용
        word_list = []

        for word in words:
            if word in 'aeiouAEIOU': # 한 글자씩 모음인지 확인. (주의) 대문자 모음도 확인해야함
                lower_word = word.lower() # 대문자 -> 소문자 전환
                word_list.append(f"ub{lower_word}") # 우비두비 적용
            else:
                word_list.append(word)
        
        output_word = ''.join(word_list) # 리스트 형식을 문자열로 변환
        
        if output_word[0].islower(): # 문자열의 첫 글자가 소문자일 경우
            return output_word[0].upper() + output_word[1:] # 대문자인 첫 글자 + 나머지 소문자 return

        return output_word

    else: # 입력된 단어가 대문자화가 아닌 경우
       return "여긴 대문자화만 처리하니 이 우비두비 말고 다른 우비두비를 찾아보세요."

# 실행
words = input('대문자화 우비두비 규칙으로 만들 단어 입력하기: ')
print(upper_ubbi_dubbi(words))