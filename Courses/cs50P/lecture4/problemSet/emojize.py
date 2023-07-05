import emoji

try:
    user_input = input("Input: ")
    print(emoji.emojize(user_input))
except Exception as e:
    print("An error occurred:", str(e))
