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