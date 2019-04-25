
def gcd(p, q):
  if q == 0:
    return p
  return gcd(q, p % q)

def eat_count(N, M):
  x=0
  choc_step=gcd(N,M)
  x=int( N/choc_step)
  return x
  
