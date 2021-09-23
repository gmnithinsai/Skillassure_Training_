'''
13)
 Write a program to accept a paragraph from the user.
 Print all the words in paragraph alphabetically after removing duplicates. 
 The words should be ordered according to the ASCII value of each character in every word,
 as read from left to right, irrespective of whether they are upper case or lower case.

'''
def wordssorted(paragraph):
    a = ' '.join((dict.fromkeys(paragraph.split())))
    b = a.split(' ')
    b.sort()
    return b
if __name__ == '__main__':
    paragraph = input("Enter sentence: ")
    result = wordssorted(paragraph)
    for i in result:
        print(i, end = ' ')
        