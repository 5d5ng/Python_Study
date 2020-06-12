
class House:
    def __init__(self,location,house_type,deal_type,price,completion_year):
        
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year

    def show_detail(self):

        print(self.location,self.house_type,self.deal_type,self.price,self.completion_year)

house = []
b1 = House('강남','아파트','매매','10억','2020년')
b2 = House('부산','주택','매매','13억','2020년')
b3 = House('해운대','아파트','매매','122억','2020년')
house.append(b1)
house.append(b2)
house.append(b3)

print('총 매물{}'.format(len(house)))
for i in house:
    i.show_detail()
