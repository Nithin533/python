def word_count_and_frequency(sentence):
    words = sentence.split()
    count = len(words)
    freq = {}

    for word in words:
        word = word.lower()  # make it case-insensitive
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1

    return count, freq

# Test the function
sentence = input("Enter a sentence: ")
count, freq = word_count_and_frequency(sentence)

print(f"\nThe number of words in the sentence is: {count}")
print("The frequency of each word is:")
for word in freq:
    print(f"{word}: {freq[word]}")
  
