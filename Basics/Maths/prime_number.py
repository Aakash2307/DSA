#  we will check if a number is prime or not

n = 29

#  a prime number is a number that is only divisible by 1 and itself
#  The below are the edge cases for prime numbers

if n <=1 :
    print(f"{n} is not a prime number")

if n == 2 :
    print(f"{n} is a prime number")

if n == 3 :
    print(f"{n} is a prime number")

for i in range(3 , int(n**0.5) + 1 , 2) : # we can skip even numbers greater than 2
    if n % i == 0 :
        print(f"{n} is not a prime number")
        break
else :    print(f"{n} is a prime number")