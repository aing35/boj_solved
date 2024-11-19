word = input().strip()

for i in range(len(word)):
    if (i + 1) % 10 != 0:
        print(f"{word[i]}", end = '')
    else:
        print(f"{word[i]}")