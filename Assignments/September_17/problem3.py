def pattern_a(rows):
    for _ in range(rows):
        print("12345")

def pattern_b(rows):
    for i in range(1, rows+1):
        print('*'*i)
        
def main():
    rows = int(input('Enter number of rows: '))
    pattern_a(rows)
    print()
    pattern_b(rows)

if __name__ == "__main__":
    main()