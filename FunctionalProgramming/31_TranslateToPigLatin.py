# 31. 파일의 내용을 피그 라틴으로 번역하기

# [메인 문제]
def plword(word):
    if word[0] in 'aeiou':
        return word + 'way'
    
    return word[1:] + word[0] + 'ay'

def plfile(filename):
    return ' '.join(plword(one_word)
                    for one_line in filename
                    for one_word in one_line.split())



# [추가 문제]
people_hobbies = [
    {"Alice": {"reading", "swimming", "cooking"}},
    {"Bob": {"painting", "cycling"}},
    {"Charlie": {"swimming", "gaming"}},
    {"Diana": {"yoga", "swimming"}},
    {"Eve": {"running", "traveling"}}
]

def hobby():
    i = 0
    max_hobby = ''
    output = {}
    input = [ x 
            for one_dic in people_hobbies
            for key, set_value in one_dic.items()
            for x in set_value
    ]

    for one in input:
        output[one] = output.get(one, 0) + 1

    for key, value in output.items():
        if i < value:
            i = value
            max_hobby = key
            
    return max_hobby

print(hobby())

'''
* GPT가 구현한 더 간결하고 내포를 두번 사용한 코드
def hobby():
    # 리스트 내포를 사용하여 모든 취미를 평탄화
    input = [x for one_dic in people_hobbies for set_value in one_dic.values() for x in set_value]

    # 취미의 빈도를 딕셔너리로 계산
    output = {one: input.count(one) for one in set(input)}

    # 가장 빈도가 높은 취미 찾기
    max_hobby = max(output, key=output.get)

    return max_hobby

print(hobby())

'''