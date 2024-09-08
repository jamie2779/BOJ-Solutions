word = input()

words = []

for i in range(1, len(word)-1):
    for j in range(i+1, len(word)):
        new = word[:i][::-1]+word[i:j][::-1]+word[j:][::-1]
        words.append(new)

words.sort()
print(words[0])