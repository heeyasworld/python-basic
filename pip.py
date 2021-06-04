# pip : pip installs packages, pip installs python
# 파이썬 패키지 관리 시스템

# 내장 함수 built-in functions
# input : 사용자 입력을 받는 함수


# language = input("무슨 언어를 좋아하세요?")
# print("{}은 아주 좋은 언어입니다.".format(language))

# dir : 어떤 객체를 넘겨줬을 때 그 객체가 어떤 변수와 함수를 가지고 있는지 표시
# print(dir())

# import pickle
# import random  # 외장 함수
# print(dir(random))

# lst = [1, 2, 3]
# print(dir(lst))

# name = "Jim"
# print(dir(name))

# 외장함수 import해서 써야함
# glob : 경로 내의 폴더 / 파일 목록 조회 (windosw dri)
# import glob
# print(glob.glob("*.py"))

# os : 운영체제에서 제공하는 기본 기능
#  import os
# print(os.getcwd())  # 현재 디렉토리 표시


# folder = "sample_dir"

# if os.path.exists(folder):
#     print("이미 존재하는 폴더입니다.")
#     os.rmdir(folder)  # rm -> remove dir
#     print(folder, "폴더를 삭제하였습니다.")
# else:
#     os.makedirs(folder)  # 폴더 생성
#     print(folder, "폴더를 생성하였습니다.")

# print(os.listdir())


# import time
# print(time.localtime())
# print(time.strftime("%y-%m-%d %H:%M:%S"))

import datetime
# print("오늘 날짜는", datetime.date.today())

# timedelta : 두 날짜 사이의 간격
today = datetime.date.today()  # 오늘 날짜 저장
td = datetime.timedelta(days=2)  # 100일 저장
print("우리가 만난지 3일은", today + td)  # 오늘로부터 100일 뒤를 알려준다
