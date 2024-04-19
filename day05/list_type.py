# 어떠한 타입.그 관련된 기능
# list_type
# soccerPlayer = ["손흥민","황희찬","김민재","이강인"]
# soccerPlayer.append("이재성")
# soccerPlayer.sort()
# print(soccerPlayer)

# 유저에게 과일을 영어로 3개 입력 받고 대문자화 시키고
# 과일리스트를 만들고, 오름차순으로 보여주기
# kiwi,apple,mango => [APPLE,KIWI,MANGO]

a = input("과일 입력:")
upperA = a.upper()
b = input("과일 입력:")
upperB = b.upper()
c = input("과일 입력:")
upperC = c.upper()
fruit = []
fruit.append(upperA)
fruit.append(upperB)
fruit.append(upperC)
fruit.sort()
print(fruit)


