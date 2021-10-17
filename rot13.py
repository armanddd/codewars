import string

def rot13(message):
    result = ""
    for char in message:
        if 65 <= ord(char) <= 90:
            if ord(char) + 13 > 90:
                char = chr(ord(char) + 13 - 90 + 65 - 1)
            else:
                char = chr(ord(char) + 13)
        elif 97 <= ord(char) <= 122:
            if ord(char) + 13 > 122:
                char = chr(ord(char) + 13 - 122 + 97 - 1)
            else:
                char = chr(ord(char) + 13)
        result += char
    return result
