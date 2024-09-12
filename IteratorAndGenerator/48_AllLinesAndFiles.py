# 48. 모든 줄과 모든 파일 출력하기

import os

def all_lines(path):
    for filename in os.listdir(path):
        full_filename = os.path.join(path, filename)
        try:
            for line in open(full_filename):
                yield line
        except OSError:
            pass