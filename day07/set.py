# data-type: int,str,float,bool,list
# list,set (집합)
# 중복 허용 안되는 타입
a = {1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4, 5, 6, 7, 8}
burgerking = {"새우와퍼", "불고기와퍼", "치즈와퍼", "스테이크와퍼"}
momstouch = {"새우와퍼", "치즈와퍼", "싸이버거", "불고기버거"}

# 합집합 (|)
union = burgerking | momstouch

# 교집합 (&)
intersection = burgerking & momstouch

# 차집합 (-)
difference = burgerking - momstouch

print(union)
print(intersection)
print(difference)

# 추가
burgerking.add("에그와퍼")

# 삭제
burgerking.remove("새우와퍼") # 구문법 없는 요소 빼면 에러
burgerking.discard("새우와퍼") # 신문법 없는 요소 빼면 에러 발생 안함

# 전체삭제
burgerking.clear()

# set() (중요)
# result = set([1,2,3,1,2,3])
# print(list(result))

news = """The double court date will represent yet another unfathomable twist in the saga of the presumptive Republican nominee who is again stretching America’s judicial and constitutional systems to their limits as he runs to reclaim the White House.

Trump has left no doubt he’d much rather be on the grander stage in Washington, watching Supreme Court justices — three of whom he appointed — debate his claim that, as an ex-president, he cannot be prosecuted for any actions that he took in office. Trump the showman would surely relish holding a photo-op on the court steps below an ornate marble facade that reads “Equal Justice Under Law.” It would be a far more colorful spectacle for a presidential campaign that has morphed with his legal defenses than the increasingly repetitive press gaggles he holds in the dingy corridor outside the Manhattan courtroom hearing his first criminal trial. But Trump has no choice but to listen to more testimony in New York from former tabloid publisher David Pecker, a key witness for prosecutors who allege the ex-president tried to mislead 2016 general election voters by covering up an affair that he denies."""

wordList = news.split()
noDuplicationWords = list(set(wordList))
noDuplicationWords.sort()
print(noDuplicationWords)