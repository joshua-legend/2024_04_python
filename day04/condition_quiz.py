#1.정수를 입력 받고
#양의 홀수, 양의 짝수, 0, 음의 홀수, 음의 짝수
#판별해주는 프로그램
# ex) -5 => 음의 홀수, 0 => 0, 3 => 양의 홀수
# num = int(input("정수 입력:"))
# if num > 0:
#     if num % 2 == 1:
#         print("양의 홀수 입니다.")
#     else:
#         print("양의 짝수 입니다.")
# elif num == 0:
#     print("0 입니다.")
# else:
#     if num % 2 == 1:
#         print("음의 홀수 입니다.")
#     else:
#         print("음의 짝수 입니다.")

# num = int(input("정수 입력:"))
# isPositive = num > 0
# isNegative = num < 0
# isOdd = num % 2 == 1
# isEven = num % 2 == 0
# if isPositive and isOdd:
#     print("양의 홀수 입니다.")
# elif isPositive and isEven:
#     print("양의 짝수 입니다.")
# elif isNegative and isOdd:
#     print("음의 홀수 입니다.")
# elif isNegative and isEven:
#     print("음의 짝수 입니다.")
# else:
#     print("0 입니다.")

# x = int(input("x 좌표 입력:"))
# y = int(input("y 좌표 입력:"))
#
# isXPositive = x > 0
# isXNegative = x < 0
# isXZero = x == 0
# isYPositive = y > 0
# isYNegative = y < 0
# isYZero = y == 0
#
# if isXZero and isYZero:
#     print("원점입니다.")
# elif isYZero:
#     print("x축 위에 존재합니다.")
# elif isXZero:
#     print("y축 위에 존재합니다.")
# elif isXPositive and isYPositive:
#     print("1사분면 위에 존재합니다.")
# elif isXNegative and isYPositive:
#     print("2사분면 위에 존재합니다.")
# elif isXNegative and isYNegative:
#     print("3사분면 위에 존재합니다.")
# else:
#     print("4사분면 위에 존재합니다.")

price = int(input("구매한 가격:"))

if price >= 200000:
    print(f"구매 금액은 {price}원, 할인율은 {20}%, 할인 금액은 {price*0.2}원, 최종 결제 금액은 {price-price*0.2}원입니다.")
elif price >= 100000:
    print(f"구매 금액은 {price}원, 할인율은 {10}%, 할인 금액은 {price*0.1}원, 최종 결제 금액은 {price-price*0.1}원입니다.")
elif price >= 50000:
    print(f"구매 금액은 {price}원, 할인율은 {5}%, 할인 금액은 {price * 0.05}원, 최종 결제 금액은 {price - price * 0.05}원입니다.")
else:
    print(f"구매 금액은 {price}원, 할인율은 {0}%, 할인 금액은 {price * 0}원, 최종 결제 금액은 {price - price * 0}원입니다.")







