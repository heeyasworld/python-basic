# import theater_module
# theater_module.price(3)  # 3명 영화보러 갈 때 가격
# theater_module.price_morning(4)
# theater_module.price_solider(5)

# import theater_module as mv # 모듈명 별명화해서 짧게 사용 가능
# mv.price(3)
# mv.price_morning(4)
# mv.price_solider(5)

# from theater_module import *  # 이 모듈에 있는 모든 것을 사용하겠다
# price(3)
# price_morning(4)
# price_solider(5)

# from theater_module import price, price_morning
# price(5)
# price_morning(6)
# price_solider(7)  # 이 부분 임포트 안해서 쓸 수 없고 오류난다

# from theater_module import price_solider as price
# # theater_module이라는 모듈에서 price_soldier라는 함수를 가져다 쓰는데 price라고 별명붙여서 쓰겠음
# price(5)  # 이때는 원래 일반가격인 price 아닌 것!

# package

# import travel.vietnam
# import travel.thailand  # travel 폴더에서 thailand.py 임포트
# thailand 자리에는 모듈이나 패키지만 쓸 수 있고
# 함수, 클래스 등은 저 자리에 못 넣는다
# trip_to = travel.thailand.ThailandPackage()  # 해당 클래스 변수 저장
# trip_to.detail()
# # travel.thailand.ThailandPackage().detail() 위와 동일

# travel.vietnam.VietnamPackage().detail()


# from travel.thailand import ThailandPackage
# # from ~ import~ 로는 클래스 위처럼 바로 임포트 가능
# trip_to = ThailandPackage()
# trip_to.detail()
# ThailandPackage().detail() # 위와 동일


# from travel import vietnam
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()


# all

# from travel import *
# # trip_to = vietnam.VietnamPackage()
# trip_to = thailand.ThailandPackage()
# trip_to.detail()


# 모듈 직접 실행

# 패키지, 모듈 위치 확인하기
from travel import *
import inspect
# import random
# print(inspect.getfile(random))

print(inspect.getfile(thailand))
print(inspect.getfile(vietnam))

# pip install
