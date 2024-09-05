# 22. CSV 파일 읽고 쓰기

# [메인 문제]
import csv

def passwd_to_csv(passwd_filename, csv_filename):
    with open(passwd_filename) as input, open(csv_filename, 'w') as output:
        infile = csv.reader(input, delimiter=':')
        outfile = csv.writer(output)
        for line in infile:
            if len(line) > 1:
                outfile.writerow((line[0], line[2]))

# 실행
passwd_to_csv('/Users/kdk/Desktop/passwd.txt', '/Users/kdk/Desktop/text.csv')



# [추가 문제]
'''
각각의 줄에 10~100 사이의 정수 10개를 랜덤하게 CSV 파일로 출력하고,
다시 파일을 읽어 들어서 각 줄에 있는 정수의 합과 평균을 구해서 출력하는 프로그램 만들기
'''
import random

def each_line_sum_avg(filename):
    with open(filename, 'w') as file:
        inoutfile = csv.writer(file)

        for _ in range(20):
            line_list = []
            for _ in range(10):
                line_list.append(random.randint(10, 100))
            inoutfile.writerow((line_list))
        
    with open(filename) as one_file:
        outfile = csv.reader(one_file, delimiter=',')

        for line in outfile:
            output_sum = 0
            for one_int in line:
                output_sum += int(one_int)

            print(f"sum: {output_sum}, avg: {output_sum/10}")

# 실행
each_line_sum_avg('/Users/kdk/Desktop/ex.csv')