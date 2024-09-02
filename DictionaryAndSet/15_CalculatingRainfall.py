# 15. 강수량 계산하기

# 함수 - 도시 이름과 강수량을 입력받아 강수량을 더하고 출력하는 함수
def get_rainfall():
    rainfall = {}

    while True:
        city_name = input('도시 이름을 입력하세요: ')
        
        if not city_name:
            break

        rain_mm = int(input('도시의 강수량을 입력하세요: '))
        # dict.get() 사용하는 걸 잘 기억해두기
        rainfall[city_name] = rainfall.get(city_name, 0) + rain_mm 

    for city, rain in rainfall.items(): # for city, rain in rainfall.items()을 사용하면 key, value를 편하게 가져올 수 있음
        print(f"{city}: {rain}")

# 실행
# get_rainfall()


# 함수 - 모든 도시의 강수량 합계만 출력하는 것이 아니라 평균도 함께 출력하는 함수
def get_rainfall_avg_sum():
    # rainfall = {'city': {'sum':20, 'avg_count':3}}

    rainfall = {}

    while True:
        city_name = input('도시 이름을 입력하세요: ')
        
        if not city_name:
            break

        rain_mm = int(input('도시의 강수량을 입력하세요: '))

        # 중첩 딕셔너리 선언
        # rainfall.setdefault(city_name, {'sum': 0, 'avg_count': 0}) 이렇게 초기화해도 됨
        if city_name not in rainfall:
            rainfall[city_name] = {'sum': 0, 'avg_count': 0}

        rainfall[city_name]['sum'] = rainfall[city_name].get('sum') + rain_mm
        rainfall[city_name]['avg_count'] += 1

    for city, rain_info in rainfall.items():
        print(f"{city} 도시의 강수량 합계는 {rainfall[city]['sum']}이고 강수량 평균은 {rainfall[city]['sum']/rainfall[city]['avg_count']}입니다.")

get_rainfall_avg_sum()


    

        
