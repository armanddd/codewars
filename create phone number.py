def create_phone_number(n):
    return "(" + "".join(list(map(str, n)))[0:3] + ")" + " " + "".join(list(map(str, n)))[3:6] + "-" + "".join(list(map(str, n)))[6:]
