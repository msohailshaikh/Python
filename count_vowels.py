### Count Vowels – Enter a string and the program counts the number of vowels in the text. For added complexity have it report a sum of each vowel found.

myString = "SohailSOHAIL"
counts = {i:0 for i in 'aeiouAEIOU'}
for char in myString:
    if char in counts:
        counts[char] += 1

for k,v in counts.items():
    print(k,v)


