with open ("data\data_02.txt", encoding = "utf-8") as file:
    data = file.read()

# Puzzle no. 1

rounds = data.split("\n")
scores = []
score_table = {
    "A X": 3,
    "B Y": 3,
    "C Z": 3,
    "A Y": 6,
    "A Z": 0,
    "B X": 0,
    "B Z": 6,
    "C X": 6,
    "C Y": 0
}
for line in rounds:
    score = 0
    if line[2] == "X":
        score += 1
    elif line[2] == "Y":
        score += 2
    elif line[2] == "Z":
        score += 3
    second_score = score_table.get(str(line))
    score += int(second_score)
    scores.append(score)

print(f"Total score is {sum(scores)}.")

# Puzzle no. 2

scores = []
score_table = {
    "A X": 3,
    "B Y": 2,
    "C Z": 1,
    "A Y": 1,
    "A Z": 2,
    "B X": 1,
    "B Z": 3,
    "C X": 2,
    "C Y": 3
}
for line in rounds:
    score = 0
    if line[2] == "X":
        score += 0
    elif line[2] == "Y":
        score += 3
    elif line[2] == "Z":
        score += 6
    second_score = score_table.get(str(line))
    score += int(second_score)
    scores.append(score)

print(f"Total score is {sum(scores)}.")