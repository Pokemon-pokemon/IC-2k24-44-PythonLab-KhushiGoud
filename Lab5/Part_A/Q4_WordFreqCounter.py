# Word Frequency Counter

text = input("Enter a sentence or paragraph: ")

# Convert text to lowercase
text = text.lower()

# Remove common punctuation
for symbol in ".,!?;:":
    text = text.replace(symbol, "")

# Split text into words
words = text.split()

# Count frequency using dictionary
frequency = {}

for word in words:
    frequency[word] = frequency.get(word, 0) + 1

print("\nWord Frequency:")
print(frequency)


# 1. Display words with frequency greater than 1
repeated_words = {
    word: count
    for word, count in frequency.items()
    if count > 1
}

print("\nRepeated Words:")
print(repeated_words)


# 2. Find the most frequent word
if frequency:
    highest_count = max(frequency.values())

    most_frequent = [
        word for word, count in frequency.items()
        if count == highest_count
    ]

    print("\nMost Frequent Word(s):")
    print(most_frequent)
    print("Frequency:", highest_count)
else:
    print("No words entered!")


# 3. Display words in alphabetical order
print("\nWords in Alphabetical Order:")

for word in sorted(frequency):
    print(word, ":", frequency[word])


# 4. Display total number of words
print("\nTotal Words:", len(words))