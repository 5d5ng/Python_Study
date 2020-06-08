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