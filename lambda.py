##############CAPITALIZE STRING#############
#def capitalize(str):
#str = "python essential batch!!"
 #   str1 = str.title()
  #  print(str1)
#capitalize(str)

capitalize_lambda = lambda str: str.title()
print("After Capitalizing string:", capitalize_lambda("python essential batch"))

list1 = ["i am sanchal r", "i am from pune", "i have completed m.e", "currently undergoing training in python via letsupgrade"]
print("Before mapping:",list(list1))

list2 = map(lambda str: str.title(),list1)
print("After mapping:",list(list2))

#output
#After Capitalizing string: Python Essential Batch
#Before mapping: ['i am sanchal r', 'i am from pune', 'i have completed m.e', 'currently undergoing training in python via letsupgrade']
#After mapping: ['I Am Sanchal R', 'I Am From Pune', 'I Have Completed M.E', 'Currently Undergoing Training In Python Via Letsupgrade']