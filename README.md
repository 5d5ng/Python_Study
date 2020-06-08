

# Python

[TOC]



# 숫자 자료형

```python
print('ss')

animal = "강아지"
age = 4
is_adult = age >= 3

print("우리집"+animal+"는"+str(age)+"살")
print(animal, "는", age, "살")  # ,를 이용하면 빈칸이 들어간다.
print("우리집 강아지는 어른인가요? " + str(is_adult))
# station = input()

# print(station, "행 열차가 들어오고 있습니다.")
```

# 연산

```python
print(1+1)
print(3-2)
print(5*2)
print(6/3)

print(2**3)  # 2^3
print(5 % 3)
print(10 % 3)
print(10//3)
print(5//3)

print(3 == 3)
print(3+4 == 7)
print(3 != 4)

print((3 > 0) and (3 < 5))
print((3 > 0) & (3 < 5))

print((3 > 0) or (3 > 5))
print((3 > 0) | (3 < 5))

print(5 > 4 > 3)
print(5 > 4 > 7)
```

# 수식 연산

```python
print(2+3*4)
print((2+3) *4)
number = 2+3*4

print(abs(-5))
print(pow(4,2))
print(max(5,12))
print(min(5,12))
print(round(3.14))#반올림
print(round(4.99))

from math import *
print(floor(4.99))
print(ceil(3.14))
print(sqrt(16))
```

# 랜덤함수

```python
from random import *

# print(random()) #0.0~1.0 미만의 임의의 값 생성
# print(random()*10) #0.0 부터 10.0 미만의 임의의 값 생성
# print(int(random()*10))
# print(int(random()*10))
# print(int(random()*10))
# print(int(random()*10)+1)#1부터 10이하의 임의의 값

# print(int(random()*45)+1)#1-45 이하의 임의의 값 생성
# print(int(random()*45)+1)#1-45 이하의 임의의 값 생성
# print(int(random()*45)+1)#1-45 이하의 임의의 값 생성

# print(randrange(1,46)) # 1-45까지 임의의 값 생성

# print(randint(1,45)) # 1-45까지의 임의의 값 생성

print("오프라인 스터디 모임 날짜는 매월 "+str(randint(4,28))+"일로 선정되었습니다.")

lst = range(1,21) #1부터 20까지 숫자를 생성
lst = list(lst) #리스트로 타입 변환

shuffle(lst)
print(lst)

winner = sample(lst,4)
print(type(winner))

print('치킨 당첨자:{0}'.format(winner[0]))

print('커피 당첨자:{0}'.format(winner[1:]))
```

# 문자열 자료형

```python
sentence ='나는 소년입니다'
print(sentence)
sentence2 = "파이썬은 쉽다"
print(sentence2)
sentence3 = """
나는 소년이고 파이썬은 쉬워요
"""

print(sentence3)
```

# 문자열 포맷

```python
print("a"+"b")
print("a","b")

#방법1
print("나는 %d살입니다." % 20)
print("나는 %s을 좋아해요."% "파이썬")
print("Apple은 %c로 시작해요." % "A")
print("나는 %s색과 %s색을 좋아해요." %("파랑","빨강"))

# 방법2
print("나는 {}살입니다.".format(20))
print("나는 {}색과 {}색을 좋아해요".format("파랑","빨강"))
print("나는 {1}색과 {0}색을 좋아해요." .format("파랑","빨강"))

#방법3
print("나는 {age}살이며,{color} 색을 좋아해요.".format(age=20,color="빨간"))
print("나는 {age}살이며,{color} 색을 좋아해요.".format(color="빨간",age=20))

#방법4 v3.6이상부터 가능
age = 20;
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요")
```

# 슬라이싱

```python
jumin ="901929-1234567"

print("성별 : "+jumin[7])
print("연 : "+jumin[0:2])#0,1번째 출력
print("월 :"+jumin[2:4])
print("일 :"+jumin[4:6])

print("생년월일 :"+jumin[:6]) #처음부터 6직전까지
print("뒤 7자리:"+jumin[7:])
print("뒤 7자리: 뒤에부터"+jumin[-7:])

# 맨 뒤에서 7번쨰부터 끝까지
```

# 문자열 처리 함수

