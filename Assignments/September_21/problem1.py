'''
1. Write a single line of code to print each of the following series:

[1, 8, 27, 64, 125, 216]

[1,9,25, 49, 81]

'''
print(list(map(lambda i: i**3, [i for i in range(1,7)])),
 list(map(lambda x: x**2, [i for i in range(1,10) if i%2 != 0])), sep = '\n')
