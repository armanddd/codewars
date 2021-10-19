def move_zeros(array):
    current_index = 0
    
    for i in range(len(array)):
        if array[i] != 0:
            array[current_index] = array[i] 
            current_index += 1

    for i in range(current_index, len(array)):
        array[i] = 0
    
    return array
