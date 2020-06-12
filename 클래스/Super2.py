class Unit:
    def __init__(self):
        print('unit생성자')

class Flyable:
    def __init__(self):
        print('Flyable생성자')

class FlyableUnit(Unit,Flyable):
    def __init__(self):
        super().__init__()

#두 개 이상의 부모클래스를 다중 상속을 받게 되고 super를 이용하여 생성자를 호출한 경우 맨 처음 클래스에 대해서만 생성자가 호출된다.
# 이런 상황을 막으려면 super를 쓰지않고 부모 클래스 이름을 명시해주어야한다.
#드랍쉽
dropship = FlyableUnit()