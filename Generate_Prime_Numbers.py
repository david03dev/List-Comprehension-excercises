#Task 5: Generate Prime Numbers

#Write a list comprehension to generate all prime numbers between 1 and 50
#[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

#function to find prime number
def find_prime(n):
    if n <=1:
        return False
    for x in range(2,int(n**0.5)+1):
        if n % x == 0:
            return False
    return True
    

res = [x for x in range(1,50) if find_prime(x)]
print(res)
