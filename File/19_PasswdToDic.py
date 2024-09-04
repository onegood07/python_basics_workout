# 19. /etc/passwd를 딕셔너리로 바꾸기

# [메인 문제]
# 키로 사용자 이름을 갖고, 값으로 사용자 ID를 갖는 딕녀서리 지정하기
def passwd_to_dic():
    output_dic = {}

    with open("/Users/kdk/Desktop/passwd.txt", 'r') as file:
        for line in file:
            if not line.startswith(('#', '\n')):
                user_info = line.split(':')
                output_dic[user_info[0]] = int(user_info[2])

    return output_dic

# 실행
print(passwd_to_dic())


# [추가 문제]
# 키로 사용자 이름을 갖고, 값으로 사용자 ID, 홈 디렉터리, 셸을 갖는 딕셔너리 지정하기

def passwd_to_dic_having_more_info(filename):
    users = {}

    with open("/Users/kdk/Desktop/passwd.txt") as file:
        for line in file:
            if not line.startswith(('#', '\n')):
                user_info = user_info.strip().split(':')
                users[user_info[0]] = [user_info[2], user_info[-2], user_info[-1]]
        
    return users

# 실행
print(passwd_to_dic_having_more_info('/etc/passwd'))