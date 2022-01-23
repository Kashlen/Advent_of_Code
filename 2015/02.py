
with open ("data\data_02.txt", encoding = "utf-8") as soubor:
    data = soubor.read()

# 1. příklad
paper = 0
for present in data.split("\n"):
    present = ([int(side) for side in present.split("x")])
    a, b, c = sorted(present)
    paper += (3 * a * b) + (2 * b * c) + (2 * a * c)

print(paper)


# 2. příklad
ribbon = 0
for present in data.split("\n"):
    present = ([int(side) for side in present.split("x")])
    a, b, c = sorted(present)
    ribbon += (2 * a) + (2 * b) + (a * b * c)

print(ribbon)


