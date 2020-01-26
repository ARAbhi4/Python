"""
Created on Fri Jan 26 2020

@author: ARAbhi

Leap Year
    A normal year has 365 days.
    A Leap Year has 366 days (the extra day is the 29th of February).

"""

data = int(input("Enter Year: "))


if data%4 == 0 and (data%100 != 0 or data%400 == 0):
	print("Leap Year")
else:
	print("Normal Year")





