import datetime
import wikipedia  # pip install wikipedia
import webbrowser
import os
import pyttsx3
import random
import time
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *

data = []

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        talk("Good morning sir")

    elif hour >= 12 and hour < 18:
        talk('Good afternoon sir')

    else:
        talk('Good evening sir')


def takeCommand():
    # It takes microphone input from the user and returns string output
    command = input("How may i help you sir ")
    try:
        print(f"user said: {command}")
        query = command


    except Exception as e:
        print(e)
        print("Say that again sir...")
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    while True:
        # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            talk('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            talk(results)
            print("According to Wikipedia")
            print(results)


        elif 'open youtube' in query:
            talk("opening youtube")
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            talk("opening google")
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            talk("opening stackoverflow")
            webbrowser.open("stackoverflow.com")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            talk(f"Sir, the time is {strTime}")
            print(f"Sir, the time is {strTime}")

        elif 'who am i jarvis' in query:
            talk("Sir , your name is Arjun , you are the one who created me")
            print("Sir , your name is Arjun , you are the one who created me")

        elif 'open udemy' in query:
            talk("opening udemy")
            webbrowser.open("udemy.com")

        elif 'open python.org' in query:
            talk("opening python.org")
            webbrowser.open("python.org")

        elif 'who are my best friends' in query:
            talk("Sir , your best friends are Shreyas,Advick,Taizen and myself!")
            print("Sir , your best friends are Shreyas,Advick,Taizen and myself!")

        elif 'thanks buddy' in query:
            talk("You're most welcome sir !")
            print("You're most welcome sir !")

        elif 'who developed you jarvis?' in query:
            talk("Yourself sir!")
            print("Yourself sir!")

        elif 'in which language are you programmed jarvis' in query:
            talk("Iam programmed in Python")
            print("Iam programmed in Python")

        elif 'bye buddy' in query:
            talk("Bye sir ! have a nice day")
            print("Bye sir!")

        elif 'open gmeet' in query:
            talk("opening google meet")
            webbrowser.open("meet.google.com")
        elif 'open github' in query:
            talk("opening github sir")
            webbrowser.open("github.com")
        elif 'open my codingal website' in query:
            talk("opening your site sir")
            webbrowser.open("https://arjunrathinam.github.io/The-seven-continents-of-the-world-/")

        elif 'when is your birthday jarvis' in query:
            talk("sir! my birthday falls on 3rd january")
            print("sir! my birthday falls on 3rd january")

        elif 'jarvis open calculator' in query:

            # addition
            def addition(n1, n2):
                return n1 + n2


            # subraction
            def subraction(n1, n2):
                return n1 - n2


            # division
            def division(n1, n2):
                return n1 / n2


            # multiplication
            def multiplication(n1, n2):
                return n1 * n2


            operations = {
                "+": addition, "-": subraction,
                "/": division, "*": multiplication
            }

            number_1 = int(input("What is the first number that you would like to enter "))
            number_2 = int(input("What is the second number that you would like to enter "))

            for keys in operations:
                print(keys)
            user_operation_selection = input("Choose any one operation from the following")
            function = operations[user_operation_selection]
            answer = function(number_1, number_2)
            print(f"{number_1} {user_operation_selection} {number_2} = {answer} ")

            print("Thank you for using jarvis calculator , hope you had a wonderful experience with us")


        elif 'jarvis shutdown' in query:
            talk("shutting down sir ....")
            print("shutting down sir ....")
            exit()

        elif 'jarvis open rock paper scissors' in query:
            talk("opening rock paper scissors")

            rock = '''
                _______
            ---'   ____)
                  (_____)
                  (_____)
                  (____)
            ---.__(___)
            '''

            paper = '''
                _______
            ---'   ____)____
                      ______)
                      _______)
                     _______)
            ---.__________)
            '''

            scissors = '''
                _______
            ---'   ____)____
                      ______)
                   __________)
                  (____)
            ---.__(___)
            '''
            user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

            computer_choice = random.randint(0, 2)
            print(f"Jarvis chose:{computer_choice}")

            if user_choice >= 3 or user_choice < 0:
                print("You typed an invalid number, you lose!")
            elif user_choice == 0 and computer_choice == 2:
                print("You win!")
            elif computer_choice == 0 and user_choice == 2:
                print("You lose")
            elif computer_choice > user_choice:
                print("You lose")
            elif user_choice > computer_choice:
                print("You win!")
            elif computer_choice == user_choice:
                print("It's a draw")
        elif "jarvis open hangman game" in query:
            # Step 4

            import random

            stages = ['''
              +---+
              |   |
              O   |
             /|\  |
             / \  |
                  |
            =========
            ''', '''
              +---+
              |   |
              O   |
             /|\  |
             /    |
                  |
            =========
            ''', '''
              +---+
              |   |
              O   |
             /|\  |
                  |
                  |
            =========
            ''', '''
              +---+
              |   |
              O   |
             /|   |
                  |
                  |
            =========''', '''
              +---+
              |   |
              O   |
              |   |
                  |
                  |
            =========
            ''', '''
              +---+
              |   |
              O   |
                  |
                  |
                  |
            =========
            ''', '''
              +---+
              |   |
                  |
                  |
                  |
                  |
            =========
            ''']

            end_of_game = False
            word_list = ["ardvark", "baboon", "camel"]
            chosen_word = random.choice(word_list)
            word_length = len(chosen_word)

            # TODO-1: - Create a variable called 'lives' to keep track of the number of lives left.
            # Set 'lives' to equal 6.
            lives = 6

            # Testing code
            print(f'Pssst, the solution is {chosen_word}.')

            # Create blanks
            display = []
            for _ in range(word_length):
                display += "_"

            while not end_of_game:
                guess = input("Guess a letter: ").lower()

                # Check guessed letter
                for position in range(word_length):
                    letter = chosen_word[position]
                    # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
                    if letter == guess:
                        display[position] = letter

                # TODO-2: - If guess is not a letter in the chosen_word,
                # Then reduce 'lives' by 1.
                # If lives goes down to 0 then the game should stop and it should print "You lose."
                if guess not in chosen_word:
                    lives -= 1
                    if lives == 0:
                        end_of_game = True
                        print("You lose.")

                # Join all the elements in the list and turn it into a String.
                print(f"{' '.join(display)}")

                # Check if user has got all letters.
                if "_" not in display:
                    end_of_game = True
                    print("You win.")

                # TODO-3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the
                #  user has remaining.
                print(stages[lives])

        elif "jarvis open secret auction game" in query:
            from art import logo

            print(logo)
            bid = {}


            def highest_bidder(bidding_record):
                highest_bid = 0
                winner = ""
                for bidder in bidding_record:
                    bid_amount = bidding_record[bidder]
                    if bid_amount > highest_bid:
                        highest_bid = bid_amount
                        winner = bidder
                print(f"The winner is {winner} with a bid of {highest_bid}")


            game_finished = False
            while not game_finished:
                bider_name = input("Type your name ")
                bid_price = int(input("Please enter your bid price $ "))
                bid[bider_name] = bid_price
                anyother_bidders = input("Any of the bidders left ")
                if anyother_bidders == "no":
                    game_finished = True
                    highest_bidder(bid)


        elif "jarvis open guess the number game" in query:
            from random import randint

            EASY_LEVEL_TURNS = 10
            HARD_LEVEL_TURNS = 5


            # Function to check user's guess against actual answer.
            def check_answer(guess, answer, turns):
                """checks answer against guess. Returns the number of turns remaining."""
                if guess > answer:
                    print("Too high.")
                    return turns - 1
                elif guess < answer:
                    print("Too low.")
                    return turns - 1
                else:
                    print(f"You got it! The answer was {answer}.")


            # Make function to set difficulty.
            def set_difficulty():
                level = input("Choose a difficulty. Type 'easy' or 'hard': ")
                if level == "easy":
                    return EASY_LEVEL_TURNS
                else:
                    return HARD_LEVEL_TURNS


            def game():

                # Choosing a random number between 1 and 100.
                print("Welcome to the Number Guessing Game!")
                print("I'm thinking of a number between 1 and 100.")
                answer = randint(1, 100)
                print(f"Pssst, the correct answer is {answer}")

                turns = set_difficulty()
                # Repeat the guessing functionality if they get it wrong.
                guess = 0
                while guess != answer:
                    print(f"You have {turns} attempts remaining to guess the number.")

                    # Let the user guess a number.
                    guess = int(input("Make a guess: "))

                    # Track the number of turns and reduce by 1 if they get it wrong.
                    turns = check_answer(guess, answer, turns)
                    if turns == 0:
                        print("You've run out of guesses, you lose.")
                        return
                    elif guess != answer:
                        print("Guess again.")


            game()


        elif "jarvis set a remainder for me" in query:
            user_reminder = input("Name of the event pls sir: ")
            talk("Name of the event please sir")
            reminder_time = input("duration of the event pls sir: ")
            talk("duration of the event please sir")
            data = [user_reminder, reminder_time]
            talk("action done successfully")

        elif "jarvis show my reminders" in query:
            talk(f"sir your remainders are {data}")
            print(data)

        elif "jarvis search google" in query:
            search = input("Sir type something that you want search for : ")
            talk(f"sir searching google for {search}")
            google_result = webbrowser.open("https://www.google.com/search?q=" + search)


        elif "jarvis set a timer for me" in query:
            def countdown(m, s):
                total_seconds = m * 60 + s
                while total_seconds > 0:
                    timer = datetime.timedelta(seconds=total_seconds)
                    print(timer, end="\r")
                    time.sleep(1)
                    total_seconds -= 1
                    print(total_seconds)
                print("Bzzzt! The countdown is at zero seconds!")

            m = input("Enter the time in minutes: ")
            s = input("Enter the time in seconds: ")
            countdown(int(m), int(s))

        elif "jarvis open jarvopad" in query:
            talk("opening jarvopad")
            class jarvopad(Tk):
                def __init__(self):
                    super().__init__()
                    self.title("jarvopad")
                    self.geometry("1000x1000")
                    self.iconbitmap("logo.ico")
                    self.scrollbar = Scrollbar(self)
                    self.scrollbar.pack(side= RIGHT, fill =Y)
                    self.text_box = Text(self, height=100, width=800, wrap=WORD, yscrollcommand=self.scrollbar.set)
                    self.text_box.pack()
                    self.scrollbar.config(command=self.text_box.yview)
                    self.main_menubar = Menu(self)
                    self.rc_menubar = Menu(self, tearoff=0)
                    self.rc_menubar.add_command(label="Select All", command=self.select_all)
                    self.rc_menubar.add_command(label="Cut", command=self.cut)
                    self.rc_menubar.add_command(label="Copy", command=self.copy)
                    self.rc_menubar.add_command(label="Paste", command=self.paste)

                    self.text_box.bind("<Button-3>", self.open_rc_menu)

                    #file

                    self.file_menu = Menu(self.main_menubar, tearoff=0)
                    self.file_menu.add_command(label="New", command=self.new_file)
                    self.file_menu.add_command(label="Open", command=self.open_file)
                    self.file_menu.add_command(label="Save", command=self.save_file)
                    self.file_menu.add_command(label="Exit", command=self.quit)
                    self.main_menubar.add_cascade(label="File", menu=self.file_menu)

                    #Edit

                    self.edit_menu = Menu(self.main_menubar, tearoff=0)
                    self.edit_menu.add_command(label="Select All", command=self.select_all)
                    self.edit_menu.add_command(label="Cut", command=self.cut)
                    self.edit_menu.add_command(label="Copy", command=self.copy)
                    self.edit_menu.add_command(label="Paste", command=self.paste)
                    self.main_menubar.add_cascade(label="Edit", menu=self.edit_menu)

                    #Contact

                    self.help_menu = Menu(self.main_menubar, tearoff=0)
                    self.help_menu.add_command(label="About", command=self.show_about)
                    self.main_menubar.add_cascade(label="Help", menu=self.help_menu)

                    self.config(menu=self.main_menubar)
                    self.mainloop()

                def quit(self):
                    self.destroy()

                def open_rc_menu(self, event):
                    try:
                        self.rc_menubar.tk_popup(event.x_root, event.y_root)
                    finally:
                        self.rc_menubar.grab_release()

                def open_file(self):
                    self.file_path = askopenfilename(defaultextension=".txt",
                                                     filetypes=[("Text Documents", "*.txt"), ("All Files", "*.*")])
                    if not self.file_path:
                        self.file_path = None
                    else:
                        self.title(f"{os.path.basename(self.file_path)} - Notepad")
                        self.text_box.delete("1.0", END)

                        with open(self.file_path) as file:
                            self.text_box.insert("1.0", file.read())

                def new_file(self):
                    self.title("untitled-jarvopad")
                    self.text_box.delete("1.0", END)
                    self.file_path = None

                def save_file(self):
                    try:
                        if self.file_path:
                            pass
                    except AttributeError:
                        self.file_path = None

                    if not self.file_path:
                        self.file_path = asksaveasfilename(initialfile="Untitled.txt",
                                                           defaultextension=".txt",
                                                           filetypes=[("Text Documents", "*.txt"),
                                                                      ("All Files", "*.*")])
                        if not self.file_path:
                            self.file_path = None
                        else:
                            with open(self.file_path, "w") as file:
                                file.write(self.text_box.get("1.0", END))

                            self.title(f"{os.path.basename(self.file_path)} - Notepad")
                    else:
                        with open(self.file_path, "w") as file:
                            file.write(self.text_box.get("1.0", END))

                def show_about(self):
                    showinfo("About", "This is a simple notepad app it has many interesting features and this app "
                                          "is developed by Arjun Rathinam C.G")

                def select_all(self):
                    self.text_box.tag_add(SEL, "1.0", END)

                def cut(self):
                    self.text_box.event_generate("<<Cut>>")

                def copy(self):
                    self.text_box.event_generate("<<Copy>>")

                def paste(self):
                    self.text_box.event_generate("<<Paste>>")


            app = jarvopad()




