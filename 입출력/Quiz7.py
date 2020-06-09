#1주차 부터 50주차 까지 보고서 양식 txt파일 만드는 프로그램

for i in range(1,51):
    with open(str(i)+"주차.txt","w",encoding="utf8") as study_file:
        study_file.write("-{}주차 주간보고-".format(i))
        study_file.write("\n부서:")
        study_file.write("\n이름:")
        study_file.write("\n업무요약:")