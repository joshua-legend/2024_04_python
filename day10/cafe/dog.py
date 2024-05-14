# 변수들[명사] + 함수들[동사] = 클래스
# 변수들[name,breed,happiness] +함수들[barking,introducing] = Dog
class Dog:
    # 변수들
    def __init__(self, a, b):
        self.name = a
        self.breed = b
        self.happiness = 0

    def intro(self):
        print(f"{self.name} {self.breed} {self.happiness}")

    def eating(self):
        print("밥먹습니다.")
        self.happiness += 10


a = Dog("제니", "푸들")
a.intro()
b = Dog("맥스", "달마시안")
b.intro()
c = Dog("킹율", "시바시바")
c.intro()

for x in range(10):
    a.eating()
a.intro()
b.intro()
c.intro()