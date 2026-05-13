#  the code helps to find the greatest common divisor of two numbers using Euclidean algorithm

def find_gcd(a,b):
    while b != 0 :
        a,b = b , a%b
    return a 

# let me understand you with an example 48 and 18

n1 , n2 = 48 , 18
gcd = find_gcd(n1,n2)
print(f"The greatest common divisor of {n1} and {n2} is {gcd}")