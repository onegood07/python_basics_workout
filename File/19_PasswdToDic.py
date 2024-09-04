# 19. /etc/passwd를 딕셔너리로 바꾸기

def passwd_to_dic():
    output_dic = {}

    with open("/Users/kdk/Desktop/passwd.txt", 'r') as file:
        for line in file:
            if not line.startswith(('#', '\n')):
                user_info = line.split(':')
                output_dic[user_info[0]] = int(user_info[2])

    return output_dic

# print(passwd_to_dic())


# nobody:*:-2:-2::0:0:Unprivileged User:/var/empty:/usr/bin/false
# 로그인 셸 (Login Shell): /usr/bin/false
# 사용자 ID (UID): -2
# 홈 디렉터리 (Home Directory): /var/empty
# 셀 (Shell): 로그인 셸과 동일하게 /usr/bin/false

def passwd_to_dic_having_more_info(filename):
    users = {}

    with open("/Users/kdk/Desktop/passwd.txt") as file:
        for line in file:
            if not line.startswith(('#', '\n')):
                user_info = line.strip()
                user_info = user_info.split(':')
                users[user_info[0]] = [user_info[2], user_info[-2], user_info[-1]]
        
    return users

print(passwd_to_dic_having_more_info('/etc/passwd'))