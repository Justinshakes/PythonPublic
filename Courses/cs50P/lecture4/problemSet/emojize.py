import emoji

# Prompt the user to enter an input
user_input = input("Input: ")

# Use the emoji library to convert the input into emojis
converted_input = emoji.emojize(user_input)

# Print the converted input
print(converted_input)
