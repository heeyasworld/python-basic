# quiz

# from random import *

# i = 0
# for customer in range(1, 51):
#     min = randint(5, 50)
#     if 5 <= min <= 15:
#         print("[O] {0}번째 손님 (소요시간 : {1}분)".format(customer, min))
#         i += 1
#     else:
#         print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(customer, min))

# print("총 탑승 승객 : {0}분".format(i))

# 샘풀이 변수명만 다르고 다 똑같다 !!!!!!!!
'''
# 7-1. 함수 정의, 출력
def open_account():
    print("새로운 계좌가 생성되었습니다.")


open_account()

# 전달값과 반환값


def deposit(balance, money):  # 입금
    print("입금이 완료되었습니다. 잔액은 {}원입니다.".format(balance+money))
    return balance+money


def withdraw(balance, money):  # 출금
    if balance >= money:  # 잔액이 출금 이상이면
        print("출금이 완료되었습니다. 잔액은 {0}원입니다.".format(balance-money))
        return balance - money
    else:
        print("출금이 완료되지 않았습니다. 잔액은 {0}원입니다.".format(balance))
        return balance


def withdraw_night(balance, money):  # 저녁에 출금
    commission = 100  # 수수료 값
    return commission, balance - money - commission


balance = 0
balance = deposit(balance, 1000)
balance = withdraw(balance, 10000)
balance = withdraw(balance, 100)

commission, balance = withdraw_night(balance, 500)
print("수수료는 {0}원이며, 잔액은 {1}원입니다.".format(commission, balance))
'''

# 기본값


# def profile(name, age, main_lang):
#     print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}"
#           .format(name, age, main_lang))


# profile("heeya", 20, "python")
# profile("trevor", 30, "java")

# 같은 학교 같은 학년 같은 반 같은 수업 / 나이,공부언어는 같을 것이므로 기본값 사용

# def profile(name, age=17, main_lang="python"):  # 기본값 설정됨
#     print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}"
#           .format(name, age, main_lang))


# profile("heeya")
# profile("trevor")


# 키워드값 정해져있어서 순서 뒤죽박죽 넣어도 제대로 정렬되서 출력됨

# def profile(name, age, main_lang):
#     print(name, age, main_lang)


# profile(name="heeya", main_lang="python", age=20)
# profile(main_lang="java", name="trevor", age=202)

# 가변 인자


# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     print("name : {0}\tage : {1}\t".format(name, age), end=" ")
#     # end =" " 이거 있으면 print한 후 줄바꿈되고 다음 줄 출력이 아닌
#     # " " 한 칸 공백만 생기고 바로 다음 줄 이어서 하게 됨
#     print(lang1, lang2, lang3, lang4, lang5)

# def profile(name, age, *language):  # *language 넣고 싶은 갯수만큼 넣을 수 있다
#     print("name : {0}\tage : {1}\t".format(name, age), end=" ")
#     for lang in language:  # language 안에 포함된 값을 하나씩 넣어서 출력
#         print(lang, end=" ")
#     print()  # ente키 역할을 해줌 줄바꿈


# profile("heeya", 20, "python", "java", "c", "c++", "c#", "javascript")
# profile("trevor", 25, "kotlin", "swift")


# 지역변수, 전역변수
# 지역변수 : 함수 내에서만 사용되고 끝
# 전역변수 : 프로그램내 모든 곳, 어디에서나 부를 수 있다
# gun = 10


# def checkpoint(soldiers):  # 경계근무나가는 군인의 수 입력
#     gun = 20  # 총 가지고 있는 총의 갯수
#     gun = gun - soldiers  # 총 총 갯수 = 총 총 갯수 - 근무나가는 군인수(1인당 1개씩 가지고 나가므로)
#     print("[함수 내] 남은 총 : {0}".format(gun))

# print("전체 총 : {0}".format(gun)) # 10 전역변수인 gun = 10 이 적용됨
# checkpoint(2) # 지역변수인 함수 내 gun = 20 - 2 = 18 이라고 결과나옴
# print("남은 총 : {0}".format(gun)) # 다시금 전역변수인 10 적용됨

#  해결방법

# gun = 10


