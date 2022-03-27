
from encodings import utf_8


with open ("data\data_03.txt", encoding="utf_8") as file:
    data = file.read()


# 1. example


def how_many_houses(data):
    coordinates = (0, 0)
    visited = {(0, 0)}
    for sign in data:
        x, y = coordinates
        if sign == "<":
            coordinates = (x-1, y)
        elif sign == ">":
            coordinates = (x+1, y)
        elif sign == "v":
            coordinates = (x, y-1)
        elif sign == "^":
            coordinates = (x, y+1)
        visited.add(coordinates)

    print("Santa visited " + str(len(visited)) + " houses.")


how_many_houses(data)


# 2. example - střídají se Santa a Robot...

santa = list()
robo_santa = list()

for i, j in enumerate(data, start=1):
    if i % 2 == 0:
        robo_santa.append(j)
    elif i % 2 == 1:
        santa.append(j)



def set_of_houses(data):
    coordinates = (0, 0)
    visited = {(0, 0)}
    for sign in data:
        x, y = coordinates
        if sign == "<":
            coordinates = (x-1, y)
        elif sign == ">":
            coordinates = (x+1, y)
        elif sign == "v":
            coordinates = (x, y-1)
        elif sign == "^":
            coordinates = (x, y+1)
        visited.add(coordinates)
    return visited


santa_visited = set_of_houses(santa)
robo_santa_visited = set_of_houses(robo_santa)
together_visited = santa_visited.union(robo_santa_visited)

print("Santa and his robot visited " + str(len(together_visited)) + " houses.")










 

