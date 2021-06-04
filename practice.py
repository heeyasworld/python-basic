# 애완동물을 소개해주세요
# animal = "고양이"
# name = "해피"
# age = 4
# hobby = "낮잠"
# is_adult = age >= 3

# print("우리집 " + animal + "의 이름은 " + name + "에요")
# hobby = "공놀이"
# print(name + "는 " + str(age) + "살이며, " + hobby + "을 아주 좋아해요")
# print(name + "는 어른일까요? " + str(is_adult))

'''
여러문장 주석처리 '''
#  여러줄 선택하고  커맨드 + 슬러시(/) 누르면 한번에 주석됨


# quiz
# station = "사당"
# print(station + "행 열차가 들어오고 있습니다.")
# station = "신도림"
# print(station + "행 열차가 들어오고 있습니다.")
# station = "인천공항"
# print(station + "행 열차가 들어오고 있습니다.")

'''
# 3-1 연산자
print(1+1)
print(3-2)
print(5*2)
print(6/3)

print(2**3)  # 2^3 = 8
print(5 % 3)  # 5/3을 한 값의 나머지 구하기 2
print(10 % 3)  # 1

print(5//3)  # 몫구하기1
print(10//3)  # 3

print(10 > 3)
print(4 >= 7)
print(10 < 4)
print(5 <= 5)

print(3 == 3)  # 3은 3과 똑같다
print(4 == 2)
print(3+4 == 7)

print(1 != 3)  # != 같지 않다
print(not(1 != 3))

print((3 > 0) and (3 < 5))
print((3 > 0) & (3 < 5))

print((3 > 0) or (3 > 5))  # true
print((3 > 0) | (3 > 5))  # true

print(5 > 4 > 3)  # true
print(5 > 4 > 7)  # false
'''
'''
# 3-2 간단한수식
print(2+3*4)  # 14
print((2+3)*4)

number = 2 + 3 * 4  # 14
print(number)
number = number + 2
print(number)  # 16
number += 2
print(number)  # 18
number *= 2
print(number)  # 36
number /= 2
print(number)  # 18
number -= 2
print(number)  # 16
number %= 5  # 나머지1
print(number)  # 1
'''
'''
# 3-3 숫자 처리 함수
from math import *
print(abs(-5))  # 5
print(pow(4, 2))  # 4^2 = 4*4 = 16
print(4**2)  # 4^2 = 16
print(max(5, 12))  # max
print(min(5, 12))  # min
print(round(3.14))  # 반올림한 값 3
print(round(4.99))  # 5

# math library에 있는 모든 걸 이용하겠다
print(floor(4.99))  # 내림 4
print(ceil(3.14))  # 올림 4
print(sqrt(16))  # 제곱근 구하기 4.0
'''

# 3-4 랜덤함수(난수 무작위로 숫자 뽑아주기)

# print(random())  # 계속 다른 난수 출력된다 0.0 ~ 1.0 미만의 값
# print(random()*10)  # 0.0~10.0미만
# print(int(random()*10))  # 0~10 미만의 임의의 값 생성
# print(int(random()*10)+1)  # 1~10이하의 임의의 값 생성

# 로또
# 1
# print(int(random()*45)+1)  # 1~45이하의 임의의 값 생성
# print(int(random()*45)+1)  # 1~45이하의 임의의 값 생성
# print(int(random()*45)+1)  # 1~45이하의 임의의 값 생성
# print(int(random()*45)+1)  # 1~45이하의 임의의 값 생성
# print(int(random()*45)+1)  # 1~45이하의 임의의 값 생성
# print(int(random()*45)+1)  # 1~45이하의 임의의 값 생성
# 2
# print(randrange(1, 46))  # 1-46미만의 임의의 값 생성
# print(randrange(1, 46))  # 1-46미만의 임의의 값 생성
# print(randrange(1, 46))  # 1-46미만의 임의의 값 생성
# print(randrange(1, 46))  # 1-46미만의 임의의 값 생성
# print(randrange(1, 46))  # 1-46미만의 임의의 값 생성
# print(randrange(1, 46))  # 1-46미만의 임의의 값 생성
# 3
# from random import *
# print(randint(1, 45))  # 1-45이하의 임의의 값 생성
# print(randint(1, 45))  # 1-45이하의 임의의 값 생성
# print(randint(1, 45))  # 1-45이하의 임의의 값 생성
# print(randint(1, 45))  # 1-45이하의 임의의 값 생성
# print(randint(1, 45))  # 1-45이하의 임의의 값 생성
# print(randint(1, 45))  # 1-45이하의 임의의 값 생성

