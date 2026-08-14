#  Printing all the divisors

n = 6 
n = abs(n) # to handle negative numbers
divisors = []

for i in range(1 , int(n**0.5) + 1):
    if n% i == 0 :
        divisors.append(i)
        if i != n //i :
            divisors.append(n//i)

divisors.sort()
print(f"The divisors of {n} are : {divisors}")

# Time Complexity: O(sqrt(n) + k log k), where k is the number of divisors found
# Space Complexity: O(k), for the divisors list
