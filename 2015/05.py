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
    letters = list(string)
    for x in letters:
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