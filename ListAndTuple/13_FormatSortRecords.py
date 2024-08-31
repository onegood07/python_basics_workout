# 13. 튜플 레코드 출력하기

import operator
# 모듈 - [2번]에서 사용하는 namedtuple을 불러오기 위한 모듈
from collections import namedtuple 

PEOPLE = [
    ('Donald', 'Trump', 7.85),
    ('Vladimir', 'Putin', 3.626),
    ('Jinping', 'Xi', 10.603)
]

# [1번] 함수 - 튜플을 요소로 갖는 리스트 PEOPLE의 값을 정렬해서 테이블 형태로 출력하는 함수
def format_sort_records(list_of_tuple):
    output = []
    template = "{1:10} {0:10} {2:5.2f}"

    for person in sorted(list_of_tuple, key= operator.itemgetter(1, 0)):
        output.append(template.format(*person))
    
    return output
    
# print('\n'.join(format_sort_records(PEOPLE)))


# [2번] 함수 - 위 예제의 튜플을 namedtuple로 바꿔서 구현해보기
Person = namedtuple('Person', ['first', 'last', 'time'])

PEOPLE_INFO = [
    Person('Donald', 'Trump', 7.85),
    Person('Vladimir', 'Putin', 3.626),
    Person('Jinping', 'Xi', 10.603)
]

# GPT의 도움을 받음
# def format_sort_records_using_namedtuple_by_gpt(people_info):
#     output = []
#     template = "{first:10} {last:10} {time:5.2f}"

#     for person in sorted(people_info, key= lambda x: (x.last, x.first)):
#         formatted = template.format(first=person.first, last=person.last, time=person.time)
#         output.append(formatted)
    
#     return output

# format_sort_records_using_namedtuple_by_gpt(PEOPLE_INFO)