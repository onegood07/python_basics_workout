# 2024/08/27 화요일
# 01. 숫자 맞히기 게임

# 모듈 - 맞춰야하는 숫자를 랜덤으로 불러오기 위한 random 모듈 불러오기
import random

# 함수 - 양의 정수만 입력받는다는 가정을 한 게임
def only_input_positive_int_guessing_game():
    answer_number = random.randint(0, 100) # 주의, 최댓값이 범위에 포함됨

    while True:
        guess_number = int(input('추측한 숫자를 입력하세요: ')) # 입력받은 값이 문자열 타입이라 int로 변환

        if guess_number > answer_number:
            print("정답보다 높아요.")
        elif guess_number < answer_number:
            print("정답보다 낮아요.")
        else:
            print("정답입니다!")
            break # 정답을 맞추면 while문 탈출


# 함수 - 예외 처리를 한 상태인 게임 (음수, 소수, 문자열 등을 입력했을 때)
def anything_input_guessing_game():
    answer_number = random.randint(0, 100) # 주의, 최댓값이 범위에 포함됨

    while True:
        guess_number = input('추측한 값을 입력하세요: ')

        if guess_number.isdigit(): # str.isdigit() - 문자열 안에 숫자만 있는지 확인하는 메서드
            guess_number = int(guess_number) # 문자열이므로 정수형으로 변환
            if guess_number > answer_number:
                print("정답보다 높아요.")
            elif guess_number < answer_number:
                print("정답보다 낮아요.")
            else:
                print("정답입니다!")
                break
        else:
            print(f"{guess_number} 말고 양수만 입력하세요!") # f-문자열 사용


# 함수 - 숫자를 예측할 기회를 3번으로 제한한 게임
def only_three_chance_guessing_game():
    answer_number = random.randint(0, 100) # 주의, 최댓값이 범위에 포함됨
    answer_chance = 0

    while answer_chance < 3:
        guess_number = int(input('추측한 숫자를 입력하세요: ')) # 입력받은 값이 문자열 타입이라 int로 변환

        if guess_number > answer_number:
            print("정답보다 높아요.")
        elif guess_number < answer_number:
            print("정답보다 낮아요.")
        else:
            print("정답입니다!")
            break

        answer_chance += 1
        print(f'남은 기회는 {3 - answer_chance}번 입니다.')

        if answer_chance == 3: # 3번의 기회 모두 소진 시 출력되는 문장
            print("3번 모두 실패했습니다. 다음 기회에!")


# 함수 - 사전 순서로 정렬된 단어 리스트에서 정답 맞추기 게임
def string_guessing_game():
    answer_str_list = sorted(['lddf', 'ewrf', 'fefe', 'hsw', 'nafe', 'ddfh', 'dfhe']) # 사전순서대로 리스트 정렬
    print(f'단어 리스트는 다음과 같습니다.: {answer_str_list}')

    # 랜덤한 단어 결정하기 (list, index 활용)
    answer_str_list_index_count = len(answer_str_list) - 1 # count가 아니라 len를 사용해야 인덱스 범위 구할 수 있음
    answer_str_list_index = random.randint(0, answer_str_list_index_count) # 인덱스 결정하기
    selected_answer_str = answer_str_list[answer_str_list_index] # 선택된 정답 단어

    while True:
        guess_str = input('추측한 단어를 입력하세요: ')

        if selected_answer_str == guess_str:
            print("정답입니다!")
            break
        elif selected_answer_str > guess_str:
            print(f"{guess_str}는 정답보다 앞에 위치합니다.")
        elif selected_answer_str < guess_str:
            print(f"{guess_str}는 정답보다 뒤에 위치합니다.")

# 실행
string_guessing_game()