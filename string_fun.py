###########STRING#######

str1 = 'Lets'
str2 = 'Upgrade'
print(str1,"\n", str2)
print("Hello, \n",str1, str2)
print("Lets","Upgrade")
print("Lets"+"Upgrade")
print("Lets" "Upgrade")
print("Lets"  "Upgrade")
print("It's collection lecture today")
print('It"s collection lecture today')
print('It\'s collection lecture today')
print("\r" "It's collection lecture \n today")
c = 'python'
d = 'enjoyable'
print("I am learning {}".format(c))
print("I am learning {} and its {}".format(c,d))

str3 = " Lets Upgrade"
print("Original string is:", str3)
l = len(str3)
print("Length of string is:",l)
print("String in upper case:", str3.upper())
print("String in lower case:", str3.lower())
print(" ",str3.capitalize())
print(" ",str3.title())
print("Original string is:", str3)
print(" ",str3.lstrip())
print(" ",str3.rstrip())
print(" ",str3.strip())
str4 = "Good Evening"
print(" ",str4.startswith("Good"))
print(" ",str4.endswith("Evening"))
print(" ",str4.endswith("Night"))
print(" ",str4.find("ning"))
print(" ",str4.index("Good"))

str5 = "Hey, Wazzup, Hey"
print(" ",str5.count("Hey"))

str6 = "one, two, three"
list1 = str6.split(",")
print(list1)

str7 = "Hello, Learning python"
print(" ",str7.split(" "))

str8 = "Python is an awesome programming language"
print(str8.center(100))

print(" ",str5.replace("Hey"," Bye"))
list1 =['www', 'google','com']
print(list1)
print("-".join(list1))

#STRING SLICING
str9 = "I am trying to achieve slicing"
print(str9[2])
print(":",str9[2:6])
print(":",str9[3: ])
print(":",str9[ :8])
print(":",str9[3:12:2])
print(";",str9[4::5])
print(" ",str9[::-1])
print("str9[::-1]:",str9[::-1])

