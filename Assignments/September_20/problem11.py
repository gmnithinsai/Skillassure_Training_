'''
11. Write a program to accept the name, age, and favorite color of the user and print the output as below:

My name is <<name>>. I am <<age>> years old and my favorite color is <<color>>

'''
def output(n, a, c):
    print(f"My name is {n}. I am {a} years old and my favorite color is {c}")

if __name__ == '__main__':
    name = input("enter name: ")
    age = int(input("Enter age: "))
    color = input("Favourite color: ")
    output(name, age, color)