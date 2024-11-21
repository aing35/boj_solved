import sys

word = []

for i in range(5):
    default_word_col = ["10"] * 15
    word_col = list(map(str, sys.stdin.readline().strip()))
    for j in range(len(word_col)):
        default_word_col[j] = word_col[j]
    word.append(default_word_col)

read_word = []

for j in range(15):
    for i in range(5):
        if word[i][j] != "10":
            read_word.append(word[i][j])

sys.stdout.write("".join(read_word))