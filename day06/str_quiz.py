#1. 뉴스 기사를 스크랩 해오고,
# 유저가 입력한 단어를 뉴스기사에서
# 그 해당 단어를 모두 대문자화 시켜서
# 다시 보여주기.
news = """Two Malaysian navy helicopters collided in mid-air as they flew in formation during a rehearsal for a military parade, killing all 10 crew on board.

One of the aircraft clipped the rotor of the other before the two crashed into the ground, footage published on local media showed.

The incident took place at 09:30 local time (02:30 BST) in the Malaysian town of Lumut, which is home to a Royal Malaysian Navy base.

There are no known survivors.
"""
# word = input("단어 입력:")
# newNews = news.replace(word,word.upper())
# print(newNews)

#2.영어 기사를 스크랩 해오고,
#단어 사이에 🍅 넣고 출력하기
words = news.split(" ")
news1 = "🍅".join(words)
print(news1)