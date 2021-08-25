# program to print the following series 4, 16, 36, 64,.......N

N = int(input('Enter the length of series: '))
#maxi = int(input('Enter maximum number: '))

for i in range(N):
    print(4 * ((i + 1) ** 2), end = ',')
    
'''for i in range(100):
    result = 4 * (i + 1) ** 2
    if result <= maxi :
        print(result, end = ',')
    else:
        break'''
