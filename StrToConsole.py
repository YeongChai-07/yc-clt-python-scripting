# First approach: Directly placing the string to print through the print() function.
print("HyperDimension\nNeptunia\nAction\nUnleashed\nDynasty\nWarriors\n")
# Second approach: Using List to store the words to print out through print() function.
word_to_print_list = ["HyperDimension", "Neptunia", "Action", "Unleashed", "Dynasty", "Warriors"]
# Printing the items in the list through List Comprehension approach
[print(my_word) for my_word in word_to_print_list]