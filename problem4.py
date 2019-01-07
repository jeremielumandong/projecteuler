"""
Largest palindrome product

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

"""

def reversed_string(a_string):
    return a_string[::-1]

def isPalindrome(val):
    reverse = reversed_string(val)
    if(val == reverse):
        return True
    else: 
        return False

def calculateHighestPalindromeProduct():
    x = 999
    y = 999
    palindromes = []
    while(x > 100):
        while(y > 100):
            total = x*y
            # print("{x}*{y} = {total}".format(x=x,y=y, total=total))
            if(isPalindrome(str(total))):
                palindromes.append(total)
            y = y - 1
        x = x - 1
        y = 999
    return palindromes

print(max(calculateHighestPalindromeProduct()))