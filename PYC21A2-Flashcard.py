class Flashcard:
    def __init__(self, word, meaning):
        self.word = word
        self.meaning = meaning

    def __str__(self):
        return f"Word: {self.word}, Meaning: {self.meaning}"
    
print("Welcome to the Flashcard application.")
flash = []

while True:
    word = input("Enter a word: ")
    meaning = input(f"Enter the mening of the word {word}: ")
    flash.append(Flashcard(word, meaning))

    option = int(input("Do you want to add another word?\n1. Yes\n0. No\nEnter your choice: "))

    if option:
        continue
    else:
        break
print("\nYour flashcards are: \n")
i=1
for word in flash:
    print(f"Card#{i}: {word}")
    i+=1