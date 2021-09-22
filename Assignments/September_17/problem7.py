def series_a(N):
    j = 1
    for i in range(1,N+1):
        result = j+(i-1)**2
        print(result, end = ' ')
        j = result

def series_b(N):
    step1 = 1
    step2 = 1
    print("1 1", end = ' ')
    for i in range(N):
        next_step = step1+step2
        print(next_step, end = ' ')
        step1 = step2
        step2 = next_step

def main():
    N = int(input('Enter length of series:  '))
    series_a(N)
    print()
    series_b(N)

if __name__ == "__main__":
    main()
