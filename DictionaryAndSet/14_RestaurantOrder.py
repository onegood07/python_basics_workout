# 14. 식당 주문 프로그램 만들기

# 함수 - 식당 주문 함수
# MENU라는 딕셔너리 선언 ('메뉴명':'가격')
MENU = {'sandwich':10, 'tea':7, 'salad':8}

def restaurant():
    total_price = 0

    while True:
        order = input('주문할 메뉴를 입력하세요: ').strip()

        if not order:
            print(f'총 가격은 {total_price}입니다.')
            break

        if order in MENU:
            total_price += MENU[order]
            print(f"주문한 {order}의 가격은 {MENU[order]}이고, 총 가격은 {total_price}입니다.")
        else:
            print("그런 메뉴는 없습니다.")

# 실행
# restaurant()


# 함수 - 간단하게 로그인하는 함수
USER = {'KoDaKyung':'kdkkdk0715', 'KimYoungHee':'kimkim0902', 'Lee':'leelee1234'}

def login():
    name, password = input('사용자 이름과 비밀번호를 입력하세요: ').split()

    if name in USER and password == USER[name]:
        print('로그인 성공!')
    else:
        print('로그인 실패')

# 실행
# login()


# 함수 - 날짜를 입력받고 해당 날짜의 온도를 출력하는 함수 (이때 날짜(key)는 문자열(str) 값으로 선언)
TEMPERATURE = {'0902':30, '0903':27, '0904':28, '0905':31, '0906':30}

def temperature():
    date = input('온도를 알고 싶은 날짜를 입력하세요(mm/dd): ')

    if date in TEMPERATURE:
        print(f"{date}의 온도는 {TEMPERATURE[date]}입니다.")

        # 예외처리(인덱스 범위)
        date_list = []
        for date_str in TEMPERATURE:
            date_list.append(date_str)
        
        if date == date_list[0]:
            print(f"다음날인 {date_list[1]}의 온도는 {TEMPERATURE[date_list[1]]}입니다.")
        elif date == date_list[-1]:
            print(f"어제인 {date_list[-2]}의 온도는 {TEMPERATURE[date_list[-2]]}입니다.")
        else:
            for index, one_date in enumerate(date_list):
                if date == one_date:
                    using_index = index
            print(f"어제인 {date_list[using_index-1]}의 온도는 {TEMPERATURE[one_date]}입니다.")
            print(f"다음날인 {date_list[using_index+1]}의 온도는 {TEMPERATURE[one_date]}입니다.")
        
# 실행
temperature()


# 함수 - 가족의 이름을 입력받아 나이를 출력하는 함수
import datetime

BIRTHDAY = {'kdk':datetime.date(2003, 7, 15), 'bro':datetime.date(2006, 8, 7), 'mom':datetime.date(1977, 12, 27), 'dad':datetime.date(1969, 11, 22)}

def age():
    now = datetime.datetime.now()
    name = input('이름을 입력하세요: ')
    
    if name in BIRTHDAY:
        print(f"{name}의 나이는 {now.year - BIRTHDAY[name].year}살입니다.")

# 실행
# age()