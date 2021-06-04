from random import *


class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        print("{0} 유닛이 생성되었습니다.".format(name))

    def move(self, location):
        print("{} : {} 방향으로 이동합니다. [속도 {}]".format(
            self.name, location, self.speed))

    def damaged(self, damage):  # 공격받고 데미지 입음
        print("{} : 공격받아 {} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{} : 현재 체력은 {}입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{} : 파괴되었습니다.".format(self.name))


class AttackUnit(Unit):  # (Unit) 이라고 쓰면 Unit class를 상속받아서 만들겠다는 의미
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage

    def attack(self, location):
        print("{} : {} 방향으로 적군을 공격합니다. [공격력 {}]".format(
            self.name, location, self.damage))

# 마린


class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self, "마린", 40, 1, 5)

    # 스팀팩 : 일정 시간 동안 이동 및 공격 속도를 증가, 자기 체력 10이 감소됨.
    def stimpack(self):
        if self.hp > 10:
            self.hp -= 10
            self.speed += 4
            self.damage += 5
            print("{} : 스팀팩을 사용합니다. (HP 10 감소, 속도 4 증가, 공격 5 증가)".format(self.name))
        else:
            print("{} : 체력이 부족하여 스팀팩을 사용하지 않습니다.".format(self.name))


# 탱크
class Tank(AttackUnit):
    # 시즈모드 : 탱크를 지상에 고정시켜, 더 높은 파워로 공격 가능, 이동은 불가.
    seize_develped = False  # 시즈 모드 개발 여부

    def __init__(self):
        AttackUnit.__init__(self, "탱크", 150, 1, 35)
        self.seize_mode = False

    def set_seize_mode(self):
        if Tank.seize_develped == False:
            return  # 시즈모드 아닐 땐 그냥 아무것도 안하고 이 코드 탈출

        # 현재 시즈모드가 아닐 때 -> 시즈모드
        if self.seize_mode == False:
            print("{} : 시즈모드로 전환합니다.".format(self.name))
            self.damage *= 2
            self.seize_mode = True
        # 현재 시즈모드일 때 -> 시즈모드 해제
        else:
            print("{} : 시즈모드를 해제합니다.".format(self.name))
            self.damage /= 2
            self.seize_mode = False


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
        self.fly(self.name, location)

# 레이스


class Wraith(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__(self, "레이스", 80, 20, 5)
        self.clocked = False  # 클로킹 모드 (해제 상태)

    def cloking(self):
        if self.clocked == True:  # 클로킹 모드 -> 모드 해제
            print("{} : 클로킹 모드 해제합니다.".format(self.name))
            self.clocked = False
        else:  # 클로킹 모드 해제 -> 모드 설정
            print("{} : 클로킹 모드 설정합니다.".format(self.name))
            self.clockeed = True


def game_start():
    print("[알림] 새로운 게임을 시작합니다.")


def game_over():
    print("Player : gg")  # good game
    print("[Player] 님이 게임에서 퇴장하셨습니다.")

# -------------------------------------------------------------------------------------------


# 실제 게임 시작
game_start()

# 마린 3기 생성
m1 = Marine()
m2 = Marine()
m3 = Marine()

# 탱크 2기 생성
t1 = Tank()
t2 = Tank()

# 레이스 1기 생성
w1 = Wraith()

# 유닛 일괄 관리 (생성된 모든 유닛을 append 처리)
attack_units = []  # 관리의 용이성을 위해서 리스트로 묶어주기
attack_units.append(m1)  # 추가
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(t2)
attack_units.append(w1)

# 전군 이동
for unit in attack_units:
    unit.move("1시")

# 탱크 시즈모드 개발
Tank.seize_develped = True
print("[알림] 탱크 시즈 모드 개발이 완료되었습니다.")

# 공격 모드 준비(마린 : 스팀팩, 탱크 : 시즈모드, 레이스 : 클로킹)
for unit in attack_units:
    if isinstance(unit, Marine):
        unit.stimpack()
    elif isinstance(unit, Tank):
        unit.set_seize_mode()
    elif isinstance(unit, Wraith):
        unit.cloking()

# 전군 공격
for unit in attack_units:
    unit.attack("1시")

# 공격 받음
for unit in attack_units:
    unit.damaged(randint(5, 21))  # 공격은 랜덤으로 받음 ( 5~ 20 사이 데미지 )

# 게임 종료
game_over()
