# 42. dict를 상속해서 FlexibleDict 클래스 만들기

# [메인 문제]
class FlexibleDict(dict):
    def __getitem__(self, key):
        try:
            if key in self:
                pass
            elif str(key) in self:
                key = str(key)
            elif int(key) in self:
                key = int(key)
        except ValueError:
            pass

        # 자식이 아니라 부모 클래스의 __getitem__을 사용하는 이유는 키를 FlexibleDict에서 변경해주고, 해당하는 값을 dict(부모 클래스)에서 가져오기 때문임.
        return dict.__getitem__(self, key)

fd = FlexibleDict()

fd['a'] = 100
print(fd['a'])

fd[1] = 100
print(fd['1'])