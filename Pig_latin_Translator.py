#Get sentence from user
original = input("Enter the sentence: ").strip().lower()

#split the sentence into words

words = original.split()

#loop through words and convert to pig latin

new_words = []


#if it starts with a vovel, just add yay
for word in words:
    if word[0] in "aeiou":
        new_word = word+"yay"
        new_words.append(new_word)
print(new_words)


#otherwise, move the first consonant cluster to end and add "ay"

#stick words back together


#output the final string