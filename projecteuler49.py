import sympy
import itertools
c=set()
for i in sympy.primerange(1000,3341):
    y=itertools.permutations(str(i))
    for a in y:
        b=int("".join(a))
        if sympy.isprime(i) and sympy.isprime(i+3330) and sympy.isprime(i+6660) and set(str(i))==set(str(i+3330)) and set(str(i))==set(str(i+6660)):
            c.add(i)
print(c)