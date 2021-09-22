#Write a program to display the 1st , 2nd , and 4th multiple of 7 which gives the remainder 1 when divided by 2,3,4,5 and 6

def main():
    a = []
    for i in range(0, 2000, 7):
        if i>0:
            if i%2==1 and i%3==1 and i%4==1 and i%5==1 and i%6==1:
                a.append(i)
    print('The numbers are: {},{},{}'.format(a[0], a[1], a[3]))

if __name__ == '__main__':
    main()