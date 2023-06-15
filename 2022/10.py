with open("data\data_10.txt", encoding="utf-8") as file:
    data = file.read().split("\n")

# Puzzle no. 1
cycle = 1
value = 1
values = []

for line in data:
    print(cycle, value)
    if line[0:4] == "noop":
        cycle += 1
        if (cycle-20) % 40 == 0:
            values.append(cycle * value)
    elif line[0:4] == "addx":
        cycle += 1
        if (cycle-20) % 40 == 0:
            values.append(cycle * value)
        cycle += 1
        value += int(line[5:])
        if (cycle - 20) % 40 == 0:
            values.append(cycle*value)

result = sum(values)
print(result)
print(values)