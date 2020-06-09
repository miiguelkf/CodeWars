'''
https://www.codewars.com/kata/51c8e37cee245da6b40000bd
Complete the solution so that it strips all text that follows any of a set of comment markers passed in. Any whitespace at the end of the line should also be stripped out.

Example:

Given an input string of:

apples, pears # and bananas
grapes
bananas !apples
The output expected would be:

apples, pears
grapes
bananas
The code would be called like so:

result = solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
# result should == "apples, pears\ngrapes\nbananas"
'''

def StripComments(s,markers):

    final = []
    for line in s.split('\n'):

        for i , char in enumerate(markers):
            if char in line:
                char_used = True
                line = line.split(char)[0].strip()

            if i == len(markers)-1:
                final.append(line)

    if not final:
        return (s)
    else:
        return('\n'.join(final))