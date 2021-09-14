words = input().split()
word_counter = {}

for word in words:
    word = word.lower()

    if word_counter.get(word):
        word_counter[word] += 1
    else:
        word_counter[word] = 1

for key, val in word_counter.items():
    print(key, val)
