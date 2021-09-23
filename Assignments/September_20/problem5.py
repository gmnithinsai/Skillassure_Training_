class EvaluateOutput:
    def A(self):
        number = 0
        for number in range(10):
            if number == 5:
                break

            print('Number is ' + str(number))
    
    def B(self):
        number = 0
        for number in range(10):
            if number == 5:
                pass

            print('Number is ' + str(number))

    def C(self):
        number = 0
        for number in range(10):
            if number == 5:
                continue

            print('Number is ' + str(number))

def main():
    check = EvaluateOutput()
    print("checking A......")
    print(check.A())
    print("checking B.........")
    print(check.B())
    print("checking C.......")
    print(check.C())

if __name__ == '__main__':
    main()