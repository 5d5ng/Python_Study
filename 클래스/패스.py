
#일반 유닛
class Unit:#객체
    def __init__(self,name,hp):
        self.name = name
        self.hp = hp 


#건물
class BuildingUnit(Unit):
    def __init__(self,name,hp,location):
        pass #그냥 넘어가라는 의미

supply_depot =BuildingUnit("서플라이 디폿",500,'7시')


def game_start():
    print('[알림] 새로운 게임을 시작합니다.')

def game_over():
    pass

game_start()
game_over()