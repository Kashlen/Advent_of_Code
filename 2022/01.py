with open ("data\data_01_a.txt", encoding = "utf-8") as file:
    data = file.read()

# Puzzle no. 1

calories_by_elf = data.split("\n\n")
list_of_totals = []
for elf in calories_by_elf:
    elf_cals = elf.split("\n")
    total_calories = 0
    for item in elf_cals:
        item_cals = int(item)
        total_calories += item_cals
    list_of_totals.append(total_calories)

print(f"Elf with largest amount of calories carries {max(list_of_totals)} cal.")

# Puzzle no. 2

highest_cals = []
for count in range(3):
    count = max(list_of_totals)
    highest_cals.append(count)
    list_of_totals.remove(count)
print(f"Top three elves carry {sum(highest_cals)} cals in total.")











