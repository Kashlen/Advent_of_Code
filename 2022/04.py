with open("data\data_04.txt", encoding="utf-8") as file:
    data = file.read().split("\n")

pairs = []
for item in data:
    pairs.append(item.split(","))

full_list_of_sections = []
for part in pairs:
    elf_1 = range(int((part[0].split("-"))[0]), int((part[0].split("-"))[1])+1)
    elf_2 = range(int((part[1].split("-"))[0]), int((part[1].split("-"))[1])+1)
    list_1 = []
    for n in elf_1:
        list_1.append(n)
    list_2 = []
    for m in elf_2:
        list_2.append((m))
    list_of_two = [list_1, list_2]
    full_list_of_sections.append(list_of_two)


"PUZZLE no. 1"

def count_full_overlaps(list_of_ranges):
    """Return number of full overlaps in section ranges between two elves. Takes list of section ranges in lists
    by pair of elves. """

    counter = 0
    for part in list_of_ranges:
        if (int((part[0].split("-"))[0]) <= int((part[1].split("-"))[0])) and (int((part[0].split("-"))[1]) >= int((part[1].split("-"))[1])):
            counter +=1
        elif (int((part[0].split("-"))[0]) >= int((part[1].split("-"))[0])) and (int((part[0].split("-"))[1]) <= int((part[1].split("-")[1]))):
            counter +=1
    return counter


print(f"{count_full_overlaps(pairs)} ranges of sections fully overlap.")


"PUZZLE no. 2"

def count_no_overlaps(list_of_ranges):
    """Return number of section ranges which don't overlap between two elves at all. Takes list of section ranges in lists
    by pair of elves. """

    counter = 0
    for part in list_of_ranges:
        if int((part[0].split("-"))[1]) < int((part[1].split("-"))[0]):
            counter +=1
        elif int((part[0].split("-"))[0]) > int((part[1].split("-"))[1]):
            counter +=1
    return counter


print(f"{len(pairs)-(count_no_overlaps(pairs))} ranges of sections overlap.")