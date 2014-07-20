import math

__author__ = 'richleung'
__project__ = 'Finding prime numbers using Sieve of Eratosthenes'


def FindPrime (n):
    # Initialize array.  Value as false (0) represent not prime number, value as true (1) represents prime number
    prime = []
    Prime_Set = set()
    UsrDefinedLen = range(0, n+1)
    for i in UsrDefinedLen:
        prime.append(i)

    # Since 0 and 1 is not a prime number...
    prime[0] = 0
    prime[1] = 0

    sqrt_n = math.sqrt(n)
    Limit = int(math.floor(sqrt_n))
    for i in xrange(2, Limit+1):
        if prime[i]:
            for j in xrange(int(math.pow(i,2)), n+1, i):
                prime[j] = 0

    for i in UsrDefinedLen:
        if prime[i] != 0:
            Prime_Set.add(prime[i])

    return Prime_Set

x = FindPrime(100)
print x