# def checkpoint(soldiers):  # 경계근무나가는 군인의 수 입력
#     global gun  # 전역 공간에 있는 함수밖 gun = 10을 사용하겠다는 의미
#     gun = gun - soldiers  # 총 총 갯수 = 총 총 갯수 - 근무나가는 군인수(1인당 1개씩 가지고 나가므로)
#     print("[함수 내] 남은 총 : {0}".format(gun))

# print(gun)  # 10
# checkpoint(2)  # 8
# print(gun)  # 8


# gun = 10


# def checkpoint_ret(gun, soldiers):
#     gun = gun - soldiers
#     print("[함수 내] 남은 총 : {0}".format(gun))
#     return gun  # return해줌으로서 밖에 있는 전역변수 gun에 영향미친다


# print("전체 총 : {0}".format(gun))
# # gun에 checkpoint_ret함수에서 계산된 값을 다시 넣어주고 아래에서 출력하면 적용됨
# gun = checkpoint_ret(gun, 2)
# print("남은 총 : {0}".format(gun))


# quiz / my answer

# def std_weight(height, gender):
#     if gender == "male":
#         std = round(height * height * 22, 2)
#         print("키 {0}cm 남자의 표준 체중은 {1}kg 입니다.".format(round(height*100), std))

#     else:
#         std = round(height * height * 21, 2)
#         print("키 {0}cm 여자의 표준 체중은 {1}kg 입니다.".format(round(height*100), std))


# std_weight(1.75, "male")
# std_weight(1.60, "female")

# # teacher's


# def std_weight(height, gender):
#     if gender == "남자":
#         return height * height * 22
#     else:
#         return height * height * 21


# height = 184
# gender = "남자"
# weight = round(std_weight(height / 100, gender), 2)
# print("키 {}cm {}의 표준 체중은 {}kg 입니다.".format(height, gender, weight))

# def f():
#     return "바보"


# print(f())

# 무슨 값을(위에서느 "바보") 함수가 퉤하고 내뱉어줬으면 좋겠을 때 리턴을 쓴다

# def f(x):
#     return x ^ 2 + x + 1


# y = f(2)
# print(y)


# def f(a, b):
#     return a + b


# print(f(1, 4))

# 8-1 표준 입출력


# print("python", "java")  # python java

# print("python", "java", sep=",")  # python,java

# print("python", "java", sep=" vs ")  # python vs java

# # end 적으면 문장의 끝에 ? 넣어주고, 줄바꿈은 하지 않고 뒷문장이랑 이어진다
# print("python", "java", sep=",", end="?")
# print("무엇이 더 재미있을까요?")

# import sys
# print("python", "java", file=sys.stdout) #std out 표준출력
# print("python", "java", file=sys.stderr) #std err 표준에러

# 시험성적
# scores = {"수학": 0, "영어": 50, "코딩": 100}
# for subject, score in scores.items():
#     print(subject.ljust(4), str(score).rjust(4), sep=":")
# # ljust(숫자) 왼쪽으로 정렬하면서, 숫자만큼의 공간 확보
# # rjust(숫자) 오른쪽으로 정렬하명서, 숫자만큼의 공가 확보
# # sep=":" seperate : 콜론으로 두 값을 구분

# 은행 대기 순번표
# 001, 002, ...

# for num in range(1, 21):  # 1-20
#     print("대기번호 : " + str(num).zfill(3))
#     # 3크기 만큼의 공간을 확보하고 값이 없는 빈공간은 0으로 채워줘 zfill(3)

# answer = input("아무 값이나 입력하세요 : ")
# print("입력하신 값은 " + answer + "입니다")
# answer = 10
# print(type(answer))
# 여기에서의 교훈 : input으로 값을 받을 경우 10처럼 숫자 입력을 하더라도 int 값이 아닌 str 값으로 인식됨

# 다양한 출력 포맷
# 0:>10  0번째 자리에 들어가는 데이터에 대한 설정 {0: 설정 여기에 적기}
# print("{: >10}".format(500))
# # 500을 출력하되 빈자리는 빈공간으로 두고, > 오른쪽 정렬, 총 10자리 공간을 확보

# print("{: >+10}".format(500))
# print("{0: >+10}".format(-500))
# # 양수일 땐 + 표시, 음수일땐 - 표시

