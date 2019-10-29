import sys

def sieve(n):
    """
    Return a list of all primes less than n
    """
    
    prime = [True for i in range(n+1)]
    p=2

    while(p**2 <= n):
        if prime[p]==True:
            for i in range(p*2, n+1, p):
                prime[i]=False
        p+=1    
    
    list = []
    for p in range(2, n+1):
        if prime[p]:
            list.append(p)

    return list



if __name__=='__main__':
    if len(sys.argv)==2:
        print(sieve(int(sys.argv[1])))
    else:
        print("Missing one required argument.")