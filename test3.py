#coding: utf8
data = [
    {"name": "田中花子", "gender": "女性", "score": 58},
    {"name": "鈴木一郎", "gender": "男性", "score": 76},
    {"name": "山田太郎", "gender": "男性", "score": 69},
    {"name": "佐藤恵子", "gender": "女性", "score": 62},
    {"name": "石井あや", "gender": "女性", "score": 71},
]

def avg(x):
    return 1.0*sum(x) / len(x)

scores = []
for datum in data:
    scores.append(datum["score"])
print avg(scores)
