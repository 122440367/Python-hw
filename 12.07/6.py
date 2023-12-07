scores = []
for i in range(10):
    score = float(input("请输入评委的打分: "))
    scores.append(score)
scores_sorted = sorted(scores)
scores_sorted = scores_sorted[1:-1]
average = sum(scores_sorted) / len(scores_sorted)
print("选手的平均分为:", average)
