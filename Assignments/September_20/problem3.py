# Write a program with "Recursion" function to find the factorial of a given number. 0! is always 1.
# The factorial of a negative number is not possible.  

def factorial(num):
    if num >= 0:
        if(num == 1 or num == 0):
            return 1
        else:
            return num*factorial(num-1)
    else:
        return " The factorial of a negative number is not possible. "

def main():
    num = int(input("Enter a number to find factorial: "))
    print(factorial(num))

if __name__ == '__main__':
    main()