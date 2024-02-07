# Use string indexing and string concatenation
# to write the sentence "we see trees" only by picking
# the necessary letters from the given string.

word = "tweezers "

print(word[1:3] + word[8] + word[7] + word[2:4] + word[8] + word[0] + word[6:4:-1] + word[5:8:2])
