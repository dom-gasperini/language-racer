# Dominic Gasperini
# Python Prime Sieve

# --- imports --- #
import sys
import math


def isPrime(number: int) -> bool:
    if number == 2:
        return True

    # catch early primes and eliminate all numbers divisable by 2
    if number < 2 or number % 2 == 0:
        return False

    # if the number is larger 
    i = 3
    while (i*i) < number:
        if number % i == 0:
            return False
        i += 2
    
    # otherwise the number is prime!
    return True


def primeCheck(primes: list) -> bool:
    # if a number is marked as prime, ensure it is in fact prime
    for i in range(len(primes) - 1):
        if primes[i]:
            if not isPrime(i):
                return False
    
    return True



def primeSieve(size: int, prime_storage: list) -> list:
    prime_storage[0] = False
    prime_storage[1] = False

    smaller_limit = int(math.sqrt(size)) + 1
    for i in range(3, smaller_limit):
        if prime_storage[i]:
            for j in range(i * i, size + 1, i):
                prime_storage[j] = False
    
    return prime_storage


# main!
def main():
    # get command line arguments 
    size = sys.argv[1]
    pass_count = sys.argv[2]

    # convert to ints
    size = int(size)
    pass_count = int(pass_count)

    prime_storage = [True for _ in range(size + 1)]

    for _ in range(pass_count):
        # reset array 
        for number in range(len(prime_storage)):
            prime_storage[number] = True

        # run sieve
        prime_storage = primeSieve(size, prime_storage)
        
    
    # check the fresh array for invalid results
    if not primeCheck(prime_storage):
        exit(-1)


# run it!
main()