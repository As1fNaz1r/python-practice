text = "apple banana apple orange banana apple"
words = text.split()
counts = {}
for word in words:
    counts[word] = counts.get(word, 0) + 1

from collections import Counter
counts = Counter(words)
