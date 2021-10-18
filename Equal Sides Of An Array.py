def find_even_index(arr):
    leftAdd = []
    rightAdd = []
    for id, nb in enumerate(arr):
        leftAdd.append(sum( [ nb for nb in arr[:id + 1:1] ] ))
            
    for id, nb in enumerate(arr):
        rightAdd.append(sum( [ nb for nb in arr[:-id - 2:-1] ] ))
        
    for id in range(len(arr)):
        if leftAdd[id] == rightAdd[-id - 1]:
            return id
    
    return -1

def find_even_index(arr):
    for i in range(len(arr)):
        if sum(arr[:i]) == sum(arr[i + 1:]):
            return i
    return -1
