class Unit:#객체
    def __init__(self,name,hp,damage):
        self.name = name
        self.hp = hp 
        self.damage = damage
        print("{0} 유닛이 생성되었습니다.".format(self.name))
        print("체력 {},공격력 {}".format(self.hp,self.damage))

#레이스 : 공중유닛, 비행기.클로킹 스킬을 갖고있다.
wraith1 = Unit("레이스",80,5)
print('유닛이르:{}, 공격력:{}'.format(wraith1.name,wraith1.damage))

#마인드 컨트롤 스킬
wraith2 = Unit("빼앗은 레이스",80,5)
wraith2.clocking = True # 파이썬에서는 객체에 추가로 변수를 만들어서 사용하는 것이 가능하다.(중요!)

if wraith2.clocking ==True:
    print('{}는 현재 클로킹 상태 입니다.'.format(wraith2.name))
