with open("data\data_05.txt", encoding="utf-8") as file:
    data = file.read().split("\n")

# input: stack organization at the beginning
stacks = ["ZJG", "QLRPWFVC", "FPMCLGR", "LFBWPHM", "GCFSVQ", "WHJZMQTL", "HFSBV", "FJZS", "MCDPFHBT"]

instruction_list = []
for line in data:
    instructions = list(''.join(i for i in line if i.isdigit()))
    if len(instructions) == 4:
        instructions[0] = instructions[0] + instructions[1]
        instructions.remove(instructions[1])
    instruction_list.append(instructions)


# PUZZLE no. 1

for instruction in instruction_list:
    moving = stacks[int(instruction[1]) - 1][- int(instruction[0]):]
    stacks[int(instruction[2]) - 1] += moving[::-1]
    stacks[int(instruction[1]) - 1] = stacks[int(instruction[1]) - 1][:- int(instruction[0])]

result = []
for stack in stacks:
    result.append(stack[-1])

print(f"Solution of first part is:")
print("".join(result))


# PUZZLE no. 2

stacks = ["ZJG", "QLRPWFVC", "FPMCLGR", "LFBWPHM", "GCFSVQ", "WHJZMQTL", "HFSBV", "FJZS", "MCDPFHBT"]

for instruction in instruction_list:
    moving = stacks[int(instruction[1]) - 1][- int(instruction[0]):]
    stacks[int(instruction[2]) - 1] += moving
    stacks[int(instruction[1]) - 1] = stacks[int(instruction[1]) - 1][:- int(instruction[0])]

result = []
for stack in stacks:
    result.append(stack[-1])

print(f"Solution of second part is:")
print("".join(result))