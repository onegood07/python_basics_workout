# 32. 딕셔너리 반전하기

# [메인 문제]
def reverse_dic(input_dic):
    return {value: key 
            for key, value in input_dic.items()
            }

d = {'a': 1, 'b': 2, 'c': 3}
print(reverse_dic(d))


# [추가 문제]
def vowel_count_in_sentence(sen):
    return {word: sum(1 for letter in word if letter in 'aeiou')
            for word in sen.split()
    }

sen = "this is an easy test"
print(vowel_count_in_sentence(sen))