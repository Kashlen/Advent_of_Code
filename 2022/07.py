with open("data\data_07.txt", encoding="utf-8") as file:
    data = file.read().split("\n")

# Puzzle no. 1: NEVIM - udělat strom, procházet jím a počítat...
def make_tree(data):
    dirs = {}
    current_place = []
    for line in data:
        if line[0:7] == "$ cd ..":
            current_place =
        if line[0:4] == "$ cd":
            dirs[line[4:]] = []


    print(dirs)
result = make_tree(data)
# result = sum(dirs_to_hundred_thousands) HODNOTY!