# 퀴즈

# from random import *
# a = randint(4, 28)
# print("오프라인 스터디 모임 날짜는 매월 "+str(a)+"일로 선정되었습니다.")
'''
# 문자열
sentence = '나는 소년입니다'
print(sentence)
sentence2 = "PYTHON IS EASY"
print(sentence2)
sentence3 = """
큰따옴표 세개 적고
여러줄에 문장 한번에
쓰는 것도 가능하지롱
"""
print(sentence3)

# 슬라이싱
jumin = "990120-1234567"
print("성별 : " + jumin[7])
# jumin[넣는 숫자번째에 쓰인 문자 출력] 0부터 시작하므로 1은 7번째 자리에 있음
print("연 : " + jumin[0:2])
# 0부터 2 이전까지의 숫자를 연속으로 출력 -> 0, 1번째만 출력
print("월 : " + jumin[2:4])
print("일 : " + jumin[4:6])
print("생년월일 : " + jumin[:6])
# :6만 적어도 0번째부터 출력된다
print("뒤 7자리 : " + jumin[7:])
# 7: 이렇게 쓰면 7번째부터 끝까지도 출력된다
print("뒤 7자리 (뒤에부터) : "+jumin[-7:])
# 맨 뒤 숫자는 -1자리라고도 표현된다. 고로 성별1부분은 -7이됨

# 문자열 처리함수
python = "Python is Amazing"
print(python.lower())  # 소문자로 전부출력
print(python.upper())  # 대문자로 전부출력
print(python[0].isupper())  # python[0] 첫번째자리가 대문자인지 확인
print(python[0].islower())  # false
print(len(python))  # python 문자의 길이
print(python.replace("Python", "Java"))  # python찾아서 java로 바꾸기

index = python.index("n")  # "n"이라는 글자의 위치
print(index)
index = python.index("n", index + 1)
# 처음꺼말고 그 다음꺼에서부터 나오는 n
print(index)

print(python.find("n"))  # "n" 나오는 위치 알려줌 5
print(python.find("java"))  # find에서는 내가 원하는 값 없다면 -1 결과값
# print(python.index("Java"))  하지만 index에서는 실행자체가 안되고 오류난다

print(python.count("n"))  # n이 총 몇번 나오는지 2

# 문자열포맷
# print("a" + "b")
# print("a", "b")  # 콤마는 띄어쓰기 출력된다

# 방법1
print("나는 %d살입니다." % 20)  # 정수
print("나는 %s을 좋아해요" % "파이썬")  # 문자열
print("Apple은 %c로 시작해요." % "A")  # 문자 한글자

print("나는 %s살입니다" % 20)  # 문자열 & 숫자
print("나는 %s색과 %s색을 좋아해요." % ("파란", "빨간"))  # 다중입력도 가능

# 2
print("나는 {}살입니다.".format(20))
print("나는 {}색과 {}색을 좋아해요.".format("파란", "빨간"))
print("나는 {0}색과 {1}색을 좋아해요.".format("파란", "빨간"))
# 위 둘은 같은 결과
print("나는 {1}색과 {0}색을 좋아해요.".format("파란", "빨간"))

# 3
print("나는 {age}살이며, {color}색을 좋아해요.".format(age=20, color="빨간"))
print("나는 {age}살이며, {color}색을 좋아해요.".format(color="빨간", age=20))

# 4(v3.6 이상부터 사용 가능한 방법)
age = 20
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요.")

# 탈출 문자
print("백문이 불여일견\n백견이 불여일타")
# \n 엔터 쳐주세요

# 저는 "나도코딩"입니다.
print("저는 \"나도코딩\"입니다.")
print("저는 \'나도코딩\'입니다.")
# \뒤에 " 넣어주면 출력오류안나고 잘 출력된다 \" \'

# \\ : 문장 내에서 \ 하나의 역슬러시로 바뀌게 된다
print("C:\\Users\\Nadocoding\\Desktop\\PythonWorkspace>")

# \r : 커서를 맨앞으로 이동서 덮어씌움
print("Red Apple\rPine")
# PineApple 이라고 나옴 :: 왜냐하면 red apple 이걸 pine이 네 글자만큼 덮음
# 그래서 \rPi 까지로 두글자만 적으면 두글자만 덮혀서 결과 :: Pid Apple

# \b : 백스페이스(한 글자 삭제)
print("Redd\bApple")  # d하나 삭제되고 RedApple 출력

# \t : tab
print("Red\tApple") #Red     Apple 결과물


# 퀴즈3
# 내 풀이
site = "http://naver.com"
site2 = site[7:]  # naver.com
site3 = site2.replace(".com", "")  # naver

a = site3[:3]  # nav
b = len(site3)  # 5
c = site.count("e")  # 1

print(a+str(b)+str(c)+"!")

# mine 2

site = "http://naver.com"
site = site[7:]  # naver.com
site = site[:site.index(".")]  # naver
password = site[:3] + str(len(site)) + str(site.count("e")) + "!"
print(f"{site}의 비밀번호는 {password}입니당")

# 샘 풀이
# url = "http://naver.com"
url = "http://google.com"

my_str = url.replace("http://", "")  # naver.com
my_str = my_str[:my_str.index(".")]
# my_str[0:5] -> 0~5직전까지 (0, 1, 2, 3, 4) #naver
# my_str 변수에서 index(".") .이 처음으로 나오는 그 위치 앞까지만 슬라이싱 출력

password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
print("{}의 비밀번호는 {}입니다.".format(url, password))


# 5-1. 리스트

subway = [10, 20, 30]
print(subway)

subway = ["heeya", "trevor", "charlie"]
print(subway)
print(subway.index("trevor"))

subway.append("bailey")  # list 맨 뒤에 추가삽입
print(subway)

subway.insert(1, "lion")  # 리스트 1번 위치에 라이언 집어넣기
print(subway)

print(subway.pop())  # 맨뒤에꺼 삭제되는데 그게 누구인지 bailey
print(subway)

# print(subway.pop())  # chalrie
# print(subway)  # charlie out

# print(subway.pop())  # trevor
# print(subway)  # trevor out

subway.append("heeya")
print(subway)
print(subway.count("heeya"))


num_list = [5, 2, 4, 3, 1]
num_list.sort()  # 정렬
print(num_list)

num_list.reverse()  # 뒤집기
print(num_list)

num_list.clear()  # 모두 지우기
print(num_list)  # [] 이렇게 빈 리스트 출력된다

# 다양한 자료형 함께 사용
num_list = [5, 2, 3, 4, 1]
mix_list = ["heeya", 20, True]
# print(mix_list)

num_list.extend(mix_list)  # list 합치기
print(num_list)  # [5, 2, 3, 4, 1, 'heeya', 20, True]
'''

