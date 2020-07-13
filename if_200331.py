
#if와 else
"""
t=int(input('기온 '))
if t>30: print('날씨가 덥다.')
else: print('날씨가 덥지않다.')
"""

#줄이동시 띄어쓰기 필수
"""
t=int(input('기온 '))
if t>30:
    print('날씨가 덥다.')
else:
    print('날씨가 덥지않다.')

"""

#다중if문 elif
"""
t=int(input('기온 '))
if t>30:
    print('날씨가 덥다.')     
elif t>20:
    print('날씨가 따뜻하다.')  #기온이 20도 초과 30도 이하인경우
elif t>10:
    print('날씨가 시원하다.')
else:
    print('날씨가 춥다.')
"""


#다중if문? 각각비교되는.. if
"""
t=int(input('기온 '))
if t>30:
    print('날씨가 덥다.')
if t>20:
    print('날씨가 따뜻하다.')
if t>10:
    print('날씨가 시원하다.')
else:
    print('날씨가 춥다.')
"""
"""
t=int(input('기온 '))
if t>30:
    print('날씨가 덥다.')
elif t>20:
    print('날씨가 따뜻하다.')
elif t>10:
    print('날씨가 시원하다.')
#else:
#    print('날씨가 춥다.')
""""
