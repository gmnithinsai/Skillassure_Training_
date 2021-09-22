def series_a(N):
    j = 2
    k = 1
    for i in range(1, N+1):
        if i%2 == 0:
            print(j, end = ' ')
            j = j+4
        else:
            print(k, end = ' ')
            k = k+3

def series_b(N):
    lst = [1,5,8]
    for i in range(1,N+1):
        lst.append(lst[-3]+lst[-2]+lst[-1])
    for k in lst:
        print(k, end=', ')


def main():
    N = int(input("Enter the length of series: "))
    series_a(N)
    print()
    series_b(N)
	
if __name__ == '__main__':
	main()
