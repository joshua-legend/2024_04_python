# 기본 자료 구조: 데이터를 어떻게 보관하는지 다루는지에 대한 방법들
# list: 순서 있고, 중복 가능
# set: 순서 없고, 중복 불가능
# dict: k[중복 안됨]-v[중복 가능] 형태로 저장
# tuple: (사과,바나나,키위) 수정 불가능

# 심화 자료 구조:
# graph: 그래프 자료구조 [지도,미니맵,경로 최적화]
# tree: 트리 자료구조 [단어 검색]











# names = ['아메리카노', '라떼', '바닐라']
# prices = [2000, 2500, 3000]
# menu = []
# for index, item in enumerate(names):
#     menu.append({'name': item, 'price': prices[index]})

# names = ['아메리카노', '라떼', '바닐라']
# prices = [2000, 2500, 3000]
# x = dict(zip(names, prices))
# print(x)

# 과일 이름 리스트[3]:
# 과일 가격 리스트[3]:
# zip으로 묶어서 k-v형태 나타내세요
fruits = ['apple', 'orange', 'kiwi']
prices = [3000, 2500, 1500]
menu = [{'name': x, 'price': y} for (x, y) in zip(fruits, prices)]

text = """
The head of public relations at China's biggest search engine Baidu has apologised after her comments glorifying a work-till-you-drop culture sparked public outcry.

In a series of videos posted on Douyin, the Chinese version of TikTok, Qu Jing, said she had no responsibility for employees' well-being "as I'm not your mother".

She also threatened retaliation against subordinates who complained about her management. "I can make it impossible for you to find a job in this industry with just a short essay," she wrote.

On Wednesday, Ms Qu acknowledged that her posts - which have since been taken down - drew "very pertinent" criticism.

"I deeply reflect on and humbly accept them,” she wrote on WeChat.

The furore stirred by Ms Qu highlights the notoriously poor work-life balance in China's tech workplaces."""
a = [{"단어": x, "글자수": len(x)} for x in text.split(" ")]
print(a)