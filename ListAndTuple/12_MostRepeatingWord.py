# 12. 특정 글자를 가장 많이 가진 단어 찾기

import collections

# 함수 - 특정 글자를 가장 많이 가진 단어를 찾는 함수
def most_repeating_word(words):
    return max(words, key= most_repeating_letter_count)  # max 함수도 key 매개변수를 받을 수 있음

def most_repeating_letter_count(word):
    # Counter()는 {값 : 등장횟수}형태의 딕셔너리를 반환
    # Counter.most_common()은 (값, 등장횟수)형태의 튜플을 요소로 갖는 리스트 반환 
    return collections.Counter(word).most_common(1)[0][1]

# 실행
words = ['this', 'is', 'an', 'elementary', 'test', 'example']
print(most_repeating_word(words))