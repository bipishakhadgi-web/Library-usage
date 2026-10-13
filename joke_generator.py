import pyjokes

for i in range(3):
    joke=pyjokes.get_joke()
    print("Joke", i + 1, ":", joke)

answer=input("Do you want another joke? (Y/N):")

while answer.lower() == "yes":
    joke=pyjokes.get_jokes()
    print("Here is another joke:", joke)

    answer=input("Do you want another joke? (Y/N):")

print("Thank you for using the joke generator!")