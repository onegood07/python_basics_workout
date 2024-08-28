# 03. 달린 시간 계산하기

# 함수 - 매일 10km를 달리는 사람이 (엔터키를 누르기 전까지) 계속 달린 시간을 기록할 때, 평균 달린 시간과 횟수를 출력하는 함수
def avg_run_timing():
    try: # 값을 잘못 입력하는 경우를 처리하기 위해 try문 사용
        avg_run_time = 0
        run_time_count = 0

        while True:
            run_time = input('10km를 뛰는데 걸린 시간을 입력해주세요: ')

            if not run_time: # 빈 문자열과 숫자 0은 False 처리됨
                break
            else:
                avg_run_time += float(run_time)
                run_time_count += 1
        
        avg_run_time = avg_run_time / run_time_count
        
        print(f"평균 시간은 {avg_run_time: .2f}이고, 달린 횟수는 {run_time_count}번 입니다.") # .2f는 소수점 2자리까지만 표시

    except ValueError as e: # 에러 발생 시 작동하는 코드. except에서 as 뒤에 변수를 지정하면 발생한 예외의 에러 메시지를 받아옴. 보통 exception의 e로 표기함.
        print("에러가 발생했습니다.", e)

# 실행
# avg_run_timing()


# 함수 - 부동소수점 1개와 정수 2개를 매개변수로 입력받고, before만큼 부동소수점 정수부분, after만큼 소수점 아래 부분을 추출해서 출력하는 함수
# 예시) 1234.5678, 2, 3을 매개변수로 입력하면, 34.567을 리턴하면 됨

# [1번] 파이썬에서 문자열도 시퀀스라서 인덱싱이 가능하다는 걸 몰랐을 때 작성한 코드
def input_float_and_int(input_float, before, after):
    split_float_list = input_float.split(".") # str.split() 사용 시, 리스트 형태로 분리됨

    # before로 부동소수점 정수부분 추출하기
    before_float = list(split_float_list[0])
    output_before_float_list = before_float[-int(before):] # 인덱싱 유의, '-'를 사용해서 뒤에서부터 인덱싱
    output_before_float = ''.join(output_before_float_list) # .join(s)는 모든 요소가 문자열로 구성된 시퀀스의 요소들을 합쳐줌 

    # after로 소수점 아래 부분 추출하기
    after_float = list(split_float_list[1])
    output_after_float_list = after_float[:int(after)]
    output_after_float = ''.join(output_after_float_list)

    print(f"계산된 값은 {output_before_float}.{output_after_float} 입니다.")

# 실행
# input_float, before, after = input('[1안] 부동소수점, before, after 값 입력하기: ').split(",")
# input_float_and_int(input_float, before, after)


# [2번] 파이썬에서 문자열이 시퀀스라 인덱싱이 가능함을 알게 되고 작성한 코드
def input_float_and_int(input_float, before, after):
    before_float, after_float = input_float.split(".") # .split() 사용으로 '.'을 기준으로 리스트 형태로 분리된 후, 각 변수에 문자열 형태로 저장됨
    print(f"계산된 값은 {before_float[-int(before):]}.{after_float[:int(after)]} 입니다.")

# 실행
input_float, before, after = input('[2안] 부동소수점, before, after 값 입력하기: ').split(",")
input_float_and_int(input_float, before, after)