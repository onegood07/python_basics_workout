# 49. 이전 호출로부터 지난 시간 계산하기

import time
def elapsed_since(data):
    last_time = None
    for item in data:
        current_time = time.perf_counter()
        delta = current_time - (last_time or current_time)
        last_time = time.perf_counter()
        yield (delta, item)

for t in elapsed_since('abcd'):
    print(t)
    time.sleep(2)