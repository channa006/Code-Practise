import pyinputplus as pyip

while True:
    prompt = ' want to know how to keep idiot busy?\n'
    response = pyip.inputYesNo(prompt)

    if response == 'no':
        break
    
print('Have Nice Day')