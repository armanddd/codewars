def binary_array_to_number(arr):
    nb = 0
    for number in arr:
        nb = nb * 2 + digit
        print(nb)

#binary_array_to_number([0, 1, 0, 1])
#0101 --> 5
#0111 --> 7

def number_to_binary(nb):
    binary_array = []
    while nb >= 1:
        if nb % 2 != 0:
            binary_array.append(1)
        else:
            binary_array.append(0)
        nb //= 2
    binary_array = binary_array[::-1]
    print(binary_array)

# number_to_binary(90)
