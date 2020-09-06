from num2words import num2words

def Convert(number):
    return num2words(number, lang='id')



print("satuan :", Convert(1))
print("belasan :", Convert(12))
print("puluhan :", Convert(30))

