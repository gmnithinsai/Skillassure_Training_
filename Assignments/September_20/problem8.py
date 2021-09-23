'''
8. Write a program to accept a sentence from the user.

i) Print the original sentence

ii) Print the number of spaces in the sentence

iii) Print the sentence after stripping extra spaces in the beginning and end of the sentence

iv) Print whether or not some extra spaces have been stripped.
'''

def count_spaces(sentence):
    return sentence.count(' ')

def stripping(sentence):
    return sentence.strip()

def check_strip(sentence):
    return sentence == sentence.strip()

def main():
    sentence = input("Enter sentence: ")
    print("original sentence: {}".format(sentence))
    print(f"Number of spaces in sentence = {count_spaces(sentence)}")
    print(stripping(sentence))
    if check_strip(sentence) == True:
        print("Extra spaces have been stripped")
    else:
        print("No extra spaces")

if __name__ == '__main__':
    main()


