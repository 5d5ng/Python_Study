from random import *
list = []
for i in range(50):
    list.append(randint(5,50))
cnt = 0 #총 탑승승객 수
client = 0
for i in list:
    cnt+=1
    if(i<=15):
        print('[O]{0}번쨰 손님 (소요시간:{1}분)'.format(cnt,i))
        client+=1
    else:
        print('[ ]{0}번쨰 손님 (소요시간:{1}분)'.format(cnt,i))

print('총 탑승 승객: {} 분'.format(client))