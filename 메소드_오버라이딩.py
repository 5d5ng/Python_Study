#일반 유닛
class Unit:#객체
    def __init__(self,name,hp,speed):
        self.name = name
        self.hp = hp
        self.speed = speed

    def move(self,location):
        print('[지상 유닛 이동]')
        print('{}:{}방향으로 이동합니다.[속도{}]'\
            .format(self.name,location,self.speed)) 


#공격 유닛 -일반 유닛 클래스로 부터 상속받음
class AttackUnit(Unit): 
    def __init__(self,name,hp,speed,damage):
        Unit.__init__(self,name,hp,speed) #일반 유닛객체로부터 생성자 가져옴
        self.damage = damage


    def attack(self,location):
        print("{}유닛이 {}시 방향으로 적군을 공격합니다. 공격력은 {}입니다.\
        ".format(self.name,location,self.damage))

    def damaged(self,damage):
        print("{}:{} 데미지를 입었습니다.".format(self.name,damage))
        self.hp-=damage
        print('{0}:현재 체력은 {1}입니다.'.format(self.name,self.hp))
        if self.hp <= 0:
            print('{}:파괴되었습니다.'.format(self.name))

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

#벌쳐 :지상 유닛, 기동성이 좋음
vulture = AttackUnit('벌처',80,10,20)

#배틀 크루저
battlecruiser = FlyableAttackUnit("배틀크루저",500,25,3)

vulture.move("11시")
# battlecruiser.fly(battlecruiser.name,"9시")
battlecruiser.move("9시")


