# 1. 음료 선택 및 잔돈 계산 프로그램
print("1.아메리카노(3000원) 2.레몬에이드(4000원) 3.카페라떼(3500원)")
beverage = int(input("음료 선택:"))
money = int(input("투입 금액:"))

if beverage == 1:
    print(f"아메리카노를 선택하셨습니다. 잔돈은 {money - 3000} 입니다.")
elif beverage == 2:
    print(f"레몬에이드를 선택하셨습니다. 잔돈은 {money - 4000} 입니다.")
elif beverage == 3:
    print(f"레몬에이드를 선택하셨습니다. 잔돈은 {money - 3500} 입니다.")
else:
    print("선택하신 번호의 음료는 없습니다.")

# 2.
print("1.시내버스(1200원) 2.광역버스(2000원) 3.마을버스(1000원)")
bus = int(input("노선 선택:"))
age = int(input("승객 나이:"))

# 7이하, 65이상
if age <= 7 or age >= 65:
    print("해당 고객은 무료 입니다.")
# 8~19세 30%
elif 8 <= age and age <= 19:
    if bus == 1:
        print(f"시내버스 요금은 {1200 * 0.7}원 입니다.(청소년 할인 적용)")
    elif bus == 2:
        print(f"광역버스 요금은 {2000 * 0.7}원 입니다.(청소년 할인 적용)")
    elif bus == 3:
        print(f"마을버스 요금은 {1000 * 0.7}원 입니다.(청소년 할인 적용)")
    else:
        print("해당 버스 번호는 없습니다.")
else:
    if bus == 1:
        print(f"시내버스 요금은 {1200}원 입니다.")
    elif bus == 2:
        print(f"광역버스 요금은 {2000}원 입니다.")
    elif bus == 3:
        print(f"마을버스 요금은 {1000}원 입니다.")
    else:
        print("해당 버스 번호는 없습니다.")

# 3.
num = int(input("정수 입력:"))
for x in range(1, 101):
    if x % num == 0 and x % 2 == 0:
        print(x)
