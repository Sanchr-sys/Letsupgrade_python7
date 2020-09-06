##################IF ELSE###################

num1 = int(input("Enter Altitude "))
print(num1)
if num1 <= 1000:
    print("Hey Pilot, Safe to Land")
elif num1 > 1000 and num1 < 5000:
    print("Hey Pilot, Bring down to 1000")
#elif num1 > 5000:
    #print("Hey Pilot,Turn Around")
else:
    print("Hey Pilot,Turn around and Attempt later")


#################FOR LOOP###################
#PRIME NUMBERS
initial = 2
end = 200

for r in range(initial, end):
    for m in range(2, r):
        if (r % m == 0):
            break
    else:
        print(r)