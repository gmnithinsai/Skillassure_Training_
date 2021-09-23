# . Write a program to find the sum of all odd numbers from 1 to N. Accept N. Display the sum.
from functools import reduce

def main():
    N = int(input("Enter the range: "))
    list_odd = reduce(lambda a, b : a+b, list(filter(lambda x: x%2 != 0, [i for i in range(1, N+1)])))
    print(list_odd)

if __name__ == '__main__':
    main()