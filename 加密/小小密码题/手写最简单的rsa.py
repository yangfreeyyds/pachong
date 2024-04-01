import gmpy2
from Crypto.Util.number import long_to_bytes


n = p*q
phin = (p-1)*(q-1)
e=37777
d = gmpy2.invert(e,phin)
m = int(pow(c,d,n))

print(long_to_bytes(m))
