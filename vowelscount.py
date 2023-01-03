"""
Return # of vowels in a given string
"""
inputStr= input("Escriba una oración: ")

def vowelcount(inputStr):
    return sum(1 for x in inputStr if x in "aeiouAEIOU")

vowels = vowelcount(inputStr)
print("El número de vocales de su oración es:", vowels)
