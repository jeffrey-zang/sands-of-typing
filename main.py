import json
import os
import time
import random
from datetime import datetime

# texts from 0-150 characters in length
with open('lib/easy.json', 'r', encoding="mbcs") as file:
    easy = json.load(file)
    file.close()
    
# texts from 150-250 characters in length
with open('lib/medium.json', 'r', encoding="mbcs") as file:
    medium = json.load(file)
    file.close()

# texts 250+ characters in length
with open('lib/hard.json', 'r', encoding="mbcs") as file:
    hard = json.load(file)
    file.close()

user = []  # array of all tests done by user
colorend = '\033[0m'  # python ansi colour code ending

def printdelay(string, dobreaker=True):
    """Prints text with a delay, based on how long each line is"""
    string = string.split('\n')
    if dobreaker:
        print(breaker)
    for i in string:
        print(i)

        if i == '':
            continue

        delay = len(list(i)) * 0.015

        if i[0] == '*':
            delay = len(list(i)) * 0.01

        if delay < 0.2:
            delay = 0.3

        time.sleep(delay)
    if dobreaker:
        print(breaker)


def printoptions():
    """Prints menu options"""
    printdelay(
        f"""\n\033[1mOptions
            \033[0;34m(1) Camel Racing (start a test)
            \033[0;32m(2) Visit the Sand Bar (view my previous times)
            \033[0;31m(3) Scour the Dunes (improve your typing skills)
            \033[0;30m(0) ***EXIT THE PROGRAM***{colorend}
            Please select one of these options (1, 2, or 3) by typing it into the console below.
            """, False)
    


breaker = f"\033[1;33m{'*' * 5} {'~' * 40} {'*' * 5}{colorend}"

printdelay(f"""
\033[1;33mWelcome to Sands of Typing!{colorend}

This program, desert and sand themed, is the \033[0;31mall-in-one package{colorend} for typing. It includes benchmarks, different tests based on \033[0;34mwords and length{colorend}, and a place for you to practice typing. Your tests will be \033[0;32mtimed and recorded{colorend} using an hourglass filled with sand. You will select options by typing into the Python console.
\n\033[1mGood Luck!{colorend}
""")

printoptions()

