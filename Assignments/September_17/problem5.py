def pattern_a(rows):
    for i in range(1, rows+1):
        print(str(i)*i)

def pattern_b(rows):
    j = 0
    for i in range(1, rows+1):
        result = (1*j) + i
        print(result)
        j = result * 10

def main():
    rows = int(input('Enter number of rows: '))
    pattern_a(rows)
    print()
    pattern_b(rows)

if __name__ == "__main__":
    main()