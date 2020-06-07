'''
Write Number in Expanded Form
You will be given a number and you will need to return it as a string in Expanded Form. For example:

expanded_form(12) # Should return '10 + 2'
expanded_form(42) # Should return '40 + 2'
expanded_form(70304) # Should return '70000 + 300 + 4'
note: All numbers will be whole numbers greater than 0.
'''

def expanded_form(number):
    i=0
    numbers_list=[]
    while number > 0:
        numbers_list.append(number%10*10**i)
        number = number//10
        i=i+1
    
    
    numbers_list_non_zeros = [i for i in numbers_list if i != 0]
    numbers_list_non_zeros_string = [ str(i) for i in numbers_list_non_zeros[::-1] ]
    
    return(' + '.join(numbers_list_non_zeros_string))