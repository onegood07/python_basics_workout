# 06. 피그 라틴 문장 만들기

# 함수 - 여러 단어가 결합된 영어 문장을 피그 라틴으로 번역하는 함수
def pig_latin_sentence(sentence):
    pig_latin_sentence_list = []
    sentence_list = sentence.split()
    
    for word in sentence_list:
        if word[0] in 'aeiou':
            pig_latin_sentence_list.append(word + 'way')
        else:
            pig_latin_sentence_list.append(word[1:] + word[0] + 'ay')
        
    return ' '.join(pig_latin_sentence_list)

# 실행
print(pig_latin_sentence('this is a test translation'))


# 함수 - 띄어쓰기로 구분되어 있는 문자열들의 리스트를 기반으로, 새로운 리스트를 만드는 함수
    # 예시) ['abc def ghi', 'jkl mno pqr', 'stu vmx yz']를 입력 시
    # ['abc jkl stu', 'def mno vmx', 'ghi pqr yz']를 리턴함

def split_str_list_return_new_list(words_list):
    output_list = []
    words_split_list = ' '.join(words_list).split() # 리스트 각 요소를 전부 담은 하나의 리스트로 변경
    print(type(words_split_list))
    for count in range(len(words_list)):
        output_list.append(words_split_list[count::len(words_list)])

    return output_list

# 실행      
print(split_str_list_return_new_list(['abc def ghi', 'jkl mno pqr', 'stu vmx yz']))


