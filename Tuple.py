############TUPLE###########

# CREATE
t1 = (2,3,5,9,5,1)
print("Tuple is:", t1)

for i in range(0,len(t1)):
    print(t1[i])

# LENGTH
print("Length is:", len(t1))

# COUNT
print("count:",t1.count(5))

# OCCURENCES(INDEX)
print("Index:", t1.index(5))

#IN function
if 1 in t1:
    print("Element is present")
else:
    print("Element not present")

#del t1