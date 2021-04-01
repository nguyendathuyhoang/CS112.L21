def UCLN(a,b):
    a=abs(a)
    b=abs(b)
    if a==0 and b!=0:
        return b
    if a==b:
        return a
    if a>b:
        return UCLN(a-b,b)
    if a<b:
        return UCLN(a,b-a)

def Xuat(a,b,c,d):
    if b==0 or c==0 or d==0:
        return "Error"
    else:
        ts=a*d
        ms=b*c
        gcd=UCLN(ts,ms)
        ts=int(ts/gcd)
        ms=int(ms/gcd)
        if ts==ms:
            return '1'
        elif ts==0:
            return '0'   
        elif ts<0:
            if ms==1:
                return f'{ts:.0f}'
            elif ms==-1:
                return f'{-ts:.0f}'
            elif ms<0:
                return f'{-ts:.0f}/{-ms:.0f}'
            else:
                return f'{ts:.0f}/{ms:.0f}'
        else:
            if ms==1:
                return f'{ts:.0f}'
            elif ms==-1:
                return f'{-ts:.0f}'
            elif ms<0:
                return f'{-ts:.0f}/{-ms:.0f}'
            else:
                return f'{ts:.0f}/{ms:.0f}'
a,b,c,d=map(int,input().split())
print(Xuat(a,b,c,d))