# 34. 모든 모음을 포함하는 단어 찾기

# [메인 문제]
def get_sv(filename):
    vowels = {'a', 'e', 'i', 'o', 'u'}

    return {word.strip()
            for word in open(filename)
            if vowels < set(word.lower())
            }

