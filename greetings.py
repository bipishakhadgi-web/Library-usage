import emoji

name = input("Enter your name:")

print("Hello", name + "!", emoji.emojize(":smile:"))

activity=input("What is your favorite activity?")

print("Enjoy", activity + "!", emoji.emojize(":thumbs_up:"))
print("Keep Learning", activity, emoji.emojize(":red_heart:"))