
#파일 쓰기
score_file = open("score.txt","w",encoding="utf8") #파일을 쓸때 w 인코딩은 utf-8로
print("수학 : 0",file=score_file)
print("영어 : 50",file=score_file)
score_file.close()

#파일 이어쓰기
score_file = open("score.txt","a",encoding="utf8") # 기존에 있는파일에 이어쓰기 append의 a
score_file.write("과학 :80")
score_file.write("\n코딩 :100")


#파일 읽어오기
score_file = open("score.txt","r",encoding="utf8")
print(score_file.read())
score_file.close()

#한줄 한줄 불러서 처리하고 싶을 때
score_file = open("score.txt","r",encoding="utf8")
print(score_file.readline(),end="") #줄별로 읽기,한줄 읽고 커서는 다음 줄로 이동
print(score_file.readline(),end="")
print(score_file.readline(),end="")
print(score_file.readline(),end="")
score_file.close()


#파일이 총 몇 줄 인지 모를떄
score_file = open("score.txt","r",encoding="utf8")
while True:
    line = score_file.readline()
    if not line:
        break
    print(line,end="")
score_file.close()

#리스트에 값을 다 넣고 처리할때
score_file = open("score.txt","r",encoding="utf8")
lines = score_file.readlines() #list형태로 저장
for line in lines:
    print(line,end="")

score_file.close()

