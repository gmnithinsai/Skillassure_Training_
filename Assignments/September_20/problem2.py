# Write a program to find the sum of all the prime numbers in the range n to m.
# Display each prime number and the final sum
from functools import reduce

def isprime(num):
    for i in range(2, int(num/2)+1):
        if (num % i) == 0:
            #print(num, "is not a prime number")
            break
    else:
        return num


def main():
    n, m = [int(x) for x in input("enter range with space sepatated integers: ").split()]
    result = reduce(lambda a,b : a+b, list(filter(isprime, [i for i in range(n, m+1)])))
    print(result)

if __name__ == '__main__':
    main()
