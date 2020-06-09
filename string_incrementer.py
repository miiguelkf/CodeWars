'''
https://www.codewars.com/kata/54a91a4883a7de5d7800009c
Your job is to write a function which increments a string, to create a new string.

If the string already ends with a number, the number should be incremented by 1.
If the string does not end with a number. the number 1 should be appended to the new string.
Examples:

foo -> foo1

foobar23 -> foobar24

foo0042 -> foo0043

foo9 -> foo10

foo099 -> foo100

Attention: If the number has leading zeros the amount of digits should be considered.
'''


def increment_string(strng):
    number = []
    for char in strng[::-1]:
        if char.isdigit():
            number.append(char)
        else:
            break
    
    number = number[::-1]
    
    if number:
        new_number = int( ''.join(number) ) +1
        w = strng[:-len(number) ]
    else:
        new_number = 1
        w = strng
        
    if len(str(new_number)) >= len(number):
        ans = w + str(new_number)
    else:
        ans = w + '0'*( len(number) - len(str(new_number)) ) +  str(new_number)
    
    return(ans)