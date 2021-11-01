def hexdump(data):
    output = []
    output_2 = []
    output_3 = []
    counter = 0
    for i in data:
        if counter % 16 == 0:
            output.append(' '.join(output_2))
            output.append('  ')
            output.append(''.join(output_3))
            output.append('\n{:08x}: '.format(counter // 16 * 16))
            output_2 = []
            output_3 = []
        output_2.append('{:02x}'.format(i))
        if i in range(32, 127):
            output_3.append(chr(i))
        else:
            output_3.append('.')
        counter += 1
    else:
        output.append(' '.join(output_2))
        output.append('  ' + '   ' * (16 * (counter % 16 != 0) - counter % 16))
        output.append(''.join(output_3))
    return (''.join(output)).replace('\n', '', 1).replace('  ', '', 1)

def dehex(dump):
    output = []
    for line in dump.split('\n'):
        for i in line[10:57].split():
            number = int(i, 16)
            output.append(number)
    return bytes(output)
