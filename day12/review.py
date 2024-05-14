class Dog:
    # 생성 해주는 친구(=생성자)
    # 특별 함수
    def __init__(self, a, b):
        self.name = a
        self.breed = b

    def barking(self):
        print("멍멍!")


a = Dog("월트", "달마시안")
a.barking()


# Book 클래스 만들기
# 제목,작가를 가지는 클래스
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display_info(self):
        return f"책 제목:{self.title} 작가:{self.author}"



b = Book("해리포터", "롤링")
print(b.display_info())