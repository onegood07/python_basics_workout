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
# words = input('우비두비 규칙으로 만들 단어 입력하기: ')
# print(ubbi_dubbi(words))


# 함수 - 대문자화(첫 글자 대문자, 이후 소문자)한 단어가 입력되면 우비두비 결과도 대문자화로 처리하는 함수
def upper_ubbi_dubbi(words):
    if words[0].isupper() and words[1:].islower(): # 대문자화인지 확인
        output_word_list = []

        for word in words:
            if word in 'aeiouAEIOU':
                lower_word = word.lower()
                output_word_list.append(f"ub{lower_word}")
            else:
                output_word_list.append(word)
        
        output_word = ''.join(output_word_list)
        
        if output_word[0].islower():
            output = output_word[0].upper()
            return  output + output_word[1:]

        return output_word

    else:
       return "여긴 대문자화만 처리하니 이 우비두비 말고 다른 우비두비를 찾아보세요."

# 실행
words = input('우비두비 규칙으로 만들 단어 입력하기: ')
print(upper_ubbi_dubbi(words))