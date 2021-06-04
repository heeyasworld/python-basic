# 클래스 : 붕어빵 틀에 비유. 틀은 하나인데 붕어빵은 무한정 만들 수 있다.
# 서로 연관이 있는 변수와 함수의 집합.

# 스타크래프트 예시
# 마린 : 공격 유닛, 군인. 총 쏠 수 있다.
# name = "마린"  # 유닛의 이름
# hp = 40  # 유닛의 체력
# damage = 5  # 유닛의 공격력

# print("{} 유닛이 생성되었습니다.".format(name))
# print("체력 {}, 공격력 {}\n".format(hp, damage))

# # 탱크 : 공격 유닛, 탱크. 포를 쏠 수 있고, 일반 모드, 시즈 모드 두 가지 있음.
# tank_name = "탱크"
# tank_hp = 150
# tank_damage = 35

# print("{} 유닛이 생성되었습니다.".format(tank_name))
# print("체력 {}, 공격력 {}\n".format(tank_hp, tank_damage))

# tank2_name = "탱크"
# tank2_hp = 150
# tank2_damage = 35

# print("{} 유닛이 생성되었습니다.".format(tank2_name))
# print("체력 {}, 공격력 {}\n".format(tank2_hp, tank2_damage))


# def attack(name, location, damage):
#     print("{} : {} 방향으로 적군을 공격합니다. [공격력 {}]".format(name, location, damage))


# attack(name, "1시", damage)
# attack(tank_name, "1시", tank_damage)
# attack(tank2_name, "1시", tank2_damage)

# 일반 유닛
# class Unit:  # Unit 이 클래스명
#     def __init__(self, name, hp, damage):
#         self.name = name
#         self.hp = hp
#         self.damage = damage
#         print("{} 유닛이 생성되었습니다.".format(self.name))
#         print("체력 {}, 공격력 {}".format(self.hp, self.damage))


# marine1 = Unit("마린", 40, 5)  # 위에 init함수에 정의된 부분중 self 빼고 뒤에 세 가지 다 넣어줘야 동작됨
# marine2 = Unit("마린", 40, 5)
# tank = Unit("탱크", 150, 35)
# 똑같은 하나의 Unit class로 마린, 탱크, 기타 다 만들 수 있게 됨

# __Init__ 함수 : 파이썬에서 쓰이는 생성자 / 즉, 마린이나 탱크같은 "객체"가 만들어질 때 자동으로 호출되는 부분
# 이때 마린과 탱크는 유닛클래스의 "인스턴스"라고 표현

# 멤버 변수 : 클래스 안에 self.name, self.damage 이런 게 "멤버 변수"
# 클래스 내에서 정의된 변수, 그 변수로 초기화를 할 수 있고, 실제로 쓸 수도 있는 것.

# 레이스 : 공중 유닛, 비행기. 클로킹(상대방에게 보이지 않는 기능)
# wraith1 = Unit("레이스", 80, 5)

# print("유닛 이름 : {}, 공격력 : {}".format(wraith1.name, wraith1.damage))
# # 클래스 외부에서 작성 / wraith1.name 이런식으로 멤버변수를 클래스 외부에서도 쓸 수 있다

# # 마인드 컨트롤 : 상대방 유닛을 내 것으로 만드는 것 (빼앗음)
# wraith2 = Unit("빼앗은 레이스", 80, 5)
# wraith2.clocking = True  # clocking이라는 변수를 클래스 외부에서 추가로 할당해서 확장됨
# # 하지만 외부에서 할당한 변수이므로 wraith1 에는 지정되지 않았음
# if wraith2.clocking == True:
#     print("{}는 현재 클로킹 상태입니다.".format(wraith2.name))


# 메소드

# 공격 유닛
# class AttackUnit:
#     def __init__(self, name, hp, damage):
#         self.name = name
#         self.hp = hp
#         self.damage = damage

