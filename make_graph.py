import json
import sys

source_filename = sys.argv[1]
destination_filename = sys.argv[2]
new_dictionary = {}


def one_letter(first_word, second_word):
    counter = 0
    for i in range(len(first_word)):
        if first_word[i] != second_word[i]:
            counter += 1
    return counter == 1


with open(source_filename, "r", encoding="utf-8") as f:
    file_content = list(f.readlines())
    previous_percent = -1
    for i, word in enumerate(file_content):
        new_list = []

        # completion percentage
        percent = i // (len(file_content) // 100)
        if previous_percent != percent:
            print(percent, '%')
            previous_percent = percent

        for other_word in file_content:
            if one_letter(word, other_word):
                new_list.append(other_word[:-1])

        true_word = word[:-1]  # remove \n в конце
        new_dictionary[true_word] = new_list

with open(destination_filename, "w", encoding='utf-8') as f:
    json.dump(new_dictionary, f, ensure_ascii=False)  # fighting with encoding (cyrillic)