while True:
    response = input()
    if response in ['0', 'zero', 'exit', 'quit']:
        print("Thanks for playing!\nExiting...\n")
        exit(0)
    
    if response in ['1', 'one', 's'] or response.startswith('start'):
        os.system('clear')

        printdelay(f"""\033[1;34mCamel Racing (typing test){colorend}\n
\033[1mDifficulty Options
\033[0;32m(1) Mojave (easy)
\033[0;33m(2) Gobi (medium)
\033[0;31m(3) Sahara (hard){colorend}
    """)

        selectedtext = []
        color = '\033[0;32m'
        while True:
            difficulty = input(
                'Please select one of these options (1, 2, or 3) by typing it into the console below.\n\n'
            )

            if difficulty.lower() in ['1', 'easy', 'mojave', 'one']:
                selectedtext = [random.choice(easy), 'easy']
                break
            elif difficulty.lower() in ['2', 'medium', 'gobi', 'two']:
                formatted = True
                selectedtext = [random.choice(medium), 'medium']
                color = '\033[0;33m'
                break
            elif difficulty.lower() in ['3', 'hard', 'sahara', 'three']:
                formatted = True
                selectedtext = [random.choice(hard), 'hard']
                color = '\033[0;31m'
                break
            continue

        os.system('clear')
        printdelay(
            f"""\033[1mSelected difficulty: {color}{selectedtext[1]}{colorend}
				
When you see the text appear, DO NOT START. You will have some time to prepare, depending on how long the text is. Then, type it out as fast as you can. The test ends when you press \033[1mENTER, so be sure not to press it before then.
    """)
        isready = input('Please type ready when you are ready to start.\n\n')

        if isready.lower() != 'ready':
            while True:
                isready = input(
                    'Please type ready when you are ready to start.\n')
                if isready.lower() == 'ready':
                    break

        os.system('clear')
        printdelay(f"""\033[1mYour text is:{colorend}\n
\033[1;34m{selectedtext[0]}{colorend}\n
Take this time to read the text. You will see "GO!" when you are allowed to start. Press ENTER when you have finished the test.
""")
        print('DON\'T START YET!')
        time.sleep(1)
        print('3')
        time.sleep(1)
        print('2')
        time.sleep(1)
        print('1')
        time.sleep(1)
        now = int(round(time.time() * 1000))
        typed = input('GO!\n\n')
        elapsed = round(int(round(time.time() * 1000)) - now) / 1000
        perminute = 60 / elapsed

        totalletters = len(list(selectedtext[0]))
        typedletters = len(list(typed))

        if typedletters != 0:
            difference = abs(totalletters - typedletters)
            accuracy = 100 - ((difference / typedletters) * 100)
            if accuracy == 0.0:
                accuracy = 100
            if selectedtext[0] != typed:
                if difference >= 2:
                    accuracy -= difference ^ 2
                else:
                    accuracy -= 1

            cpm = typedletters * perminute
            rawwpm = cpm / 4.7
            abswpm = rawwpm * (accuracy / 100)

            os.system('clear')

            now = datetime.now()
            user.append({
                'difficulty': [selectedtext[1], color],
                'wpm': round(abswpm, 2),
                'accuracy': round(accuracy, 2),
                'time': now.strftime("%d/%m/%Y %H:%M:%S")
            })

            placing = random.randint(4, 10)
            if abswpm > 120:
                placing = '1st'
            elif abswpm > 100:
                placing = '2nd'
            elif placing > 90:
                placing = '3rd'
            else:
                placing = f'{placing}th'

            printdelay(f"""You typed:\n
\033[1;34m{typed}{colorend}\n
Your stats:\n
\033[1mWords per minute: {round(abswpm, 2)}{colorend}
Characters per minute: {round(cpm, 2)}
Raw WPM: {round(rawwpm, 2)}

\033[1mAccuracy: {round(accuracy, 2)}%{colorend}
Time Taken: {round(elapsed, 2)}s
Difficulty: {color}{selectedtext[1]}{colorend}

Added to user records.
\033[1;33mYour camel got {placing} place.
  """)

            printoptions()
        else:
            print('Test invalid: no input')
            printoptions()

    if response.lower() in ['2', 'view', 'sand bar', 'two']:
        os.system('clear')
        if user == []:
            print('You don\'t have any recorded times. Do a camel race first!')
            printoptions()
            continue

        averagewpm = 0
        averageacc = 0
        numtests = len(user)

        print(f'{breaker}\n\033[1mYour times:{colorend}')
        for index, i in enumerate(user):
            print(f"""\033[1;34m({index + 1}) - {i['time']}{colorend}
	- Difficulty: {i['difficulty'][1]}{i['difficulty'][0]}{colorend}
	- Words Per Minute: {i['wpm']}
	- Accuracy: {i['accuracy']}
""")
            averagewpm += i['wpm']
            averageacc += i['accuracy']

        print(
            f'Average WPM: {round(averagewpm / numtests, 2)}\nAverage Accuracy: {round(averageacc / numtests, 2)}%\nTotal Tests: {numtests}'
        )
        print(breaker)
        printoptions()

    if response.lower() in ['3', 'improve', 'scour', 'three']:
        os.system('clear')
        printdelay(f"""\033[1mBest typing resources{colorend}\n
Other Typing Tests:
  - monkeytype (monkeytype.com)
  - TypeRacer (play.typeracer.com)
  - KeyMash (keyma.sh)

Learn Typing:
  - keybr.com
  - typingclub.com
  - typing.com

Other Layouts:
  - Dvorak
  - Workman
  - Colemak
""")
        printoptions()
