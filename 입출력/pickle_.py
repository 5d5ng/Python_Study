# Pickle 사용하는데이터를 파일형태로 저장하는 것 
import pickle
#쓰기
profile_file = open("profile.pickle","wb") #파일을 열땨는 쓰기(w) 목적으로 바이너리타입 정의(b)
profile = {"이름":"박명수","나이":30,"취미":["축구","골프","코딩"]}

print(profile)
pickle.dump(profile, profile_file) #profile에 있는 정보를 file 에 저장
profile_file.close()


#읽기
profile_file = open("profile.pickle","rb") #파일을 열땨는 쓰기(w) 목적으로 바이너리타입 정의(b)
profile = pickle.load(profile_file)
print(profile)
profile_file.close()
