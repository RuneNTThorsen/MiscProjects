This was a fun one. It was originally a request from a company that I applied to. They wanted a CV that included a lot of standard things and then also the sum of the first 1001 primes. I'm still not even sure if they actually wanted to see it or if it was just a joke. It could potentially be serious, because it could serve as a sort of test to see if people applying actually can program and make efficient programs as well as have the necessary knowledge for the job.

Anyway the script here uses the Sieve of Erastothenes to find and mark primes. Initially it assumes that all possible numbers are primes and then weeds out non-primes iteratively. Lastly the sum of all the primes are found.

The number "7927" might seem arbitrary. This was found through trial and error, until the "primes" list contained exactly 1001 elements after which the last element was printed out. I then just set this as the upper limit to which primes were to be found. This limit can of course be set higher or lower.

A better course of action (regarding all sorts of different good code styles and principles) might have been to actually compartmentalize things into functions and so on and so forth, but as this is a very small project, I didn't want to bother and just allowed it to be a small script.

If someone wants to reuse the code, I marked where the part involving the Sieve of Erastothenes starts and ends with some comments.
