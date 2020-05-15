# Erastothenes Sieve
# Time complexity: O{sqrt(N)}

def primes(N):
    count=0
    i = 2
    elements = [1]*(N+1)
    elements[0]=0
    elements[1]=0
    result=[]
    while( i*i<=N ):
        if(elements[i]):
            j=i*i
            while(j<=N):
                elements[j]=0
                j+=i
        i+=1
    for i in range(len(elements)):
        if(elements[i]==1):
            result.append(i)
    return result
    
N=int(input('enter some number'))
print(primes(N))
