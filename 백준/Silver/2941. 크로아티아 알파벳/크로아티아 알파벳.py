import sys

word = sys.stdin.readline().strip()

croatian_alphabet = {"dz=": 0, "z=": 1, "s=": 2, "nj": 3, "lj": 4, "d-": 5, "c-": 6, "c=": 7}

for i in croatian_alphabet.keys():
  if i in word:
    word = word.replace(i, str(croatian_alphabet[i]))


sys.stdout.write(f"{len(word)}")
