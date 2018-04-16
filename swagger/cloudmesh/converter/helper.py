def to_decimal(num):
    res, digit = 0, 0
    for i in range(len(num)-1, -1, -1):
        if num[i] == '1':
            res += pow(2, digit)
        digit += 1
    return res

def to_binary(num):
    num = int(num)
    tokens = []
    while num > 0:
        tokens.append('1' if num%2 else '0')
        num /= 2
    return "".join(reversed(tokens))