```python
python = "Python is Amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper())

print(len(python))

print(python.count("i")) #문자 내 i개수

print(python.replace("Python","Java")) #문자열 교체

index = python.index("n")

print(index)

index = python.index("n",index+1) #다음에 있는 n위치를 찾도록 하는 것

print(python.find("n")) 
print(python.find("java")) # 못찾을 경우 -1반환 python.index메소드를 이용하면 찾는게 없는 경우에러가 발생
```

# 탈출문자

```python
print("백문이 불여일견 \n 백견이 불여일타")

print('저는 "나도코딩" 입니다.')
print("저는 \"나도코딩\" 입니다.")

# \\ :문장내에서 \

# \r :커서를 맨 앞으로 이동

print("Red Apple\rPine")

#\b :백스페이스 (한글자 삭제)

print("Redd\bApple")

# \t : 탭
print("Red\tApple")
```

# 리스트

```python
#리스트
s1 = 10
s2 = 20
s3 = 30

subway = [10,20,30]
print(subway)

subway = ["유재석","조세호","박명수"]
print(subway)
print(subway.index("조세호"))

#하하 추가
subway.append("하하")
print(subway)

#정형돈을 유재석 조세호 사이에 넣어라
subway.insert(1,"정형돈")
print(subway)

#지하철에 있는 사람을 한명씩 뒤에서 꺼냄
print(subway.pop())
print(subway)

#같은 이름의 사람이 몇명있는지 확인하기
subway.append("유재석")
print(subway)
print(subway.count("유재석"))

#정렬도 가능
num_list = [4,2,1,3,-1]
num_list.sort()
print(num_list)
#순서 뒤집기
num_list.reverse()
print(num_list)

#모두 지우기
num_list.clear()
print(num_list)

#자료형 관계없이 가능
num_list = [4,1,3,1,4]
mix_list = ["조세호",20,True]
print(mix_list)

#리스트 확장 리스트끼리 합치는 것도 가능
num_list.extend(mix_list)
print(num_list)
```

# 튜플

```python
# 내용변경이나 추가를 못하는데 속도가 리스트보다 빠르다
menu = ("돈까스","치즈가스")
print(menu[0])
print(menu[1])

#menu.add("ss") 추가 불가능

# name = "김종국"
# age = 20
# hobby = "코딩"
# print(name,age,hobby)
# 튜플을 이용하면 더 간단하게 표현 가능
name , age, hobby = "김종국", 20,"코딩"
print(name,age,hobby)
```

# 딕셔너리

```python
cabinet ={3:"유재석",100:"김태호"}
print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3))
print(cabinet.get(5)) #없는 키를 넣으면  get은 None 대괄호는 오류 발생

#None 말고 디폴트 값을 주려면
print(cabinet.get(5,'사용가능'))
print(3 in cabinet) #True
print(5 in cabinet) #False

cabinet ={"A-3":"유재석","B-30":"김태호"}
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
```

# 집합

```python
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
```

# If문

```python
weather = "미세먼지"
if weather == "비":
    print('우산을 챙기세요')
elif weather == "미세먼지":
    print('마스크를 챙기세요')
else:
    print('준비물 필요없어요')

temp = int(input("기온은 어때요?"))
if 30<=temp:
    print('너무더워요. 나가지 마세요')
elif 10 <= temp and temp <30:
    print('괜찮은 날씨에요')
elif 0<=temp<10: # and 
    print('외투를 챙기세요')
else:
    print('추워요. 나가지 마세요')
```

# For문

```python
# print("대기번호 :1")
# print("대기번호 :2")
# print("대기번호 :3")
# print("대기번호 :4")

for wating_no in range(1,6): #  1 2 3 4 5
    print("대기번호 :{0}".format(wating_no))

starbucks =["아이언맨","그루트","토르"]

for customer in starbucks:
    print('{0}, 커피가 준비되었습니다.'.format(customer))
```

# While문

```python
#While
customer ="토르"
index = 5
while index >=1:
    print("{0}, 커피가 준비되었습니다. {1}번 남았어요.".format(customer,index))
    index -= 1
    if index == 0:
        print('커피는 폐기처분되었습니다.')

customer = "아이언맨"
# index = 1
# while True:
#     print("{0}, 커피가 준비 되었습니다.".format(customer))
#     index +=1 

customer = "토르"
person = 'Unknown'
while person != customer:
    print("{0},  커피가 준비되었습니다.".format(customer))
    person = input("이름이 어떻게 되세요?")
```