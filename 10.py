# 예외처리 : 에러 발생한 거 처리해주는 역할

# try:
#     print("나누기 전용 계산기입니다.")
#     nums = []
#     nums.append(int(input("첫번째 숫자를 입력하세요 : ")))
#     nums.append(int(input("두번째 숫자를 입력하세요 : ")))
#     # nums.append(int(nums[0] / nums[1]))
#     print("{} / {} = {}".format(nums[0], nums[1], nums[2]))
# except ValueError:
#     print("에러! 잘못된 값을 입력하였습니다.")
# except ZeroDivisionError as err:
#     print(err)  # 무슨 오류인지 출력됨
# except Exception as err:
#     print("알 수 없는 에러가 발생했습니다.")
#     print(err)

# 에러 발생시키기
# # 사용자 정의 예외 처리 : 우리가 직접 정의한 에러를 만들어보자
# finally : 예외처리 구문에서 오류가 나든 말든, 무조건 실행되는 구문


# class BigNumberError(Exception):
#     def __init__(self, msg):
#         self.msg = msg

#     def __str__(self):
#         return self.msg

# try:
#     print("한 자리 숫자 나누기 전용 계산기입니다.")
#     num1 = int(input("첫번째 숫자 입력 : "))
#     num2 = int(input("두번째 숫자 입력 : "))
#     if num1 >= 10 or num2 >= 10:
#         raise BigNumberError("입력값 : {}, {}".format(
#             num1, num2))  # 에러 발생시키기 # 사용자 정의 예외처리
#     print("{} / {} = {}".format(num1, num2, int(num1/num2)))
# except ValueError:
#     print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")
# except BigNumberError as err:
#     print("에러 발생! 한 자리 숫자만 입력하세요.")
#     print(err)
# except ZeroDivisionError:
#     print("에러 발생! 0으로 나눌 수 없습니다.")
# finally:
#     print("계산기를 이용해주셔서 감사합니다.")

# 퀴즈

class SoldOutError(Exception):
    pass


chicken = 10
waiting = 1

while(True):
    try:
        print("[남은 치킨 : {}]".format(chicken))
        order = int(input("치킨 몇 마리 주문하시겠습니까?"))
        if order > chicken:
            print("재료가 부족합니다.")
        elif order < 1:
            raise ValueError
        else:
            print("[대기번호 {}] {}마리 주문이 완료되었습니다.".format(waiting, order))
            waiting += 1
            chicken -= order

        if chicken == 0:
            raise SoldOutError
    except ValueError:
        print("잘못된 값을 입력하였습니다.")
    except SoldOutError:
        print("재고가 소진되어 더 이상 주문을 받지 않습니다.")
        break
