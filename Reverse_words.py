"""
Function that accepts a string parameter, and reverses each word in the string. All spaces in the string should be retained.
"""
inputStr= input("Escriba una oración: ")

"""
def reverse_words(str):
    return ' '.join(s[::-1] for s in inputStr.split(' '))
"""
"""
def reverse_words(inputStr):
  #go for it
  newStr = []
  for i in inputStr.split(' '):
      newStr.append(i[::-1])
  return ' '.join(newStr)
"""
"""
import re

def reverse_words(inputStr):
  return re.sub(r'\S+', lambda w: w.group(0)[::-1], inputStr) #Esta no me funcionó
"""

def reverse_words(inputStr):
  return " ".join(map(lambda word: word[::-1], inputStr.split(' ')))
  
reverse = reverse_words(inputStr)
print("Su oración al revés se ve así: ", reverse)

"""
str.split() will squeeze consecutive spaces into 1. But if you give it a delimiter, it will no longer squeeze consecutive delimiters. So "aaa".split('a') will give you ["", "", ""] "a".join(["", "", ""]) will give you "aaa"
"""

