# program to display the series 1, 3, 7, 13, 21, 43, 57, 73, 91, 111, 157, 183, 211 .... N

j = 1
N = int(input('Enter the maximum range:'))
for i in range(1, N+(N//5)-1):
    if i%6!=0:
        print(j,end = ' ')
    j = j + 2*i
    
'''
i = 2
j = 1
for k in range(1, 20):
    print(j, end = ',')
    if k >= 5 and k % 5 == 0:
        j += i
        i += 2
    j += i
    i += 2
'''
 