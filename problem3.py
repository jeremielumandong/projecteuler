"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""
import math

def primeFactors(n):
    primeValues = []
    while(n % 2 == 0):
        primeValues.append(2)
        n = n / 2
    
    for i in range(3, int(math.sqrt(n))+ 1, 2):
        while(n % i == 0):
            primeValues.append(i)
            n = n / i
    
    if(n> 2):
        primeValues.append(2)

    return primeValues

print(max(primeFactors(600851475143)))