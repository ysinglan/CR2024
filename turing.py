def decomposer_turing(n):
    if n<100 or n>999:
        rep=None
    else :
        u=n%10
        d=int(n/10)%10
        c=int(n/100)%10
        rep=(c,d,u)
    return rep

def somme(c,d,u):
    if c>9 or c<0 or d>9 or c<0 or u>9 or u<0: 
        rep=None
    else:
        rep=c+u==d
    return rep


def divisible_turing(n):
    return n%9==0

def devine():
    code=100
    trouve=False
    while code <=999 and not trouve:
        (c,d,u)=decomposer_turing(code)
        if somme(c,d,u) and divisible_turing(code):
            trouve=True
        else: code=code+1
    return code

print(devine())