'''
Write the program to generate the following series
800, 802, 806, 812, 820,830, 842, 856, 872, 890, 910, 932, 956, 982 ... N 

Add the sum of digits of each number in the above series. Display each sum number. 
Ex. 800 = 8 + 0 + 0 = 8 
806 = 8 + 0 + 6 = 14
Display how many of these sum numbers have the digit 1. 
If N is 900, the output of the program should be as follows:

800 802 806 812 820 830 842 856 872 890 

      8 10 14 11 10 11 14 19 17 17 
      The  count  of the sum numbers which have the digit 1 = 9 
'''

n = int(input('Enter the range of numbers:'))
j = 0
num_list = []
new_list = []

for i in range(n):
    j = j + 2*i
    num_list.append(800 + j)
    
count = 0   
for i in num_list:10
    sums = 0
    while i>0:
        rem = i%10
        sums = sums+rem
        i = i//10
    if sums <= 9:
        count += 1
    new_list.append(sums)
print(new_list)
print('The count of sum numbers which have digit 1 is ', count)