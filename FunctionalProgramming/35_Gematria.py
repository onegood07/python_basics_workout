# 35. 제마트리아 (1)

import string

def gematria():
    return {alpha: number
            for number, alpha in enumerate(string.ascii_lowercase, 1)
    }

print(gematria())