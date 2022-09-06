from logging import exception
from xmlrpc.client import ResponseError
import pyinputplus as pyip

# response = pyip.inputNum(prompt='Enter a number: ')
# response = pyip.inputNum(prompt='Enter a number: ',min=100)
# response = pyip.inputNum(prompt='Enter a number: ',greaterThan=100)
# response = pyip.inputNum('>',min=3,lessThan=6)


# limit , timeout and default keyword Arguments

# response = pyip.inputNum(limit=2)

# Below not through the exception
# response = pyip.inputNum(limit=2,default='N/A')

# the allowRegexes and blockRegexes Keyword Argument
# response = pyip.inputNum(allowRegexes=[r'(I|V|X|L|C|D|M)+',r'zero'])


# response = pyip.inputNum(blockRegexes=[r'[02468]$'] )


def addsUpToTen(numbers):
    numbersList = list(numbers)
    for i,digit in enumerate(numbersList):
        numbersList[i]=int(digit)

    if sum(numbersList)!= 10:
        raise Exception('the digits must add up to 10, not %s.' %(sum(numbersList)))
    
    return int(numbers)


response=pyip.inputCustom(addsUpToTen)