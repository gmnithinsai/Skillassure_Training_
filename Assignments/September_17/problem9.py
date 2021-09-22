''' Write a program to find whether a given number is a Fibonacci number or not.  '''

def fibon(n):
    lst = [1,1]
    while lst[-1]<n:
    	lst.append(lst[-2]+lst[-1])
    return lst	

def main():
    n = int(input("Enter the nth position of serise N = "))
    lst = fibon(n)
    if n in lst:
    	print(f"{n} is a Fibonacci number")
    else:
    	print(f"{n} is Not a Fibonacci number")

if __name__ == '__main__':
    main()
