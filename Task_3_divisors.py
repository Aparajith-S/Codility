def gcf(a,b):
  if b==0:
    return a
  return gcf(b,a%b)

def check(A,B):
  g=gcf(max(A,B),min(A,B))
  while(g!=1):
    g= gcf(max(A,B),min(A,B))
    if g == 1:
      break
    A/=g
  return A==1

def common_div(A, B):
  count = 0
  for i in range(len(A)):
       if((check(A[i],B[i])) and (check(B[i],A[i])) ):
           count+=1
  return count
