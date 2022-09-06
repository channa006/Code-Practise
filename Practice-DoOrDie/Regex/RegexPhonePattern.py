import re

# 1
# phoneNumReg = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
# mo = phoneNumReg.search('my number os 198-749-0987')
# print('Phone Number Found ' + mo.group())


# 2

# phoneNumReg = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
# mo = phoneNumReg.search('my number os 001-749-0987')

# print(mo.group(0))
# print(mo.group(1))
# print(mo.group(2))

# area_code, main_number = mo.groups()

# print(area_code)
# print(main_number)


# 3

# phoneNumReg = re.compile(r'(\(\(\d\d\d\)\)) (\d\d\d-\d\d\d\d)')
# mo = phoneNumReg.search('my number os ((001)) 749-0987')

# print('Phone Number Found ' + mo.group(0))


# heroReg = re.compile(r'Batman|Robin')
# mo = heroReg.search('Super Hero Comic Version Robin Batman Robin')

# print(mo.group())

# batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
# mo = batRegex.search('Batmobile Batbat lost a wheel')

# print(mo.group(0))
# print(mo.group(1))

# 4

# batRegex = re.compile(r'Bat(wo)?man')
# mo1 = batRegex.search('The Adventures of Batman')
# print(mo1.group())


# mo2 = batRegex.search('The Adventures of Batwoman')
# print(mo2.group())


# phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
# mo1 = phoneRegex.search('My number is 415-555-4242')
# print(mo1.group())


# mo2 = phoneRegex.search('My number is 555-4242')
# print(mo2.group())

# Zero or More Matches

# batRegex = re.compile(r'Bat(wo)*man')
# mo1 = batRegex.search('The Adventures of Batman')
# print(mo1.group())

# mo2 = batRegex.search('The Adventures of Batwoman')
# print(mo2.group())

# mo3 = batRegex.search('The Adventures of Batwowowowowowowoman')
# print(mo3.group())


# Matching one or more with the Plus

# batRegex = re.compile(r'Bat(wo)+man')
# mo1 = batRegex.search('The Adventures of Batwoman')
# print(mo1.group())

# mo2 = batRegex.search('The Adventures of Batwowowowoman')
# print(mo2.group())

# mo3 = batRegex.search('The Adventures of Batman')
# print(mo3 == None)

# Matching Specific Repetitions with Braces


# greedyHaRegex = re.compile(r'(Ha){3,5}')
# mo1 = greedyHaRegex.search('HaHaHa')
# print(mo1.group())

# greedyHaRegex = re.compile(r'(Ha){4,5}?')
# mo1 = greedyHaRegex.search('HaHaHaHaHaHa')
# print(mo1.group())

# Findall Method

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('Cell: 415-555-9999 Work: 212-555-0000')
print(mo.group())

# # On the other hand, findall() will not return a Match object but a list of strings

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
li = phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
print(li)

# shortened character \d , \D , \w , \W , \s , \S

# xmasRegex = re.compile(r'\d+\s\w+')
# li = xmasRegex.findall(
#     '12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge')
# print(li)

#
# vowelRegex = re.compile(r'[aeiouAEIOU]')
# l = vowelRegex.findall('RoboCop eats baby food. BABY FOOD.')
# print(len(l))

# for item in l:
#     print(item)

# Negation
# vowelRegex = re.compile(r'[^aeiouAEIOU]')
# l = vowelRegex.findall('RoboCop eats baby food. BABY FOOD.')
# print(l)

# The Carat and Dollar Sign Characters
# you can use the ^ and $ together to indicate that the entire string must match the regex

# beginsWithHello = re.compile(r'^Hello')
# mo = beginsWithHello.search('Hello, world!')
# print(mo)

# endsWithNumber = re.compile(r'\d$')
# mo = endsWithNumber.search('Your number is 42')
# print(mo)


# The r'\d$' regular expression string matches strings that end with a numeric character from 0 to 9

# wholeStringIsNum = re.compile(r'^\d+$')
# mo = wholeStringIsNum.search('1234455567890')
# print(mo)

# The Wild card Character (.dot characeter)

# atRegex = re.compile(r'.at')
# mo = atRegex.findall('The cat in the hat sat on the flat mat.')
# print(mo)


# Matching Everything with Dot-Star
# The dot-star uses greedy mode: It will always try to match as much text as possible.

# nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
# mo = nameRegex.search('First Name: Al Last Name: Sweigart')

# print(mo.group(1))
# print(mo.group(2))


# nongreedyRegex = re.compile(r'<.*?>')
# mo = nongreedyRegex.search('<To serve man> for dinner.>')
# print(mo.group())

# greedyRegex = re.compile(r'<.*>')
# mo = greedyRegex.search('<To serve man> for dinner.>')
# print(mo.group())


# Matching Newlines with the Dot Character

# noNewlineRegex = re.compile('.*')
# p = noNewlineRegex.search(
#     'Serve the public trust.\nProtect the innocent.\nUphold the law.').group()
# print(p)


# newlineRegex = re.compile('.*', re.DOTALL)
# p = newlineRegex.search(
#     'Serve the public trust.\nProtect the innocent.\nUphold the law.').group()

# print(p)


# Ignore the Case Insensitive

# robocop = re.compile(r'robocop', re.I)
# p = robocop.search('RoboCop is part man, part machine, all cop.').group()
# print(p)

# p = robocop.search('ROBOCOP protects the innocent.').group()
# print(p)

# p = robocop.search(
#     'Al, why does your programming book talk about robocop so much?').group()
# print(p)


# Substituting Strings with the sub() Method

# namesRegex = re.compile(r'Agent \w+')
# p = namesRegex.sub(
#     'CENSORED', 'Agent Alice gave the secret documents to Agent Bob.')

# print(p)

#

# agentNamesRegex = re.compile(r'Agent (\w)\w*')
# p = agentNamesRegex.sub(
#     r'\1****', 'Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.')

# print(p)

# Managing Complex Regexes

# phoneRegex = re.compile(
#     r'((\d{3}|\(\d{3}\))?(\s|-|\.)?\d{3}(\s|-|\.)\d{4}(\s*(ext|x|ext.)\s*\d{2,5})?)', re.VERBOSE)

# p = phoneRegex.search(
#     'Find the phone 111-222-3333 and follow up on 444.555.6666')

# print(p.group())
