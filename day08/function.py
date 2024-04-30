# 함수: input[int,str,[],None] -> output
# 마술 상자: [100 -> 500, 200 -> 1000, 300 -> x]
# f(x) => len(x),str(x),int(x),print(x),input(x)
# count("p")
def koreaIt(x):
    return x + "코리아아이티"


def add(x, y):
    return x + y


# 어떠한 단어를 넣었을 때, 그 단어가 5글자 이상이면
# 글자가 길어요!, 아니면 글자가 짧아요!
def isWordLong(x):
    if len(x) >= 5:
        return "글자가 길어요!"
    else:
        return "글자가 짧아요!"


# 함수: input ->[로직] -> output

# abc(3,'🥚')
# ['🥚','🥚''🥚']

def makeEmojiList(x, y):
    return [y for x in range(x)]


# 🥚 🐣 🐥 🐓 🍗
# 🥚 -> 🐣
# 🐣 -> 🐥
# 🐥 -> 🐓
# 🐓 -> 🍗

def changeEmoji(x):
    dictChange = {
        '🥚': '🐣',
        '🐣': '🐥',
        '🐥': '🐓',
        '🐓': '🍗',
    }
    return dictChange[x]


print(changeEmoji('🐓'))
