def pattern_a(rows):
    b = rows
    for i in range(1, rows+1):
        print(" "*(b-1), end = '')
        print('*'*i)
        b = b-1

def pattern_b(rows):
    x = rows
    y = rows
    for i in range(1, rows+1):
        print(" "* (x-1), end = '')
        print("*" * ((2*i)-1), end = '')
        print(" " * (y-1))
        x = x-1
        y = y-1

def main():
    rows = int(input('Enter number of rows: '))
    pattern_a(rows)
    print()
    pattern_b(rows)

if __name__ == "__main__":
    main()