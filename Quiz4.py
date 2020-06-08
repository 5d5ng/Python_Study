from random import *

lst = range(1,21) #1부터 20까지 숫자를 생성
lst = list(lst) #리스트로 타입 변환

shuffle(lst)
print(lst)

winner = sample(lst,4)
print(type(winner))

print('치킨 당첨자:{0}'.format(winner[0]))

print('커피 당첨자:{0}'.format(winner[1:]))
