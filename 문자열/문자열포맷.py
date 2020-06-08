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