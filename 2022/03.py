with open("data\data_03.txt", encoding="utf-8") as file:
    data = file.read().split("\n")


"PUZZLE no. 1"

def find_errors(rucksacks):
    """"Returns list of wrongly added items in rucksacks."""

    errors = list()
    for rucksack in rucksacks:
        half = len(rucksack)//2
        first_comp = set(rucksack[0:half])
        second_comp = set(rucksack[half:])
        errors.append(first_comp.intersection(second_comp))
    return errors


def set_priority(letter):
    """"Returns priority[int] of a given letter[str]."""

    letter = str(letter)[2]
    if letter.islower():
        priority = ord(letter) - 96
    if letter.isupper():
        priority = ord(letter) - 38
    return priority


def count_total(puzzle_input):
    """"Returns total sum of priorities based on found errors in rucksacks."""

    errors = find_errors(puzzle_input)
    priorities = []
    for error in errors:
        priorities.append(set_priority(error))
    return sum(priorities)


print(f"Total sum of priorities based on found errors is {count_total(data)}.")


"PUZZLE no. 2"

def find_badges(rucksacks):
    """"Returns list of badges."""

    badges = list()
    for i in range(0, len(rucksacks), 3):
        badge = set(rucksacks[i]).intersection(rucksacks[i+1], rucksacks[i+2])
        badges.append(badge)
    return badges


def count_total_for_badges(puzzle_input):
    """"Returns total sum of priorities based on found badges."""

    badges = find_badges(puzzle_input)
    priorities = []
    for badge in badges:
        priorities.append(set_priority(badge))
    return sum(priorities)


print(f"Total sum of priorities based on found badges is {count_total_for_badges(data)}.")