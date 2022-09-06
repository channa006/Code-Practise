import pyperclip
import re


phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?                # area code
    (\s|-|\.)?                        # separator
    (\d{3})                           # first 3 digits
    (\s|-|\.)                         # separator
    (\d{4})                           # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?    # extension
    )''', re.VERBOSE)


emailRegex = re.compile(
    r'''([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+(\.[a-zA-Z]{2,4}))''', re.VERBOSE)

text = str(pyperclip.paste())

matches = []


for groups in phoneRegex.findall(text):
    # print(groups)
    phoneNum = '.'.join([groups[1], groups[3], groups[5]])
    print(phoneNum)
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
        matches.append(phoneNum)
        print(phoneNum)


for groups in emailRegex.findall(text):
    # print(groups)
    matches.append(groups[0])

# print(matches)


# Copy results to the clipboard.
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))


else:
    print('No phone numbers or email addresses found.')
