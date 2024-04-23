#1.유저에게 다섯개의 정수를 입력 받고, 리스트화한 다음
#각각 요소를 3배로 만든다음 출력하기
# ex) [5,1,2,5,19] => [15,3,6,15,57]

numberList = []
for x in range(5):
    num = int(input("정수 입력:"))
    numberList.append(num)
print(numberList)
newNumberList = []
for x in numberList:
    newNumberList.append(x*3)
print(newNumberList)


#2.유저에게 서로 다른 다섯개의 정수를 입력 받고,
#리스트화 한 다음에,가장 큰 수를 뽑아내는 프로그램
numberList = []
for x in range(5):
    num = int(input("정수 입력:"))
    numberList.append(num)
numberList.sort()
numberList.reverse()
print(numberList[0])