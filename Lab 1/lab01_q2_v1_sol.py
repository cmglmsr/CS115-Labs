# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 04:13:46 2022

"""

# Input data
total_price = int(input('Enter total project price (USD): '))
completion_rate = float(input('Enter completion percentage: '))
overdue_days = int(input('Enter number of days overdue: '))

# calculate penalty per day
penalty_per_day = 0.05 * total_price

# Calculate payment
if completion_rate >= 90:
    payment = total_price  
else:
    payment = total_price  * completion_rate / 100

if overdue_days > 1:
    payment = payment - penalty_per_day * overdue_days

# display results
print(f"Payment earned is {payment:.2f} USD")
print(f"This is {payment/total_price*100:.1f}% of {total_price} USD")
