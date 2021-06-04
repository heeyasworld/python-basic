# 패키지 : 모듈들을 모아놓은 집합. 하나의 디렉토리에 여러 모듈들을 모아둔 걸 패키지라고 함.

class ThailandPackage:
    def detail(self):
        print("[태국 패키지 3박 5일] 방콕, 파타야 여행(야시장 투어) 50만원")


if __name__ == "__main__":
    print("Thailand 모듈을 직접 실행")
    print("이 문장은 모듈을 직접 실행할 때만 실행되요")
    trip_to = ThailandPackage()
    trip_to.detail()
else:
    print("Thailand 외부에서 모듈 호출")
