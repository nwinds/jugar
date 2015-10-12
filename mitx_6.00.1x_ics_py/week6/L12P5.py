def genPrimesFirstEd():
    primes = [2]
    while True:
        for num in range(primes[-1]+1, primes[-1]**2):
            try:
                for p in primes:
                    if (num % p) == 0:
                        raise Exception
                next = primes[-1]
                yield next
                primes.append(num)
            except Exception:
                continue
 
def genPrimes():
    primes = [2]
    num = 2
    while True:
        num += 1
        try:
            for p in primes:
                if (num % p) == 0:
                    raise Exception
            next = primes[-1]
            yield next
            primes.append(num)
        except Exception:
            continue
         
#test: use assert to prevent overflow
for n in genPrimes():
    print(n)
    assert n < 10
    
    
#the following is the answer provided by mooc
# Note that our solution makes use of the for/else clause, which 
# you can read more about here:
# http://docs.python.org/release/1.5/tut/node23.html 

def genPrimesRefAnswer():
    primes = []   # primes generated so far
    last = 1      # last number tried
    while True:
        last += 1
        for p in primes:
            if last % p == 0:
                break
        else:
            primes.append(last)
            yield last
