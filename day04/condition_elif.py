#condition_elif.py
# num = int(input("점수 입력:"))
# if num >= 90:
#     print("A등급")
# elif num >= 80:
#     print("B등급")
# elif num >= 70:
#     print("C등급")
# else:
#     print("과락입니다.🤗")

# 국,영,수 점수를 3개 입력 받고,
# 평균이 90점 이상 'A', 80점 이상 'B', 70점 이상 'C', 60점 이상 'D'
# 나머지는 F로 나타내는 프로그램 작성하기
# kor = int(input("국어 점수:"))
# eng = int(input("영어 점수:"))
# math = int(input("수학 점수:"))
# avg = (kor + eng + math) / 3
#
# if avg >= 90:
#     print("A")
# elif avg >= 80:
#     print("B")
# elif avg >= 70:
#     print("C")
# elif avg >= 60:
#     print("D")
# else:
#     print("F")

# nested condition
# if문의 depth는 2번까지 지향하는 걸로!
score = int(input("점수 입력:"))
if score > 60:
    if score == 100:
        print("만점입니다!")
    else:
        print("합격입니다.")
else:
    if score == 0:
        print("이건 좀...")
    else:
        print("불합격입니다.")



