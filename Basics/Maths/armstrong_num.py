#  the code helps to find if a number is an Armstrong number

# An Armstrong number is a number that equals the sum of its own digits each raised to the power of the number of digits.

n = 153

s = str(n)  # convert the number to string to easily access each digit
num_digits = len(s)  # find the number of digits

total  = 0 

for digit in s :
    digit = int(digit) # convert the digit back to integer
    total += digit ** num_digits # raise each digit to the power of the number of digits and add to total

if total == n :
    print(f"{n} is an Armstrong number")
else :
    print(f"{n} is not an Armstrong number")