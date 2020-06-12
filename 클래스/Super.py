
#일반 유닛
class Unit:#객체
    def __init__(self,name,hp):
        self.name = name
        self.hp = hp 


#건물
class BuildingUnit(Unit):
    def __init__(self,name,hp,location):
        # Unit.__init__(self,name,hp)
        super().__init__(name,hp)#super를 쓸때는 ()쓰고 self를 넣지 않는다.
        self.location = location