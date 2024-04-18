# 1.정삼각형 넓이
base = int(input("밑변:"))
height = int(input("높이:"))
print(f"정삼각형의 넓이는 {base * height * 0.5}입니다.")

# 2.홀수 and 양수
num = int(input("숫자 입력:"))
if num % 2 == 1 and num > 0:
    print("입력한 숫자는 양수이며 홀수입니다.")
else:
    print("입력한 숫자는 양수 또는 홀수가 아닙니다.")

#3.과일이름에 'a' 포함?
fruit = input("과일 이름 입력:")
if 'a' in fruit:
    print("해당 과일 이름에 'a'가 포함되는군요!")
else:
    print("'a'가 포함되지 않는군요!")









