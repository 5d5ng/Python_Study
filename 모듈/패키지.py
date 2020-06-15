#신규여행사 
# import travel.thailand
# trip_to = travel.thailand.ThailandPackage()
# trip_to.detail()

# from travel import vietnam
# trip_to2 = vietnam.VietnamPackage()
# trip_to2.detail()

#__all__
from travel import * 
trip_to2 = thailand.ThailandPackage()
trip_to2.detail()

##파이썬 모듈 위치 확인
import inspect 
import random
print(inspect.getfile(random))  #random모듈이 있는 위치 경로 출력
print(inspect.getfile(thailand))  #thailand모듈이 있는 위치 경로 출력