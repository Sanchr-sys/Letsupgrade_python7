## DICTIONARY

#CREATE
Library = {1: 'Mechanical', 2:'Electronics' }
print(Library)

Library[3]= 'Computers'
print("After adding:", Library)
Library[3] = 'Computer science'
print("After update", Library)

#ADD MULTIPLE VALUES
Library.update({4:'Printing', 5:'Biotech', 6:'Information Technology'})
print("AAfter update:",Library)

# LENGTH
print("Length of Library is:",len(Library))

# PRINT KEYS
print("Keys:", Library.keys())

#PRINT VALUES
print("values:", Library.values())

# PRINT KEY/VALUE
print("key value:",Library.items())
print("value at 5:", Library.get(5))

#PRINT KEYS and VALUES and BOTH
for i in Library:
    print(i)
for i in Library:
    print(Library[i])
for i,j in Library.items():
    print(i,j)

#REMOVE ELEMENT
print("popitem():",Library.popitem())
print("pop:", Library.pop(2))

Library1 = {1:'Electrical', 2:'Instrumentation', 3:'Chemical'}
print(Library1)

Library1.clear()
print(Library1)

#IN function to check key only not values
if 1 in Library:
    print("Key present")
else:
    print("Key not present")

#DELETE
del Library
del Library1
