"""#FOR문
S=0
num=int(input('N='))
for i in range(1,num+1):
      S+=i

print(S)
"""

"""#WHILE문
num=int(input('N='))
S=0
i=1
while i<num+1:
    S+=i
    i+=1

print(S)
"""

"""#홀수출력
num=int(input('N='))
for i in range(1,num+1):
    if(i%2==1):print(i)
"""

"""#홀짝 선택 후 출력
num=int(input('N='))
option=int(input('홀수/짝수 선택(1:홀수, 2:짝수)='))

if(option==1):
    for i in range(1,num+1):
        if(i%2==1):print(i)

elif(option==2):
    for i in range(1,num+1):
        if(i%2==0):print(i)

else:
    print('입력 오류')
"""

#파이썬에서는 들여쓰기 오류(SyntaxError) 조심. 띄어쓰기 들여쓰기 주의.
"""
i=1
while i <= 10:
    if i%2 == 1:
        print(i, end='')
    i+=1
"""
"""
num=0
while num<1:
    print(num,'은 자연수가 아닙니다.')
    num=int(input('자연수 입력='))
    
print(num,'의 모든 약수 :')
for i in range(1, num+1):
    if num%i==0:
         print(i, end=' ')
            
"""
#if와 AND와 OR
a=int(input('a= '))
b=int(input('b= '))
if (a>0 and b>0) or (a<0 and b<0): print('양수')
else: print('음수')

