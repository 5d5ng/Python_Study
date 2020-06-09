print('python','java',sep=",",end="?")
print('무엇이 더 재밌을까요???') 

import sys
print('python','java',file = sys.stdout) #표준 출력으로 처리
print('python','java',file = sys.stderr) #표준 에러로 처리


#시험 성적
scores = {"수학":0,"영어":50,"코딩":100}
#items()는 키 벨류 쌍으로 튜플로 보내줌


#정형화된 포맷으로 출력하기
for subject,score in scores.items():
    #print(subject,score)
    print(subject.ljust(8),str(score).rjust(4),sep=":" ) #subject 왼쪽으로 정렬을 하되 8글자의 공간을 확보해달라는 의미
                                  #score 오른쪽으로 공간 4개주고 정렬  

#은행 대기 순번표 001 002 003 0채우기
for num in  range(1,21):
    print('대기번호:'+str(num).zfill(3))

# zfill(n) n번자리를 주고 남는 앞자리 0으로채움


answer = input("아무 값이나 입력하세요: ")
print(type(answer))
print("입력하신 값은 "+answer +"입니다.")
