from encodings import utf_8
import datetime

start = datetime.datetime.now()

with open ("data\data_05.txt", encoding="utf_8") as file:
    dataset = file.read()

# 1st part

strings = list(dataset.split("\n"))

def has_3_vowels(string):
    vowels = ["a", "e", "i", "o", "u"]
    string_vowels_list = list()
    for letter in string:
        for vowel in vowels:
            if letter == vowel:
                string_vowels_list.append(vowel)
    if len(string_vowels_list) >= 3:
        return True
    else:
        return False
            
def has_double_letters(string):
    for x in string:
        if x+x in string:
            return True
    else:
        return False

def has_naughty_strings(string):
    naughty_strings = ["ab", "cd", "pq", "xy"]
    for naughty in naughty_strings:
        if naughty in string:
            return True
    else:
        return False


def how_many_nice(data):
    nice_strings = list()
    for string in data:
        if has_naughty_strings(string) == False and has_3_vowels(string) and has_double_letters(string):
            nice_strings.append(string)
    print(len(nice_strings))
    

how_many_nice(strings)

print("Runtime: {0}".format(datetime.datetime.now()-start))



# 2nd part

def has_double_letters_twice(string):
    for x in range(0, len(string)-1):
        for y in range(x+2, len(string)-1):
            if string[x:x+2] == string[y:y+2]:
                return True
    else:
        return False

def has_xyx_alike_string(string):
    for x in string:
        for y in string:
            if x+y+x in string:
                return True
    else:
        return False


def how_many_new_nice(data):
    nice_strings = list()
    for string in data:
        if has_double_letters_twice(string) and has_xyx_alike_string(string):
            nice_strings.append(string)
    print(len(nice_strings))

how_many_new_nice(strings)

#It contains a pair of any two letters that appears at least twice in the string without overlapping, like xyxy (xy) or aabcdefgaa (aa), but not like aaa (aa, but it overlaps).
#It contains at least one letter which repeats with exactly one letter between them, like xyx, abcdefeghi (efe), or even aaa.