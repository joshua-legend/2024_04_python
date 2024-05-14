# sort 보여주기 목표!
def spellingMagic(word):
    spellingList = list(word)  # [m,e,g,a]
    spellingList.sort()  # [a,e,g,m]
    result = "".join(spellingList)  # list -> str

    spellingList1 = list(word)
    spellingList1.reverse()
    result1 = "".join(spellingList1)  #
    return {"sorted": result, "reversed": result1}


# 정수 n이 주어졌을 때, 홀수면 "odd" 짝수면 "even"을 돌려주는
# 함수 만들기
def oddEven(n):
    if n % 2 == 1:
        return "odd"
    else:
        return "even"
