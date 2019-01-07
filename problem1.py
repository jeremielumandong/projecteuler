"""
 Multiples of 3 and 5
 
 If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
 Find the sum of all the multiples of 3 or 5 below 1000.

"""

def multiple(multiples, max):
    num = 0
    arrMutiples = set()
    while(num < max):
        for multi in multiples:
            if(num % multi == 0):
                arrMutiples.add(num)
        num+=1
    total = sum(arrMutiples)
    return total         

print(multiple([3,5], 1000))
