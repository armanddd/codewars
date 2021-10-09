import re

def top_3_words(text):
    dict = {}
    words = re.findall("([a-zA-Z']+)", text)
    
    for id, word in enumerate(words):
        words[id] = word.lower()
    for id, val in enumerate(words):
        dict[val] = words.count(val)
    
    dict = {k: v for k, v in sorted(dict.items(), key=lambda item: item[1], reverse=True)}
    dict = removeApostropheFromDictionary(dict)
    
    try:
        return [list(dict)[0], list(dict)[1] , list(dict)[2]]
    except IndexError:
        try: 
            return [list(dict)[0], list(dict)[1]]
        except IndexError:
            try:
                return [list(dict)[0]]
            except IndexError:
                return []

def is_allowed_specific_char(string):
    charRe = re.compile("[^\']")
    string = charRe.search(string)
    
    return not bool(string)

def removeApostropheFromDictionary(dict):
    temp_index = 0

    while temp_index < len(dict):
        if is_allowed_specific_char(list(dict)[temp_index]):
            del dict[list(dict)[temp_index]]
            temp_index = 0
            continue
        temp_index += 1
    
    return dict
