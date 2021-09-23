# Complete the piece of code so that the print5() function prints numbers from 1 to 5

def print5():
    i = 1
    print(i)
    while(True):
        i+=1
        if i == 6:
            break
        print(i)

def main():
    print5()

if __name__ == '__main__':
    main()