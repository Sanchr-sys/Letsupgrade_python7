########## COLLECTIONS ###########

# LIST
#1 CREATION of list
Tech = ["Python", "C", "Java","Ruby","C#"]
print (Tech)

#2 print LENGTH of List
l = len(Tech)
print("Length of list is:", l)

#3 ADD elements in list
Tech.append("C++")
print("After append:", Tech)

#4 add MULTIPLE elements in list
Tech.extend(["Ruby", " Javascript"])
print("After extend:", Tech)

#5 OCCURENCES of elements in List
print(Tech.count("Ruby"))

#6 CREATE list from ANOTHER list
Tech1 = ["Perl", "Android"]

Tech2 = []
Tech2 = Tech1
print(Tech2)
Tech1.append("HTML")
print(Tech1)
print(Tech2)

#NO CHANGES in original list Tech1
Tech3 = Tech1.copy()
print(Tech3)
Tech1.append("SQL")
print(Tech1)
print(Tech3)

#7 POP element from list
Tech.pop()
print("After Pop:",Tech)

#8 REMOVE element from list by specifying Index
print(Tech)
print(Tech.remove('Java'))
print("After remove:",Tech)

#9 CLEAR list
Tech2.clear()
print(Tech2)

#10 DELETE list
del Tech3[1]
print("after 1st index element deleted:",Tech3)
del Tech3

#11 SORT list
Tech.sort()
print("After sort:",Tech)

#12 DESCENDING ORDER
Tech.reverse()
print("Reverse is:", Tech)