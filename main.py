

def binary(x):
    # turns a number in a kind of binary representation as a list: 21 -> [1,-1,4,-1,16]

    power=[]
    cnt=0
    while x>0:
        if x%2==1:
            power.append(2**cnt)
        else:
            power.append(-1)
        x=x//2
        cnt+=1
    return power

def gcd(a,b):
    while b:                # loop until b is 0
        rest= a%b
        a=b
        b=rest
    return a

def repeated_squaring(b,n,k):
    a=1
    if k == 0:
        return a
    c=b
    power=binary(k)
    if power[0]==1:                             # if k odd
        a=b                                     #special case: add b^1 to rezult
    for i in range(1, len(power)):
        c =(c**2)%n                             #we calculate b^(2^x)%n
        if power[i]!=-1:                        #if the power of 2 is in k's binary repr save it
            a = (c*a)% n
    return a


def is_good_base(b):
    if repeated_squaring(b,n,n-1)==1 and gcd(b,n)==1:                # if b^(n-1) = 1 (mod n) and ...
        return True
    else:
        return False

bases=[]
n=int(input("n= "))
for b in range(1,n):
    if is_good_base(b):
        bases.append(b)

print("The bases with respect to which " + str(n) + " is pseudoprime are: ")

print(bases)
