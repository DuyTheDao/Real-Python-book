# exponent.py - Real Python Course
# P. 48
# Python 3.6
# Duy Dao

base = input("Enter a base: ")
exponent = input("Enter an exponent: ")
result = float(base) ** float(exponent)
print ("{b} to the power of {e} is {ans}".format(b=base, e=exponent, ans=result))
