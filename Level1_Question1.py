def simple_interest(p, t, r):
    si = (p*t*r)/100
    return si

principle_amount = int(input())
rate = float(input())
time = int(input())

print(simple_interest(principle_amount, time, rate)