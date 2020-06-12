from random import *
#일반 유닛
class Unit:#객체
    def __init__(self,name,hp,speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        print('{} 유닛이 생성되었습니다.'.format(name))

    def move(self,location):
        print('[지상 유닛 이동]')
        print('{}:{}방향으로 이동합니다.[속도{}]'\
            .format(self.name,location,self.speed)) 

    def damaged(self,damage):
        print('{}:{}데미지를 입었습니다.'.format(self.name,damage))
        self.hp-=damage
        print('{}:현재 체력은 {}입니다.'.format(self.name,self.hp))
        if self.hp<=0:
            print('{}: 파괴되었습니다.'.format(self.name))



#공격 유닛 -일반 유닛 클래스로 부터 상속받음
class AttackUnit(Unit): 
    def __init__(self,name,hp,speed,damage):
        Unit.__init__(self,name,hp,speed) #일반 유닛객체로부터 생성자 가져옴
        self.damage = damage


    def attack(self,location):
        print("{}유닛이 {}시 방향으로 적군을 공격합니다. 공격력은 {}입니다.\
        ".format(self.name,location,self.damage))



#날 수 있는 기능을 가진 클래스
class Flyable:
    def __init__(self,flying_speed):
        self.flying_speed = flying_speed

    def fly(self,name,location):
        print("{0} :{1} 방향으로 날아갑니다.[속도{2}]"\
            .format(name,location,self.flying_speed))

#공중 공격 유닛 클래스 두개의 클래스로 부터 상속받은 것 
class FlyableAttackUnit(AttackUnit,Flyable):
    def __init__(self,name,hp,damage,flying_speed):
        AttackUnit.__init__(self,name,hp,0,damage) #지상스피드를 0으로 넣어줌 
        Flyable.__init__(self,flying_speed)
    
    def move(self,location): #메소드 오버라이딩 이용
        print('[공중유닛 이동]')
        self.fly(self.name ,location)



#마린 클래스
class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self,'마린',40,1,5)

    #스팀팩: 일정 시간 동안 이동 및 공격 속도를 증가, 체력 10 감소
    def stimpack(self):
        if(self.hp>10):
            self.hp -= 10
            print('{}: 스팀팩을 사용합니다.(HP감소)'.format(self.name))
        else:
            print("{}: 체력이 부족하여 스팀팩을 사용하지 않습니다.".format(self.name))

class Tank(AttackUnit):

    seize_developed = False

    def __init__(self):
        AttackUnit.__init__(self,'탱크',150,1,35)
        self.seize_mode = False;

    def set_seize_mode(self):
        if Tank.seize_developed == False:
            return

        #현재 시즈모드 동작 중일때와 아닐 때가 있음
        if self.seize_mode == False:
            print('{}:시즈모드로 전환합니다.'.format(self.name))
            self.damage *=2
            self.seize_mode = True
        
        else:
            print('{}:시즈모드를 해제합니다.'.format(self.name))
            self.damage /=2
            self.seize_mode = False



class Wraith(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__(self,'레이스',80,20,5)
        self.clocked = False #클로킹 모드 (해제)

    def clocking(self):
        if(self.clocked == True):
            print('클로킹 모드를 해제합니다.')
            self.clocked = False
        else:
            print('클로킹 모드를 설정합니다.')
            self.clocked = True


def game_start():
    print('[알림] 새로운 게임을 시작합니다.')

def game_over():
    print("Player:gg")
    print("[Player] 님이 게임에서 나갔습니다.")





#실제 게임 진행
game_start()

#마린 3개
m1 = Marine()
m2 = Marine()
m3 = Marine()

#탱크 3개
t1 = Tank()
t2 = Tank()
t3 = Tank()

#레이스
w1 = Wraith()


#유닛 일관 관라
attack_units = []
attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(t2)
attack_units.append(t3)
attack_units.append(w1)



# 전군 이동
for unit in attack_units:
    unit.move('1시')

#탱크 시즈모드 개발
Tank.seize_developed = True
print('탱크 시즈모드 개발 완료!')

#공격 모드 준비
for unit in attack_units: 
    #  이 객체가 특정 클래스의 인스턴스인지 확인하는 함수
    if isinstance(unit,Marine):
        unit.stimpack()

    elif isinstance(unit,Tank):
        unit.set_seize_mode()
    elif isinstance(unit,Wraith):
        unit.clocking()


#전군 공격

for unit in attack_units:
    unit.attack('1시')

# 전군 피해

for unit in attack_units:
    unit.damaged(randint(5,20))# 5-20 중 랜덤으로 공격받음 

#게임 종료
game_over()