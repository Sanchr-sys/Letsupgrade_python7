############PRIME NOS###########

def whether_Prime(a):
    for num in range(2,a):
        if a%num == 0:
            return False
        else:
            return True

Prime_list = filter(whether_Prime, range(2500))
print ('Prime numbers in range(2500):', list(Prime_list))