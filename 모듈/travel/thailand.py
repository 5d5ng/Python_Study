class ThailandPackage:
    def detail(self):
        print("태국 마시지 3박 5일 패키지 방콕 파타야 여행")

if __name__ == "__main__": # 모듈 직접 실행하는 경우
    print('Thailand 모듈을 직접실행')
    print('이 문장은 모듈을 직접 실행할 때만 실행되요')
    trip_to = ThailandPackage()
    trip_to.detail()
else:
    print('Thailand  외부에서 모듈 호출')