# 사전
# cabinet = {3: "heeya", 100: "trevor"} # key: "value"
# print(cabinet[3])
# print(cabinet[100])

# print(cabinet.get(3))
# print(cabinet[5]) #없는 키값 입력시 오류나고 프로그램 여기에서 종료됨

# print(cabinet.get(5))  # get()이용시 없는 키값이라도 'None'출력되고 프로그램 계속 실행됨
# print(cabinet.get(5, "사용 가능"))  # "사용 가능"은 앞에 키값이 none일 경우 출력되고, none아니면 출력아예안됨

# print(3 in cabinet)  # true
# print(5 in cabinet)  # false

# cabinet = {"a-3": "heeya", "a-100": "trevor"}
# print(cabinet["a-3"])
# print(cabinet["a-100"])

# # new customer
# print(cabinet)
# cabinet["a-3"] = "lion"  # heeya -> lion, update key
# cabinet["c-20"] = "charlie"  # add new key
# print(cabinet)

# del cabinet["a-3"]  # delete key
# print(cabinet)

# print(cabinet.keys())  # print only keys

# print(cabinet.values())  # print only values

# print(cabinet.items())  # print key and value together

# cabinet.clear()  # all delete
# print(cabinet)  # {} 출력됨


# 튜플
# list랑 다르게 내용추가, 변경을 할수없다/ 속도는 더 빠르다

# menu = ("돈가스", "치즈가스")
# print(menu[0])
# print(menu[1])

# name = "heeya"
# age = "20"
# hobby = "coding"
# print(name, age, hobby)

# (name, age, hobby) = ("heeya", 20, "coding")
# print(name, age, hobby)
# name = "trevor"
# print(name, age, hobby)

# 세트set 집합
# 중복이 안되고, 순서가 없다

# my_set = {1, 2, 3, 3, 3}
# print(my_set)  # {1,2,3}

