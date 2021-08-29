# Write a program that takes amount and displays them in words 
# a.  Input: 1234 
# b. Output: One thousand two hundred and thirty four only 

words_units = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
words_tens1 = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
words_tens2 = ['', 'none', 'twenty', 'thirty', 'fourty','fifty', 'sixty','seventy','eighty','ninety']
words_Hun = ['',
    'one hundred and',
    'two hundred and',
    'three hundred and',
    'four hundred and',
    'five hundred and',
    'six hundred and',
    'seven hundred and',
    'eight hundred and',
    'nine hundred and'
]
words_thous = [
    'none','one thousand',
               'two thousand', 
               'three thousand', 
               'four thousand',
               'five thousand',
               'six thousand',
               'seven thousand',
               'eight thousand', 
               'nine thousand']

num = int(input())

lis = []
while num > 0:
    rem = num % 10
    lis.append(rem)
    num = num//10
    
if lis[-3] == 1:
    print(words_thous[lis[-1]], words_Hun[lis[-2]], words_tens1[lis[-4]])
elif lis[-4] == 0 and lis[-3] == 0:
    print(words_thous[lis[-1]], words_Hun[lis[-2]][0:-4])
elif lis[-3] == 0:
    print(words_thous[lis[-1]], words_Hun[lis[-2]], words_units[lis[-4]])
elif lis[-2] == 0:
    print(words_thous[lis[-1]], words_tens2[lis[-3]], words_units[lis[-4]])
else:
    print(words_thous[lis[-1]], words_Hun[lis[-2]], words_tens2[lis[-3]], words_units[lis[-4]])
    
