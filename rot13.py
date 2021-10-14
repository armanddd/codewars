def rot13(message):
    ans = ""
    for c in message:
        if ord(c) > 64 and ord(c) < 91:
            if 90 % ord(c) > 13:
                c = chr(ord(c) + 13)
            else:
                c = chr(64 + (13 - (90 - ord(c))))
        if ord(c) > 96 and ord(c) < 123:
            if 122 % ord(c) > 13:
                c = chr(ord(c) + 13)
            else:
                c = chr(96 + (13 - (122 - ord(c))))
        ans += c
    return ans