# java = {"heeya", "trevor", "babe"}
# python = set(["heeya", "lion"])  # 이렇게도 set 정의 가능

# # 교집합 (java, python 둘다 가능한 heeya)
# print(java & python)
# print(java.intersection(python))

# # 합집합(java, python 둘중 하나 이상 가능한 사람들)
# print(java | python)
# print(java.union(python))

# # 차집합 (java할수있지만 python 못하는 개발자)
# print(java - python)
# print(java.difference(python))

# # python 할줄아는 사람이 늘어남
# python.add("trevor")
# print(python)

# # java를 까먹은 사람
# java.remove("babe")
# print(java)


# # 자료구조의 변경
# # coffee shop
# menu = {"coffee", "milk", "juice"}
# print(menu, type(menu))

# menu = list(menu)
# print(menu, type(menu))

# menu = tuple(menu)
# print(menu, type(menu))

# menu = set(menu)
# print(menu, type(menu))

# quiz 4
# list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
#         16, 17, 18, 19, 20]
# shuffle(list)
# yay = sample(list, 4)

# print(" -- 당첨자 발표 -- ")
# print("치킨 당첨자 : "+str(yay[0]))
# print("커피 당첨자 : ["+str(yay[1])+", "
#       + str(yay[2])+", "+str(yay[3])+"]")
# print(" -- 축하합니다 -- ")

'''
from random import *
users = range(1, 21)
# 1이상 21미만 숫자 생성
# print(type(users))
users = list(users)
# range type -> list type 바뀜
# print(type(users))

# print(users)
shuffle(users)
# print(users)

winners = sample(users, 4)
print(" -- 당첨자 발표 -- ")
print("치킨 당첨자 : {}".format(winners[0]))
print("커피 당첨자 : {}".format(winners[1:]))
print(" -- 축하합니다 -- ")
'''

# # 6-1. if
# weather = input("What's the weather like today? ")
# if weather == "rain" or weather == "snow":
#     print("get your umbrella")
# elif weather == "fine dust":
#     print("get your mask")
# else:
#     print("you don't need anything today")

# temp = int(input("What's the temperature today?"))
# if temp >= 30:
#     print("It's hot today")
# elif temp >= 20:
#     print("It's good weather for picnic")
# elif 20 > temp > 15:
#     print("It's chilly today. Get your jacket just in case")
# else:
#     print("It's cold today.")


# for

# for waiting_no in [0, 1, 2, 3, 4]:
#     print("waiting_no : {0}".format(waiting_no))
# # [0,1,2,3,4] list속 값들이 하나씩 돌아가면서 0부터 순차적으로
# # waiting_no 속으로 들어감

# for waiting_no in range(5):  # range(5) 0부터 5미만 숫자까지 0,1,2,3,4
#     print("waiting_no : {}".format(waiting_no))

# for wait_no in range(1, 6):  # 1-5
#     print("wait_no : {}".format(wait_no))

# starbucks = ["Ironman", "Thor", "Hulk"]
# for customer in starbucks:
#     print("{}, Your coffee is ready.".format(customer))

# while 조건이 만족될 때까지 반복
# customer = "Thor"
# index = 5
# while index >= 1:
#     print("{0}, Your coffee is ready. {1}min.".format(customer, index))
#     index -= 1
#     if index == 0:
#         print("Your coffee is disposed of")

# customer = "Ironman"
# index = 1
# while True:  # 이거 무한루프
#     print("{0}, Your coffee is ready. {1}".format(customer, index))
#     index += 1

# customer = "Thor"
# person = "Unknown"

# while person != customer:
#     print("{0}, Your coffee is ready.".format(customer))
#     person = input("What's your name?")


# continue and break
# absent = [2, 5]  # 결석
# no_book = [7]
# for student in range(1, 11):
#     if student in absent:
#         continue
#     elif student in no_book:
#         print(
#             "Let's finish the class. but {0} come to teacher's room.".format(student))
#         break
#     print("{0}, Read a book.".format(student))
# contiue는 해당 부분만 스킵하고 뒷부분은 실행
# BREAK는 그자리에서 종료

# 한줄 for
# students = list(range(1, 6))  # [1,2,3,4,5]
# print(students)
# students = [i+100 for i in students]
# print(students)

# alumnos = ["Iron man", "Thor", "I am groot"]
# alumnos = [len(i) for i in alumnos]
# print(alumnos)

# student = ["iron man", "thor", "hulk"]
# student = [i.upper() for i in student]
# print(student)

# quiz
