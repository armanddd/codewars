import re

def order(sentence):
    if not sentence:
        return ""
    indexes = list(map(lambda x: int(x) - 1, re.findall(r'\d+', sentence)))
    ans = []
    for id,val in enumerate(sentence.split(" ")):
        ans.append(sentence.split(" ")[indexes.index(id)])
    return " ".join(ans)
