#Beginning of Sieve of Erastothenes
n = 7927

potential_primes = [True for i in range(n+1)]

p = 2

while (p * p <= n+1):
    if (potential_primes[p]):
        #If potential_primes[p] is True, then this is executed and all the multiples of p is updated to reflect that they are not prime
        for i in range(p * 2, len(potential_primes), p):
            potential_primes[i] = False
    p += 1

primes = []

for p in range(2, n+1):
    if (potential_primes[p]):
        primes.append(p)
#End of Sieve of Erastothenes

sum_of_primes = sum(primes)
print(sum_of_primes)
