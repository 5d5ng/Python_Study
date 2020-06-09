gun = 10

def checkpoint(soldiers): #경계근무   
    global gun # 전역 공간에 있는 gun을 사용하겠다는 의미 즉 위에 선언해놓은 gun 변수를 사용한다는 의미
    gun = gun - soldiers
    print("[함수 내] 남은 총:{0}".format(gun))

def checkpoint_ret(gun,soldiers): #전역변수를 사용하지 않고 매개변수로 전달하는 경우
    gun = gun - soldiers
    print("[함수 내] 남은 총:{0}".format(gun))
    return gun

print("전체 총 :{0}".format(gun))
# checkpoint(2)
gun = checkpoint_ret(gun,2)
print("남은 총 :{0}".format(gun))
