### Count Words in a String – Counts the number of individual words in a string. For added complexity read these strings in from a text file and generate a summary.

def count_words(my_string):
    counts = dict()
    words = my_string.split()
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts

text = "the quick brown fox jumps over the lazy dog."

print("Total words found : "+ str(len(text.split())))
print(count_words(text))