#     def attack(self, location):
#         print("{} : {} 방향으로 적군을 공격합니다. [공격력 {}]".format(
#             self.name, location, self.damage))

#     def damaged(self, damage):  # 공격받고 데미지 입음
#         print("{} : {} 데미지를 입었습니다.".format(self.name, damage))
#         self.hp -= damage
#         print("{} : 현재 체력은 {}입니다.".format(self.name, self.hp))
#         if self.hp <= 0:
#             print("{} : 파괴되었습니다.".format(self.name))


# # 파이어뱃 : 공격 유닛, 화염방사기.
# firebat1 = AttackUnit("파이어뱃", 50, 16)
# firebat1.attack("5시")

# # 공격 2번 받는다고 가정
# firebat1.damaged(25)
# firebat1.damaged(25)

# 상속 : 물려 받는 것. Unit이라는 클래스의 내용을 상속받아서 AttackUnit 만들기.
# 일반 유닛
class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed

    def move(self, location):
        print("[지상 유닛 이동]")
        print("{} : {} 방향으로 이동합니다. [속도 {}]".format(
            self.name, location, self.speed))


class AttackUnit(Unit):  # (Unit) 이라고 쓰면 Unit class를 상속받아서 만들겠다는 의미
    def __init__(self, name, hp, speed, damage):
        # self.name = name
        # self.hp = hp
        # self.speed = speed
        Unit.__init__(self, name, hp, speed)
        self.damage = damage

    def attack(self, location):
        print("{} : {} 방향으로 적군을 공격합니다. [공격력 {}]".format(
            self.name, location, self.damage))

    def damaged(self, damage):  # 공격받고 데미지 입음
        print("{} : {} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{} : 현재 체력은 {}입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{} : 파괴되었습니다.".format(self.name))


# 파이어뱃 : 공격 유닛, 화염방사기.
# firebat1 = AttackUnit("파이어뱃", 50, 16)
# firebat1.attack("5시")

# # # 공격 2번 받는다고 가정
# firebat1.damaged(25)
# firebat1.damaged(25)

# 9-6.다중 상속
# 드랍쉽 : 공중 유닛, 수송기. 마린 / 파이어뱃 / 탱크 등을 수송. 공격 기능 없음.


class Flyable:  # 날 수 있는 기능을 가진 클래스
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{} : {} 방향으로 날아갑니다. [속도 {}]".format(
            name, location, self.flying_speed))


# 공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage)  # 0 = 지상 speed
        Flyable.__init__(self, flying_speed)

    def move(self, location):
        print("[공중 유닛 이동]")
        self.fly(self.name, location)


# 발키리 : 공중 공격 유닛, 한 번에 14발 미사일 발사.
# valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
# valkyrie.fly(valkyrie.name, "3시")

# 메소드 오버라이딩

# 벌쳐 : 지상 유닛, 기동성이 좋음.
# vulture = AttackUnit("벌쳐", 80, 10, 20)

# 배틀크루저 : 공중 유닛, 체력도 굉장히 좋음, 공격력도 좋음.
battlecrusier = FlyableAttackUnit("배틀크루저", 500, 25, 3)

# vulture.move("11시")
# battlecrusier.move("9시")

# pass : 아무것도 안하고 일단 넘어간다
# 건물


# class BuildingUnit(Unit):
#     def __init__(self, name, hp, locaiton):
#         # Unit.__init__(self, name, hp, 0)
#         # 위에 방식이랑 아래 super(). 방식이랑 같은 역할을 함. 단 super()로 할 땐 self 뺀다.
#         super().__init__(name, hp, 0)
#         self.location = locaiton


# 서플라이 디폿 : 건물, 1개 건물 = 8유닛 생성 가능.
# supply_depot = BuildingUnit("서플라이 디폿", 500, "7시")


# def game_start():
#     print("[알림] 새로운 게임을 시작합니다.")


# def game_over():
#     pass


# game_start()
# game_over()

# super
