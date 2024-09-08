# 37. 함수 호출을 사용자에게 맡기기 - 모듈 파일

def menu(**options):
    while True:
        option_string = '/'.join(sorted(options))

        choice = input(f'옵션을 입력하세요({option_string}): ')

        if choice in options:
            return options[choice]()
        
        print('NO.')