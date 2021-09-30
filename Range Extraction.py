def removeDuplicatesFromList(list):
    res = []
    for i in list:
        if i not in res:
            res.append(i)
    return res

def removeEmptyListsFromList(listt):
    for id, list in enumerate(listt):
        if len(listt[id]) < 3:
            listt.pop(id)
            removeEmptyListsFromList(listt)
    return listt
    

def solution(args):
    temp_array = []
    temp_array2 = []
    id = 0
    while id < len(args):
        if id + 1 >= len(args):
            break
        while args[id] + 1 == args[id + 1]:
            temp_array2.append(id)
            temp_array2.append(id + 1)
            id += 1
            if id + 1 >= len(args):
                break
        temp_array.append(temp_array2)
        temp_array2 = []
        id += 1
     
    for id, list in enumerate(temp_array):
        temp_array[id] = removeDuplicatesFromList(temp_array[id])
    temp_array = removeEmptyListsFromList(temp_array)
    
    print(temp_array)

    finalStr = ""
    temp_id2 = 0

    for id, val in enumerate(temp_array):
        print(temp_id2)
        while temp_id2 < temp_array[id][0]:
            finalStr += str(args[temp_id2]) + ","
            temp_id2 += 1
        if temp_id2 >= temp_array[-1][0]:
            finalStr += str(args[temp_array[id][0]]) + "-" + str(args[temp_array[id][-1]])
        else:
            finalStr += str(args[temp_array[id][0]]) + "-" + str(args[temp_array[id][-1]]) + ","    
        temp_id2 += len(temp_array[id])
        
    while temp_id2 < len(args):
        if temp_id2 == 0:
            finalStr += str(args[temp_id2])
        else:
            finalStr += "," + str(args[temp_id2])
        temp_id2 += 1
    
    return finalStr
    
