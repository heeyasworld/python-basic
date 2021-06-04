class Unit:
    def __init__(self):
        print("Unit 생성자")


class Flyable:
    def __init__(self):
        print("Flayble 생성자")


class FlyableUnit(Unit, Flyable):  # 다중상속
    def __init__(self):
        # 다중상속을 할 때, super()를 쓰면, 앞에 상속한 처음 클래스 Unit에 대한 __init__함수만 호출됨.
        # super().__init__()
        Unit.__init__(self)
        Flyable.__init__(self)
        # 그래서 다중상속할 때는 이렇게 super() 말고 따로 빼서 써주기


# 드랍쉽
dropship = FlyableUnit()
