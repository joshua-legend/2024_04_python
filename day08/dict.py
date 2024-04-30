# (기본 타입) a = 1, b = 3.14, c = True, d = "hello"
# e = [] , f = {} set or dict
# key[str or int] - value[any]
person = {
    'name': "엄준식",
    'age': 22,
    'town': "동탄시",
    'coffeeList': ['아아', '라떼', '바닐라'],
    'academy': {
        "first": "java",
        "second": "c-langauge",
        "third": "python",
    },
}

print(f"이름: {person["name"]} 동네:{person["town"]} 좋아하는 커피 3번째:{person["coffeeList"][2]}")
print(f"세번째 수업:{person["academy"]["third"]}")

# 데이터 생성
person["gender"] = "woman"  # k - v 데이터 만들기

# 데이터 삭제
del person["town"]
print(person)
#
print(person.keys())  # key
print(person.values())  # value
print(person.items())  # k - v 모두
