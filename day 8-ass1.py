############# DECORATOR #############


def hello_decorator(func):
    def inner1():
        print("Hello, this is before function execution")

        func()
        n = int(input("Enter the value of 'n': "))
        a = 0
        b = 1
        sum = 0
        count = 1
        print("Fibonacci Series: ", end = " ")
        while(count <= n):
            print(sum, end = " ")
            count += 1
            a = b
            b = sum
            sum = a + b


        print("This is after function execution")

    return inner1

def fibonacci():
        print("This is inside the function !!")

fibonacci = hello_decorator(fibonacci)
fibonacci()
