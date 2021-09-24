'''
7. Complete the following program:

users = ['Customer', 'Admin', 'Analyst']

loginCredentials = ['Valid','Invalid','Empty','Empty']

// Write a single line of code to print the all the possible combinations of elements
 of users with elements of loginCredentials. For example: ('Customer','Valid'),('Customer','Invalid'),
 (Customer,'Empty'),...

'''
users = ['Customer', 'Admin', 'Analyst']

loginCredentials = ['Valid','Invalid','Empty','Empty']

print(','.join([str((i,j)) for i in users for j in loginCredentials]))