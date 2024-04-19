# loop_while.py
# x = 10
# while x > 0:
#     print("불금인데 학원온거 ㅇㅈ")
#     x -= 1

# while True:
#     x = int(input("숫자 0을 넣어야 멈춤:"))
#     if x == 0:
#         break
#     elif x == 1:
#         print("아이스 아메리카노")
#     elif x == 2:
#         print("아이스 라떼")


# 유저에게 언어를 고르세요(1.python 2.java 3.c++)
# while True:
#     num = int(input("언어를 고르세요(1.python 2.java 3.c++):"))
#     if num == 1:
#         print("python")
#     elif num == 2:
#         print("java")
#     elif num == 3:
#         print("c++")
#     elif num == 4:
#         print("프로그램 종료!")
#         break
#     else:
#         print("숫자를 잘못 입력 하였습니다.")


# 계산기 프로그램
# 유저에게
# 0.프로그램 종료 1.더하기 2.빼기 3.곱하기 4.제곱 5.나누기(몫)
# 그 외 번호는 번호 입력 오류 -> 다시 묻기!
# 1번 -> 두 정수를 입력하고 더한 결과값이 나옴
# 2번 -> 두 정수를 입력하고 뺀 결과값이 나옴

while True:
    print("계산기 프로그램!")
    num1 = int(input("첫 번째 정수:"))
    num2 = int(input("두 번째 정수:"))
    codeNumber = int(input("0.프로그램 종료 1.더하기 2.빼기 3.곱하기 4.제곱 5.나누기(몫):"))
    if codeNumber == 0:
        print("프로그램 종료!")
        break
    elif codeNumber == 1:
        print(f"더한 값: {num1 + num2}")
    elif codeNumber == 2:
        print(f"뺀 값: {num1 - num2}")
    elif codeNumber == 3:
        print(f"곱한 값: {num1 * num2}")
    elif codeNumber == 4:
        print(f"제곱 값: {num1 ** num2}")
    elif codeNumber == 5:
        print(f"나눈(몫) 값: {num1 // num2}")
    else:
        print("번호를 잘못 입력 하였습니다!")