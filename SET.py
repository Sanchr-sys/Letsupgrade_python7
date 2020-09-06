#########SET#########

#CREATE
Set1={2,1,2,3,4}
print(Set1)

for i in Set1:
    print("elements in set:",i)

#Length
print("Length is:",len(Set1))

#ADD and UPDATE
Set1.add(8)
print("after addition:", Set1)
Set1.update({9,10})
print("After update:",Set1)

#REMOVE and DISCARD
Set1.remove(9)
print("Remove:",Set1)
Set1.discard(10)
print("After discard:",Set1)

#NOERROR even if element not present in set
Set1.discard(20)
print("After discard:",Set1)

Set1.clear()
print("After clear:", Set1)

del Set1


#Mathematical operations
#UNION
S1={1,2,3,4,5,6}
S2={4,5,6,7,8,9}
print("Union is:",S1.union(S2))

#INTERSECTION
S1={1,2,3,4,5,6}
S2={4,5,6,7,8,9,10}
print("Intersection:",S1.intersection(S2))

#DIFFERENCE
S1={1,2,3,4,5,6}
S2={4,5,6,7,8,9,10}
print("Difference is:", S1.difference(S2))
print("Difference is:",S2.difference(S1))

#SYMMETRIC DIFFERENCE
print("Symmetric difference:",S1.symmetric_difference((S2)))

#SUBSET
S1={1,2,3}
S2={1,2,3,4,5}
print("Is subset():",S1.issubset(S2))
print("Is subset():",S2.issubset(S1))

#SUPERSET
print("Is superset():",S1.issuperset(S2))
print("Is superset():",S2.issuperset(S1))

#DISJOINT
S3 = {'a','b','c'}
print("Disjoint:",S1.isdisjoint(S3))