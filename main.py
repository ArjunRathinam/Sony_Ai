import webbrowser
import speech_recognition as sr
import wikipedia
import requests
import bs4
import random
import pyttsx3
import datetime

info_data = ["arjun is the creator of me , he is currently in college, he loves programming and has a great depth of "
             "knowledge in it."]

hi_word = ['fine sir how about you?', '“Thanks for asking sir! I’m excellent. How about you?”', 'I am fine, thanks']

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
rate = engine.getProperty('rate')


def speak(audio):
    engine.setProperty('rate', 150)
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning!")

    elif 12 <= hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("Hi sir sony here , how was your day today hope all was fine.")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        query_audio = r.recognize_google(audio, language='en-in')
        print("Recognizing...")
        print(f"User said: {query_audio}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query_audio


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'search' in query:
            speak('sure sir.....')
            item = input("what do you want to search for: ")
            speak(f"opening {item} sir...")
            webbrowser.open("https://www.google.com/search?q=" + item)

        elif 'kill power' in query:
            speak("sure sir.... have a great day")
            exit()

        elif 'how are you' in query:
            random_repl1 = random.choice(hi_word)
            speak(random_repl1)
            print(random_repl1)

        elif 'set a reminder' in query:
            import time

            print("What shall I remind you about?")
            text = str(input())
            print("In how many minutes?")
            local_time = float(input())
            local_time = local_time * 60
            time.sleep(local_time)
            print(text + "remainder complete")
            speak("remainder complete")

        elif 'idiot' in query:
            speak("I am sorry to hear that sir, but i will keep improving")

        elif 'who are you' in query:
            speak(info_data)

        elif 'who is your creator' in query:
            speak(info_data)

        elif 'thanks' in query:
            speak("for you sir , always...")

        elif 'in which language are you programmed' in query:
            speak("I think iam programmed in python")

        elif 'today was the worst day' in query:
            speak("Oh! , sorry to hear that sir... now let me make you happy , let's play some games")
            speak("opening rock paper scissors")

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
                speak("You typed an invalid number, you lose!")
            elif user_choice == 0 and computer_choice == 2:
                print("You win !")
                speak("You win")
            elif computer_choice == 0 and user_choice == 2:
                print("You lose")
                speak("you lose")
            elif computer_choice > user_choice:
                print("You lose")
                speak("you lose")
            elif user_choice > computer_choice:
                print("You win!")
                speak("You win")
            elif computer_choice == user_choice:
                print("It's a draw")
                speak("It's a draw sir")

        elif 'help me in maths' in query:
            speak("opening calculator sir...")

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

        elif 'find weather' in query:
            city = input("type the city name: ")
            # Generating the url
            url = "https://google.com/search?q=weather+in+" + city
            # Sending HTTP request
            request_result = requests.get(url)
            # Pulling HTTP data from internet
            soup = bs4.BeautifulSoup(request_result.text
                                     , "html.parser")
            # Finding temperature in Celsius.
            # The temperature is stored inside the class "BNeawe".
            temp = soup.find("div", class_='BNeawe').text
            print(f' the temperature in {city} is {temp}')

        elif 'start engine' in query:
            speak('sure sir, starting search engine...')

            text = input("what do you want to search for: ")
            url = 'https://google.com/search?q=' + text

            # Fetch the URL data using requests.get(url),
            # store it in a variable, request_result.
            request_result = requests.get(url)

            # Creating soup from the fetched request
            soup = bs4.BeautifulSoup(request_result.text,
                                     "html.parser")
            heading_object = soup.find_all('h3')

            # Iterate through the object
            # and print it as a string.
            for info in heading_object:
                print(info.getText())
                print("------")
