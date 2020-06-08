def DecodeBits(bits):

    bits = bits.strip('0')

    bits_dictionary = {}
    last_bit = 0
    aux = 0

    for i in bits:
        if i == '0':
            if last_bit == '0':
                bits_dictionary[aux] = bits_dictionary[aux] + 1
            else:
                aux = aux + 1
                bits_dictionary[aux] = 1
                
        if i == '1':
            if last_bit == '1':
                bits_dictionary[aux] = bits_dictionary[aux] + 1
            else:
                aux = aux + 1
                bits_dictionary[aux] = 1
        last_bit = i

    min_repeated_times = min( list( bits_dictionary.values() ) )


    print(bits_dictionary)

    morse = []
    for key, value in bits_dictionary.items():
        if key%2 != 0:
            if value == min_repeated_times:
                morse.append('.')
            else:
                morse.append('-')
        elif key%2 == 0:  
            if value == 7*min_repeated_times:
                morse.append('   ')
            if value == 3*min_repeated_times:
                morse.append(' ')
        

    return(''.join(morse))
