#!/usr/bin/env python3
amount = float(input("Enter amount: "))
inrate = float(input("Enter interest rate: "))
period = int(input("Enter period: "))
value = 0
year = 1
while year <= period:
    value = amount + (inrate*amount)
    print("year {} Rs. {:.2f}".format(year,value))
    amount = value
    year += 1
