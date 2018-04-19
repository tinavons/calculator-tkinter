import Tkinter
import tkMessageBox
import random

secretNumber = random.randint(1, 100)

def check_guess():
    userGuess = int(guessNumberEntry.get())
    result = ""

    if userGuess == secretNumber:
        result = "Congratulations! You guessed the number!"
    elif userGuess > secretNumber:
        result = "Your guess is too big."
    else:
        result = "Your guess is too small. "
    tkMessageBox.showinfo("Rezultat", result)


window = Tkinter.Tk()

window.geometry("400x200")

greetingsLabel = Tkinter.Label(window, text = "Welcome to the game")
greetingsLabel.pack() #s .pack pripnemo element na window

guessNumberLabel = Tkinter.Label(window, text = "Enter the number")
guessNumberLabel.pack()

guessNumberEntry = Tkinter.Entry(window)
guessNumberEntry.pack()

guessNumberButton = Tkinter.Button(window, text= "Guess", command=check_guess)
guessNumberButton.pack()


window.mainloop()

