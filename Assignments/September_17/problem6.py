def pattern_a(rows):
    j = 0
    for i in range(1, rows+1):
        for j in range(j, i+j):
            print(j+1, end = ' ')
        print()
        j = j+1


def pattern_b(rows):
    step1 = 2
    step2 = 1
    print(1)
    print("1 2")

    for i in range(3, rows+1):
        for j in range(i):
            result = step1 + step2
            print(result, end = ' ')
            step2 = step1
            step1 = result
        print()

def main():
    rows = int(input('Enter number of rows: '))
    pattern_a(rows)
    print()
    pattern_b(rows)

if __name__ == "__main__":
    main()