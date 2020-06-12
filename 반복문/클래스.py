# # 마린 : 공격유닛, 군인, 총을 쏠 수 있음
# name = "마린"
# hp = 40 #체력
# damage = 5 #공격력

# print("{0} 유닛이 생성되었습니다.".format(name))
# print("체력{0}, 공격력{1}\n".format(hp,damage))


# #탱크 : 공격 유닛,탱크 , 포를 쏠 수 있는데,. 일반모드 / 시즈모드

# tank_name = "탱크"
# tank_hp = 150
# tank_damage = 35
# print("{0} 유닛이 생성되었습니다.".format(tank_name))
# print("체력{0}, 공격력{1}\n".format(tank_hp,tank_damage))

# def attack(name,location,damage):#한줄 띄워서 쓸때 \사용
#     print('{}:{} 방향으로 적군을 공격 합니다.\ 
#     [공격력:{}]'.format(name,location,damage))

# attack(name,"1시",damage)
# attack(tank_name,"1시",tank_damage)

# #만약에 탱크나 마린이 100개 더 생성해야 한다면? => 그래서 클래스가 필요하다

class Unit:#객체
    def __init__(self,name,hp,damage):
        self.name = name
        self.hp = hp 
        self.damage = damage
        print("{0} 유닛이 생성되었습니다.".format(self.name))
        print("체력 {},공격력 {}".format(self.hp,self.damage))

marine1 = Unit('마린',40,5)#인스턴스 생성  , self를 제외한 인자들을 다 넣어줘야 생성가능
marine2 = Unit('마린',40,5)
tank = Unit('탱크',150,35)