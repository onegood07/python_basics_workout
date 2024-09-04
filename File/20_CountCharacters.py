# 20. 글자 수 세기

# [메인 문제]
'''
텍스트 파일을 전달했을 때, 텍스트 파일의 글자 수, 단어 수, 줄 수, 유일한 단어 수를 출력하기
1. 글자 수 (공백 포함)
2. 단어 수 (띄어쓰기로 구분된 요소 수)
3. 줄 수
4. 유일한 단어 수 ('No', 'no'는 다른 것으로 대소문자 구분)
'''

def count_char_line_word_unique():
    counts = {
        'chars': 0, 'lines': 0, 'words': 0
    }
    unique_words = set()

    with open('/Users/kdk/Desktop/wcfile.txt') as file:
        for one_line in file:
            counts['lines'] += 1
            counts['chars'] += len(one_line)
            counts['words'] += len(one_line.split())

            unique_words.update(one_line.split())

    counts['unique_words'] = len(unique_words)

    for key, value in counts.items():
        print(f"{key}: {value}")

# 실행
# count_char_line_word_unique()



# [추가 문제]
'''
사용자로부터 '텍스트 파일의 이름'과 '빈도를 계산할 단어들'을 띄어쓰기로 구분해서 입력받고,
사용자가 입력한 단어들을 키로, 텍스트 파일 내부에서 해당 키가 등장하는 횟수를 값으로 갖는 딕셔너리를 만들기
'''

def calculate_word_frequencies():
    user_inputs = input('텍스트 파일의 이름과 빈도를 계산할 단어를 입력하세요(띄어쓰기로 구분): ')

    # 입력받은 문자열을 '텍스트 파일 이름(인덱스 0)과 빈도를 계산할 단어(인덱스 1:)로 구분하기
    user_inputs = user_inputs.split()
    text_filename = user_inputs[0]
    words = user_inputs[1:]

    # 딕셔너리 내포를 활용하여 게산할 단어를 키로, 값을 0으로 갖는 딕셔너리 만들기
    output_dic = {keyword: 0 for keyword in words}

    # 입력받은 파일을 열고 단어 빈도수 계산해서 출력하기
    with open(f"/Users/kdk/Desktop/{text_filename}") as file:
        for one_line in file:
            line = one_line.split()

            for word in line:
                if word in words:
                    output_dic[word] += 1

    for key, value in output_dic.items():
        print(f"{key}: {value}")

# 실행
calculate_word_frequencies()