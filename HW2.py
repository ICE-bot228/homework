from random import shuffle
a=input('имя')
ab=input('фамилия')
abc=input('отчество')
symbols=[]
symbols1 = []
symbols2=[]
for symbol in a:
    symbols += symbol

for symbol in ab:
    symbols1 += symbol
    
for symbol in abc:
    symbols2 += symbol
    
    
    
    
    
shuffle(symbols)
shuffle(symbols1)
shuffle(symbols2)


print(symbols)
print(symbols1)
print(symbols2)

