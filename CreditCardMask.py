"""
Function maskify, which changes all but the last four characters into '#'.
"""
cc = input("Ingresa el número de cuenta: ")

"""
def maskify(cc):
   return "#"*(len(cc)-4) + cc[-4:]

result = maskify(cc)
print (result)
"""

def maskify(cc):
    cc_len = (len(cc))
    if cc_len <= 4: return cc
    return (cc_len - 4) * '#' + cc[-4:]
    
result = maskify(cc)
print ("Con la máscara se ve así", result)
