words = {}
for i in range(int(input())):
    line = input().lower()
    sort_line = "".join(sorted(line))
    words[sort_line] = words.get(sort_line, set())
    words[sort_line].add(line)

new_words = [" ".join(sorted(value)) for value in words.values() if len(value) > 1]

print("\n".join(sorted(new_words)))

