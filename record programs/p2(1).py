def factorial(n):

    if n == 0 or n == 1:
     return 1
    else:
        return n * factorial(n-1)

#Test the function

num = int(input("Enter a number to find its factorial: "))
print(f"The factorial of {num} is {factorial(num)}")
