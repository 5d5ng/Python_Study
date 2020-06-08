#Set
#중복안되고 순서가 없다

my_set ={1,2,3,3,3}
print(my_set)

java = {"유재석","김태호","양세형"}
python = set(["유재석","박명수"]) #set으로 감싸줌

# 교집합 출력 즉 자바와 파이썬 둘다 가능한 사람
print(java & python)
print(java.intersection(python))

# 합집합

print(java | python)
print(java.union(python))

#차집합 자바는 할줄 알지만 파이썬을 할 줄 모르는 개발자
print(java - python)
print(java.difference(python))

#python 할 줄 아는 사람 늘어남
python.add("김태호")
print(python)

java.remove("김태호")
print(java)

