import math, string
from random import randrange

maxlength = 30
alphabets = True
numbers = True
specials = True
domains = True

#popular top level domains. They consist of 55 2 letter domains, 6 3 letter domains, and 2 4 letter domains
tlds = ['.ru', '.de', '.jp', '.uk', '.br', '.it', '.pl', '.fr', '.in', '.ir', '.au', '.cn', '.nl', '.es', '.cz', '.kr', '.ua', '.ca', '.eu', '.co', '.gr', '.za', '.ro', '.ch', '.se', '.tw', '.hu', '.vn', '.mx', '.be', '.at', '.tr', '.dk', '.me', '.ar', '.tv', '.sk', '.no', '.us', '.fi', '.io', '.cl', '.id', '.pt', '.by', '.il', '.nz', '.ie', '.kz', '.lt', '.hk', '.cc', '.my', '.sg', '.bg', '.com', '.org', '.net', '.biz', '.xyz', '.edu', '.info', '.club']

#I am not allowing backslash and single quote. Dot must be the last character
specialCharacters = '!#$%&*=?^_`{|}~-.'

howManyResults = 50

beforeAtOptions = []
afterAtOptions = []

#adding alphabets into conditates list
if alphabets is True:
  alphabetString = string.ascii_lowercase[:26]
  beforeAtOptions.extend(list(alphabetString))
  afterAtOptions.extend(list(alphabetString))

#adding numbers into conditates list
if numbers is True:
  numberString = list(range(10))
  beforeAtOptions.extend(numberString)
  afterAtOptions.extend(numberString)

#adding special characters into conditates list
if specials is True:
  specialString = list(specialCharacters)
  beforeAtOptions.extend(specialString)

#count the number of possible character options
#Minus 1 for not including dot
beforeAtOptionsLength = len(beforeAtOptions) - 1
afterAtOptionsLength = len(afterAtOptions)

resultCount = 0

while(resultCount < howManyResults):
  #pick the length of the string.
  stringLength = randrange(6, maxlength + 1)
  result = [''] * stringLength

  #pick the position of @ mark
  at = randrange(1, stringLength - 4)
  result[at] = '@'
  
  #see if . is possible and whether it is going to be somewhere
  if at > 2:
    dotPossible = True
  else:
    dotPossible = False
  
  dotFlag = False
  count = 0
  while(count < at):
    #include dot
    if dotPossible and (count == 1):
      beforeAtOptionsLength = len(beforeAtOptions)
    
    #not include dot as the last character before the @ mark.
    if dotPossible and (count == (at - 1)):
      beforeAtOptionsLength = len(beforeAtOptions) - 1
    
    #avoid ..
    if(dotFlag == True):
      beforeAtOptionsLength = len(beforeAtOptions) - 1

    #pick a random number as an index for character option list
    n = randrange(0, beforeAtOptionsLength)
    result[count] = str(beforeAtOptions[n])

    if(dotFlag == True):
      beforeAtOptionsLength = len(beforeAtOptions)
      dotFlag = False

    if(str(beforeAtOptions[n]) == '.'):
      dotFlag = True

    count = count + 1
  
  if(domains == True):
    #select a top level domain and reverse the string
    if (stringLength == 6):
      topLevelDomain = tlds[randrange(0, 55)][::-1]
    elif (stringLength == 7):
      topLevelDomain = tlds[randrange(0, 61)][::-1]
    else:
      topLevelDomain = tlds[randrange(0, 63)][::-1]
    
    #insert the characters of the top level domain from the end
    index = -1
    for letter in topLevelDomain:
      result[index] = letter
      index = index -1
    
    rest = stringLength - len(topLevelDomain)
  
  else:
    rest = stringLength

  count = at + 1
  while(count < rest):
    #pick a random number as an index for character option list
    n = randrange(0, afterAtOptionsLength)
    result[count] = str(afterAtOptions[n])
    count = count + 1
  
  if(domains == False):
    #pick a position for .
    dot = randrange(at + 2, stringLength - 2)
    result[dot] = '.'

  resultString = ''.join(result)

  print resultString
  
  resultCount = resultCount + 1
