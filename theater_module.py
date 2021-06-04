# 예시. 자동차.
# 일부 부품만 교체 가능하듯이
# 타이어나 범퍼처럼 일부만 교체할 수 있도록 코드 짜면 유지 및 보수에 용이
# 파이썬 : 클래스, 함수 등을 담고 있는 파일을 '모듈'이라고 부름.
# 모듈의 확장자는 : .py

# 극장에 있다고 가정하고 새로운 모듈 만들어보겠음
# 현금 결제만 되는데 거스름돈을 못준다고 하는 경우

# 일반 가격 정보 - 함수
def price(people):
    print("{}명 가격은 {}원입니다.".format(people, people * 10000))

# 조조 할인 가격


def price_morning(people):
    print("{}명 조조할인 가격은 {}원입니다.".format(people, people * 6000))

# 군인 할인 가격


def price_solider(people):
    print("{}명 군인할인 가격은 {}원입니다.".format(people, people * 4000))
