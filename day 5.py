##############IDENTIFY SUBLIST###############

list1 =[1,3,5,7,9,11,13]
list2 =[5,7,9]

print("Original list:" +str(list1))
print("Original list:" +str(list2))
f = 0
if(set(list2).issubset(set(list1))):
    f = 1
if(f):
    print("Match")
else:
    print("GONE")


#output
#Original list:[1, 3, 5, 7, 9, 11, 13]
#Original list:[5, 7, 9]
#Match
