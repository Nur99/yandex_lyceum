words = input().split()
sorted_words = sorted(words, key=lambda word: word.lower())
print(*sorted_words)
