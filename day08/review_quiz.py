# - 입력: n = 7
#     - 결과: 16 (1 + 3 + 5 + 7)
# - 입력: n = 6
#     - 결과: 56 (2^2 + 4^2 + 6^2)
# num = int(input("입력:"))  # 7
# result = 0
# # 홀수
# if num % 2 == 1:
#     for x in range(num + 1):
#         if x % 2 == 1:
#             result += x
# else:
#     for x in range(num+1):
#         if x % 2 == 0:
#             result += x ** 2
# print(result)

# - 입력: arr = [1, 2, 3] (변수 선언 상태),  k = 3(입력)
#     - 결과: [3, 6, 9] (모든 원소에 3을 곱함)
# - 입력: arr = [1, 2, 3] (변수 선언 상태) , k = 2 (입력)
#     - 결과: [3, 4, 5] (모든 원소에 2를 더함)

arr = [1, 2, 3]
k = int(input("입력:"))

newList = []
if k % 2 == 1:
    for x in arr:
        newList.append(x * k)
else:
    for x in arr:
        newList.append(x + k)
print(newList)