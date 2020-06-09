cabinet ={3:"유재석",100:"김태호"}
print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3))
print(cabinet.get(5)) #없는 키를 넣으면  get은 None 대괄호는 오류 발생

#None 말고 디폴트 값을 주려면
print(cabinet.get(5,'사용가능'))
print(3 in cabinet) #True
print(5 in cabinet) #False

cabinet ={"A-3":"유재석" , "B-30":"김태호"}
print(cabinet["A-3"])
print(cabinet.get("B-30"))
# 새 멤버 추가
print(cabinet)
cabinet["C-20"] = "조세호"
cabinet["A-3"] = "김종국"
print(cabinet)

del cabinet["A-3"] #키 삭제 가능
print(cabinet)

#key들 만 출력
print(cabinet.keys())
#value만 출력
print(cabinet.values())
# key-value 쌍 출력
print(cabinet.items())

#초기화
cabinet.clear();
print(cabinet);
