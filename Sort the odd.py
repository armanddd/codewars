def sort_array(source_array):
    for i,v in enumerate(source_array):
        for i2,v2 in enumerate(source_array):
            if source_array[i] < source_array[i2] and source_array[i] % 2 == 1 and source_array[i2] % 2 == 1:
                temp = source_array[i]
                source_array[i] = source_array[i2]
                source_array[i2] = temp
    return source_array
