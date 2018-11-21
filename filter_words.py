import sys

source_filename = sys.argv[1]
word_length = int(sys.argv[2])
final_file = sys.argv[3]

with open(source_filename, "r", encoding="cp1251") as f:
    with open(final_file, "w", encoding="utf-8") as l:
        for word in f.readlines():
            if len(word) == word_length + 1:  # with \n
                l.write(word)
