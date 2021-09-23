'''
9. Write a program to accept a sentence and a search word from the user

i) Print whether or not the search word is present in the sentence irrespective of the cases.

ii) Print whether or not the search word is present in the sentence taking cases into consideration.

'''
def searchword_casesensitive(sentence, search_word):
    word_list = sentence.split()
    if search_word in word_list:
        return True
    else:
        return False
def searchword(sentence, search_word):
    word_list = sentence.upper().split()
    if search_word.upper() in word_list:
        return True
    else:
        return False


if __name__ == "__main__":
    sentence = input("Enter sentence: ")
    search_word = input("enter word to search: ")
    res1 = searchword(sentence, search_word)
    res2 = searchword_casesensitive(sentence, search_word)
    if res1 == True:
        print('search word is present in the sentence irrespective of the cases')
    else:
        print('search word is not present in the sentence irrespective of the cases')
    if res2:
        print('search word is present in the sentence taking cases into consideration')
    else:
        print('search word is not present in the sentence taking cases into consideration')

    