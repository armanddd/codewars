import re

def order(sentence):
    if not sentence:
        return ""
    indexes = list(map(lambda x: int(x) - 1, re.findall(r'\d+', sentence)))
    ans = []
    for id in range(len(sentence.split(" "))):
        ans.append(sentence.split(" ")[indexes.index(id)])
    return " ".join(ans)