# print("{0:_<+10}".format(500))
# print("{0:_<10}".format(500))
# # 왼쪽 정렬, 빈칸을 _로 채움

# print("{0:,}".format(1000000000))
# # 3자리마다 콤마 찍어주기

# print("{0:+,}".format(1000000000))
# print("{0:+,}".format(-1000000000))
# # 3자리마다 콤마 찍어주기 +- 부호도 붙이기

# print("{0:^<+30,}".format(100000000000))
# # 3자리마다 콤마 찍어주기 +- 부호도 붙이기 , 자릿수도 확보 30칸
# # 돈이 많으면 행복하니까 빈자리는 ^ 로 채우기

# print("{0:f}".format(5/3))
# # 소수점 출력
# print("{0:.2f}".format(5/3))
# 소수점 특정자릿수까지만 표시할래  소숫점2자리까지 표시해달라는 뜻. 3자리에서 반올림된 값 출력.

# 파일 입출력
# score_file = open("score.txt", "w", encoding="utf8")
# # 이 파일을 "w" 쓰기위한 목적으로 연다
# print("수학 : 0", file=score_file)  # 파일안에 내용써넣기 / 자동 줄바꿈
# print("영어 : 50", file=score_file)
# score_file.close()  # 파일 닫기

# score_file = open("score.txt", "a", encoding="utf8")
# # "a" append 이어 쓰기
# score_file.write("과학 : 80")
# score_file.write("\n코딩 : 100")
# # 위의 print로 출력하면 자동줄바꿈되지만 이걸로 쓰면 자동줄바꿈 안됨/그래서 \n 으로 수동줄바꿈해주기
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# # "r" 파일을 읽는다
# print(score_file.read())  # 파일에 있는 모든 내용을 읽는다
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.readline(), end="")
# # 줄별로 읽기, 한 줄 읽고 커서는 다음줄로 이동
# # 그리고 print 자체도 한 줄 띄워주기 때문에 결국 '두줄'이 띄워지게 됨.
# # 이게 싫다면 end="" 를 코드에 삽입하면 줄바꿈이 한번만 됨
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# while True:
#     line = score_file.readline()
#     if not line:
#         break
#     print(line, end="")
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# lines = score_file.readlines()  # 모든 line을 가지고 와서 list 형태로 저장
# for line in lines:
#     print(line, end="")
# score_file.close()

# pickle
# import pickle
# # wb
# # profile이라는 pickle 파일 만들기 wb->write 바이너리(binary) 타입
# profile_file = open("profile.pickle", "wb")
# profile = {"name": "heeya", "age": 30, "hobby": [
#     "tennis", "coding", "weight_training"]}  # [] list {} dictionary
# print(profile)
# pickle.dump(profile, profile_file)  # profile 에 있는 정보를 file 에 저장해줌
# profile_file.close()

# # rb
# profile_file = open("profile.pickle", "rb")  # read binary 읽어주는 기능
# profile = pickle.load(profile_file)  # file에 있는 정보를 profile 에 불러오기
# print(profile)
# profile_file.close()

# 우리가 가지고 있는 어떤 데이터를 피클을 통해서 어떤 파일에 저장을 하고
# 파일에 있는 내용을 로드를 통해서 불러와서 변수에 저장한 다음
# 계속 쓸 수 있도록 해주는 유용한 라이브러리 pickle

# with
# import pickle

# file을 열고, as profile_file : 프로필_파일이라는 변수에 저장
# with open("profile.pickle", "rb") as profile_file:
#     print(pickle.load(profile_file))  # 파일 실행 close 해줄 필요없이 종료됨

# with open("study.txt", "w", encoding="utf8") as study_file:
#     study_file.write("python을 열심히 공부하고 있어요")

# with open("study.txt", "r", encoding="utf8") as study_file:
#     print(study_file.read())


# quiz 7

# for no in range(1, 51):
#     with open("{0}주차.txt".format(no), "w", encoding="utf8") as report_file:
#         report_file.write("- {0} 주차 주간보고 - ".format(no))
#         report_file.write("\n부서 : ")
#         report_file.write("\n이름 : ")
#         report_file.write("\n업무 요약 : ")

# for no in range(1, 51):
#     with open("{0}주차.txt".format(no), "r", encoding="utf8") as report_file:
#         print(report_file.read())
