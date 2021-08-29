name = input('Enter Name: ')
empid = input('Employee id: ')
basic = int(input('Enter basic salary: '))
spl_allowances = int(input('Enter special allowances : '))
bonus  = int(input('Enter bonus percentage: '))
tax_sav_invest = int(input('Enter Monthly tax saving investments: '))

salary_m = bonus + spl_allowances + basic
bonus_money = salary_m * (bonus / 100) * 12 
salary_y = (salary_m * 12) + bonus_money

print('Annual gross salary: ', salary_y)

if tax_sav_invest < 150000:
    if salary_y <= 250000 :
        print('annual net salary ', salary_y)
        print('Tax payable : ', salary_y * 0)
    elif salary_y > 250000 and salary_y <= 500000 :
        print('annual net salary: ', salary_y * 0.95)
        print('Tax payable : ', salary_y * 0.5)
    elif salary_y > 500000 and salary_y <= 1000000 :
        print('annual net salary: ', salary_y * 0.8)
        print('Tax payable : ', salary_y * 0.2)
    else:
        print('annual net salary: ', salary_y * 0.7)
        print('Tax payable : ', salary_y * 0.3)
else:
    if salary_y <= 400000:
        print('annual net salary: ', salary_y)
        print('Tax payable : ', salary_y * 0)
    elif salary_y > 400000 and salary_y <= 500000 :
        print('annual net salary: ', salary_y * 0.95)
        print('Tax payable : ', salary_y * 0.5)
    elif salary_y > 500000 and salary_y <= 1000000 :
        print('annual net salary: ', salary_y * 0.8)
        print('Tax payable : ', salary_y * 0.2)
    else:
        print('annual net salary: ', salary_y * 0.7)
        print('Tax payable : ', salary_y * 0.3)

        
        