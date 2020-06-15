# import theater_module #폴더내에 있는 모듈 사용
# theater_module.price(3)
# theater_module.price_morning(4)
# theater_module.price_soldier(5)

# import theater_module as mv # as 명령어로 로 줄여서 사용가능
# mv.price(3)
# mv.price_morning(4)
# mv.price_soldier(5)

from theater_module import *
#from random import *
price(3)
price_morning(4)
price_soldier(5)

from theater_module import price,price_morning #  theater_module 내에서 price,price_moring 모듈만 사용하겠다는 의미
from theater_module import price_soldier as price #price_soldier를 price라는 이름으로 사용

