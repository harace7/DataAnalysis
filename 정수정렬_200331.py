"""#a,b,c 정수 정렬
a=int(input('숫자1 '))
b=int(input('숫자2 '))
c=int(input('숫자3 '))

print('정렬전 :',a,b,c)

if(a>b):
    a,b = b,a
if(b>c):
    b,c = c,b
if(a>b):
    a,b = b,a

print('정렬후 :',a,b,c,)
"""

#a,b,c,d 정수 정렬
a=int(input('숫자1 '))
b=int(input('숫자2 '))
c=int(input('숫자3 '))
d=int(input('숫자4 '))

print('정렬전 :',a,b,c,d)

if(a>b):
    a,b = b,a
if(b>c):
    b,c = c,b
if(c>d):
    c,d = d,c

if(b>c):
    b,c =c,b
if(a>b):
    a,b = b,a


print('정렬후 :',a,b,c,d)
