import pickle

with open ("profile.pickle","rb") as profile_file: # 파일정보를 profile_file이라는 변수에 저장
    print(pickle.load(profile_file))

# with 문은 close()필요없이 불러온 파일을 자동으로 종료시켜준다

#pickle이 아닌 일반적인 파일입출력 with as문 사용
with open("study.txt","w",encoding="utf8") as study_file:
    study_file.write("파이썬을 열심히 공부하고 있어요")

with open("study.txt","r",encoding="utf8") as study_file:
    print(study_file.read())