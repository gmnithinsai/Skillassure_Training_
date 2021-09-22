def Apattern(rows):
    for i in range(1, rows+1):
        print(str(i)*rows)

def Bpattern(rows):
    for i in range(rows):
        print('*' * rows)

def main():
    rows = int(input("Enter number of rows: "))
    Apattern(rows)
    print()
    Bpattern(rows)


if __name__ == "__main__":
    main()