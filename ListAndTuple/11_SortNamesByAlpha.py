# 11. 이름을 알파벳 순서로 정렬하기

# 모듈 - operator 모듈의 itemgetter 함수를 활용
from operator import itemgetter

# 리스트 - 리스트 안이 딕셔너리로 구성된 리스트 (alphabetize_names 문제에서 사용)
PEOPLE = [{
    'first':'Reuven', 'last':'Lerner',
    'email':'reuven@lerner.co.il'
}, {
    'first':'kim', 'last':'younghee',
    'email':'imyoung@stu.kr'
}, {
    'first':'ko', 'last':'dakyung',
    'email':'kdk@dk.co.kr'
}, {
    'first':'kim', 'last':'youngji',
    'email':'kimkim@coco.kr'
}]

# 함수 - 이름 리스트를 매개변수로 받아 딕셔너리의 last 속성을 기준으로 정렬, 그 다음 first 속성 기준으로 정렬하는 함수
def alphabetize_names(people):
    for person in sorted(people, key=itemgetter('last', 'first')):
        print(f'{person["last"]}, {person["first"]}, {person["email"]}')
        
alphabetize_names(PEOPLE)


# 함수 - 양의 정수와 음의 정수를 매개변수로 받고 절댓값으로 이를 정렬하는 함수
def positive_negative_int(*ints):
    # abs 함수는 절댓값을 반환함
    return sorted(ints, key= abs) 

print(positive_negative_int(9, -8, 29, 30, -19))


# 함수 - 문자열 리스트를 매개변수로 받고, 문자열에 포함되어 있는 모음의 수로 이를 정렬하는 함수
def sort_by_vowel_count(str_list):
    def vowel_count(str):
        count = 0
        for alphabet in str:
            if alphabet in 'aeiouAEIOU':
                count += 1
        return count
            
    return sorted(str_list, key= vowel_count)


# 함수 - 위에 있는 걸 GPT가 만든 함수
def sort_by_vowel_count_by_gpt(*strings):
    def vowel_count(s):
        return sum(1 for char in s if char in 'aeiouAEIOU')  # 이렇게 하나로 합쳐서 하는 것도 가능하다는 점 알아두기, sum을 이용하는 것도 기억하기
    
    return sorted(strings, key=vowel_count)

print(sort_by_vowel_count(['apple', 'banana', 'peach']))