vowels = 'aeiou'
word = 'education'
count = 0

for char in word:
    if char in vowels:
        count += 1
print(f'Total vowels in {word} are {count}')
