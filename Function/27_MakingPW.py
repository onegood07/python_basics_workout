# 27. 비밀번호 생성기 만들기

# [메인 문제]
import random

def create_password_generator(chars):
    def create_password(length):
        output = []
        for _ in range(length):
            output.append(random.choice(chars))
        
        return ''.join(output)
    return create_password

# alpha_pw = create_password_generator('abcde')
# symbol_pw = create_password_generator('!@#$%')

# print(alpha_pw(5))
# print(symbol_pw(5))

# [추가 문제]
'''
비밀번호 생성기를 만들었으니 이렇게 만들어진 비밀번호가 시스템 기준을 만족하는지 확인하는 create_password_checker 만들기
'''

def create_password_generator(chars):
    def create_password(length):
        output = []
        for _ in range(length):
            output.append(random.choice(chars))
        
        return ''.join(output)
    return create_password

alpha_pw = create_password_generator('abcde')
symbol_pw = create_password_generator('!@#$%')

alpha_in = alpha_pw(5)
symbol_in = symbol_pw(5)

# pw = alpha_in + symbol_in
pw = 'ABCDabcd!@#$10293'
print(pw)

def collect_pw(pw):
    def create_password_checker(min_uppercase, min_lowercase, min_punctuation, mindigits):
        def uppercase_check():
            uppercase_count = sum(1 for c in pw if c.isupper())
            return uppercase_count >= min_uppercase
    
        def lowercase_check():
            lowercase_count = sum(1 for c in pw if c.islower())
            return lowercase_count >= min_lowercase
    
        def min_punctuation_check():
            punctuation_count = sum(1 for c in pw if c in '!@#$%^&*')
            return punctuation_count >= min_punctuation
        
        def mindigits_check():
            mindigits_count = sum(1 for c in pw if c in '1234567890')
            return mindigits_count >= mindigits
    
        if uppercase_check() and lowercase_check() and min_punctuation_check() and mindigits_check():
            print("로그인 성공! :)")
        else:
            print("로그인 실패 :(")

    return create_password_checker

a = collect_pw(pw)
a(4, 2, 3, 4)
