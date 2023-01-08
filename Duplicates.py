word_to_check: str = input('Give me word or a sentence to check')
word_to_check = word_to_check.replace(' ','')
list_of_chars = list(word_to_check)
duplicates = []

print("Your word/sentence: " + word_to_check)
print(f"Lets made a list of letters out of it: {list_of_chars}")

for i in list_of_chars:
    count = list_of_chars.count(i)
    if count > 1 and i not in duplicates:
        duplicates.append(i)
        print(f"List of duplicates: {duplicates}")
