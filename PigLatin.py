message = input("Enter the English message to convert into Pig Latin ")

VOWELS = ('a', 'e', 'i', 'o', 'u')

pig_latin = []  # A list of words in Pig Latin

for word in message.split():  # Seperate the non-letters at the start of this word
    prefix_nonletters = ''
    while len(word) > 0 and not word[0].isalpha():
        prefix_nonletters += word[0]
        word = word[1:]

    if len(word) == 0:
        pig_latin.append(prefix_nonletters)
        continue
        # Separate the nonletters at the end of the word

    suffix_nonletters = ''
    while not word[-1].isalpha():
        suffix_nonletters += word[-1]
        word = word[:-1]
        # Remember if the word was in uppercase or title case

    was_upper = word.isupper()
    was_title = word.istitle()

    word = word.lower()  # make the word lower case for translation

    # Separate the constants at the start of this word
    prefix_constants = ''
    while len(word) > 0 and not word[0] in VOWELS:  # If length of word is greater than zero and prefix_constants
        # isn't contained in VOWELS
        prefix_constants += word[0]  # Add the prefix_constants to word[index position zero]
        word = word[1:]  # Word equals word[index position 1 plus every other index position in word]

    # Add the Pig Latin ending to the word
    if prefix_constants != '':  # If prefix_constants doesn't equal nothing
        word += prefix_constants + 'ay'  # Take word + 'ay'
    else:
        word += 'yay'
        # Set the word back to uppercase or title case
    if was_upper:
        word = word.upper()
    if was_title:
        word = word.title()
        # Add the non letters back to the start or the end of the word
    pig_latin.append(prefix_nonletters + word + suffix_nonletters)

    # Join all the words back together
print(' '.join(pig_latin))
print(f"{' '.join(pig_latin)} = {message}")