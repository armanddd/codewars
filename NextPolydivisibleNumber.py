def next_num(n):
    n = n + 1
    while checkPolyDiv(n) == False:
        n += 1
    return n
            
def checkPolyDiv(nb):
    i = 1
    arr = []
    while i <= len(str(nb)):
        arr.append(str(nb)[0:i:1])
        i += 1
    for nr in arr:
        if int(nr) % len(nr) != 0:
            return False
    return True

