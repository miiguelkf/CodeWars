'''
https://www.codewars.com/kata/556b85b433fb5e899200003f

Given a string representing a simple fraction x/y, your function must return a string representing the corresponding mixed fraction in the following format:

[sign]a b/c

where a is integer part and b/c is irreducible proper fraction. There must be exactly one space between a and b/c. Provide [sign] only if negative (and non zero) and only at the beginning of the number (both integer part and fractional part must be provided absolute).

If the x/y equals the integer part, return integer part only. If integer part is zero, return the irreducible proper fraction only. In both of these cases, the resulting string must not contain any spaces.

Division by zero should raise an error (preferably, the standard zero division error of your language).

Value ranges
-10 000 000 < x < 10 000 000
-10 000 000 < y < 10 000 000
Examples
Input: 42/9, expected result: 4 2/3.
Input: 6/3, expedted result: 2.
Input: 4/6, expected result: 2/3.
Input: 0/18891, expected result: 0.
Input: -10/7, expected result: -1 3/7.
Inputs 0/0 or 3/0 must raise a zero division error.
Note
Make sure not to modify the input of your function in-place, it is a bad practice.
'''

from fractions import Fraction

def mixed_fraction(s):

    positive = False
    n,d = s.split('/')

    if int(n)/int(d) >= 0:
        positive = True 

    s = str(Fraction(abs(int(n)),abs(int(d))))

    if '/' not in s:
        if positive:
            return(s)
        else:
            return('-' + s)

    n,d = s.split('/')

    integer = int(n)//int(d) 
    n = int(n) - integer*int(d)

    if positive:
        if integer == 0:
            return( str(n) + '/' + str(d)   )
        else:
            return( str(integer) + ' ' + str(n) + '/' + str(d)   )
    else:
        if integer == 0:
            return( '-' + str(n) + '/' + str(d)   ) 
        return ( '-' + str(integer) + ' ' + str(n) + '/' + str(d)   )

print( mixed_fraction('22/0') )

