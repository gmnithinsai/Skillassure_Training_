# program to print the following series : 1, 1, 2, 3, 5, 8, 13, … N 
n = int(input('Enter the range:'))
sums = 0
a = 0
b = 1
count = 1
while count <= n:
    print(sums, end = ' ')
    count+=1
    a = b
    b = sums
    sums = a+b
    
    