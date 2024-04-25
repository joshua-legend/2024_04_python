# "hello".upper() => HELLO
# [].append("사과") => ["사과"]
# print,input,str,list,int,float,list,bool,range,type

# length
# len: 문자열 또는 리스트의 길이를 알려주는 기능
# print(len("hello"))
# print(len("python"))
# print(len([2, 4, 6, 8, 10]))
#
# # max, min
# print(max([2, 12, 3, 51, 23, 312, 3312, 11]))
# print(min([2, 12, 3, 51, 23, 312, 3312, 11]))
#
# # sum
# print(sum([1,2,3,4,5]))


# 영어 기사 스크랩 해오고,
# 단어 길이가 6글자 이상
# 단어들만 출력하기
# hint: "hello world".split("")=>["hello","world"]
# news ="""For most people, sitting in court at their own criminal trial would represent a defining moment of their life.
#
# But Donald Trump’s return to his hush money trial Thursday does not even represent the most critical courtroom drama of his day.
#
# The ex-president’s attention is certain to stray from what he has repeatedly complained is a “freezing” court in New York to the neoclassical splendor of the US Supreme Court. Justices will be hearing oral arguments in his sweeping immunity case that could have profound implications for his legal fate and poses never-before-resolved questions about the powers of the presidency.
#
# The double court date will represent yet another unfathomable twist in the saga of the presumptive Republican nominee who is again stretching America’s judicial and constitutional systems to their limits as he runs to reclaim the White House.
#
# Trump has left no doubt he’d much rather be on the grander stage in Washington, watching Supreme Court justices — three of whom he appointed — debate his claim that, as an ex-president, he cannot be prosecuted for any actions that he took in office. Trump the showman would surely relish holding a photo-op on the court steps below an ornate marble facade that reads “Equal Justice Under Law.” It would be a far more colorful spectacle for a presidential campaign that has morphed with his legal defenses than the increasingly repetitive press gaggles he holds in the dingy corridor outside the Manhattan courtroom hearing his first criminal trial. But Trump has no choice but to listen to more testimony in New York from former tabloid publisher David Pecker, a key witness for prosecutors who allege the ex-president tried to mislead 2016 general election voters by covering up an affair that he denies."""

# words = news.split()
# for x in words:
#     if len(x) >= 6:
#         print(x)


# 문자 길이가 5글자 이하이고 알파벳 a,e 포함되면 대문자로 출력하고
# 그게 아니면 그 과일의 문자 길이를 출력하는 프로그램
# -> APPLE, 6, 4, MANGO, ...
fruits = ["apple","banana","kiwi","mango","strawberry","pineapple","melon"]
for x in fruits:
    if len(x) <= 5 and ("a" in x or "e" in x):
        print(x.upper())
    else:
        print(len(x))


