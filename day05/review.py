# variable, input/print, dataType, operator
# 조건문[if-elif-else]
num = int(input("정수 입력:"))
if num > 0:
    print("0보다 큽니다.")
elif num == 0:
    print("0입니다.")
else:
    print("0보다 작습니다.")

# 반복문[for 문]
for x in range(100):
    if x % 2 == 0:
        print(x) #0,2,4,6,8,...,98