'''
7. Write a program to accept a sentence from the user, 
   print the number of characters in the sentence
   classify whether the sentence is short, medium, or long based on the below criteria:

Short - Less than 10 words

Medium - 10 to 20 words

Long - More than 20 words
'''
def classify(count):
    if count < 10:
        return "short"
    elif count > 9 and count < 21:
        return "Medium"
    else:
        return "Long"
def main():
    sentence = input("Enter a sentence: ").split(' ')
    words_count = len(sentence)
    print(classify(words_count))

if __name__ == '__main__':
    main()