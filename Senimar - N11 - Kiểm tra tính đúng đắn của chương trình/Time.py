def time(s):
    h,m,s=s.split(':')
    s1=s[:2]
    if int(h)<0 or int(h)>12 or int(h)<0 or int(h)>59 or int(s1)<0 or int(s1)>59  or (int(h)==0 and s[2:]=='PM'):
        return "Error"
    else:
        if s[2:]=='PM' and h!='12':
            h=str(int(h)+12)
        if s[2:]=='AM' and h=='12':
            h='00'
        if s[2:]=='PM' and h=='12':
            h='12'
    conv_time=h+':'+m+':'+s[0:2]
    return conv_time

s=str(input())
print(time(s))