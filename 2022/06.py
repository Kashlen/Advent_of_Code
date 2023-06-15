with open("data\data_06.txt", encoding="utf-8") as file:
    file = file.read()


# Puzzle no. 1
def find_four_different_signs(data):
    for i in range(0, len(data)):
        part = [data[i]]
        for n in range(1, 4):
            part.append(data[i + n])
        counts = []
        for x in part:
            counts.append(part.count(x))
        if sum(counts) == 4:
            return i + 4


position = find_four_different_signs(file)
print(f"{position} characters need to be processed before the first start-of-packet marker is detected")


# Puzzle no. 2
def find_fourteen_different_signs(data):
    for i in range(0, len(data)):
        part = [data[i]]
        for n in range(1, 14):
            part.append(data[i + n])
        counts = []
        for x in part:
            counts.append(part.count(x))
        if sum(counts) == 14:
            return i + 14


position = find_fourteen_different_signs(file)
print(f"{position} characters need to be processed before the first start-of-message marker is detected")
