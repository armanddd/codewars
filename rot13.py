def rot13(message):
    ans = ""
    for c in message:
        if ord(c) > 64 and ord(c) < 91:
            if 90 % ord(c) > 13:
                res = ord(c) + 13
            else:
                res = 64 + (13 - (90 - ord(c)))
            ans += chr(res)
        if ord(c) > 96 and ord(c) < 123:
            if 122 % ord(c) > 13:
                res = ord(c) + 13
            else:
                res = 96 + (13 - (122 - ord(c)))
            ans += chr(res)
    return ans
