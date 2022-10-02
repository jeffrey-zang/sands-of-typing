import os
import time
import random
from datetime import datetime

easy = [  # texts from 0-150 characters in length
    'The quick brown fox jumps over the lazy dog.',
    'Leave something for someone but don\'t leave someone for something.',
    'Believe in one thing too much and you have no room for new ideas.',
    'I am he as you are he as you are me and we are all together.',
    'There will come a time when all of us are dead.',
    'Do something different, but kind of the same.',
    'I can\'t stress enough how much this is not a tutorial.',
    'My first name is Mr. Schattman, and I was born in Austin, Texas, which I profusely apologize for.',
    'However small the chance might be of striking lucky, the chance was there.',
    'If you think anyone is sane you just don\'t know enough about them.',
    'Never gonna give you up, never gonna let you down, never gonna run around and desert you.',
    'At ClockHacks, you will be able to work in teams of up to 4 to create a website, game, app, robot, or whatever tech-related product you want.',
    'All man\'s miseries derive from not being able to sit quietly in a room alone.',
    'Sometimes I wish I never built this palace, but real love is never a waste of time.',
    'Apparently, it only appears to those people who are pure of heart and have a strong desire to see it.',
    'I played video games in a drunken haze, I was 17 years young. Hurt my knuckles punching the machines, the taste of Scotch rich on my tongue.',
    'You can\'t get back what you\'ve lost, what\'s important now is what is it that you still have.',
    'They often wish that people would just once and for all work out where the hell they wanted to be.',
    'Why do they call it oven when you of in the cold food of out hot eat the food?',
    'Mother, I would be most grateful if you let me consume a pastry with a high levels of sugars and simple carbohydrates.',
    'If you are reading this, you are slow. If you are not reading this, you are average.',
    'Step right up and I\'ll guess your weight. Your wait is: 45 minutes!',
    'There are two types of camels: One humped or “dromedary” camels and two humped Bactrian camels.',
    'Camels have three sets of eyelids and two rows of eyelashes to keep sand out of their eyes.',
    'Camels are very strong and can carry up to 900 pounds for 25 miles a day.',
    'Camels can travel at up to 40 miles per hour – the same as a racehorse!',
    'Some camel calves are born completely white and turn brown as their adult coat comes in.'
]
medium = [  # texts from 150-250 characters in length
    'The mark of the immature man is that he wants to die nobly for a cause, while the mark of the mature man is that he wants to live humbly for one.',
    'I have a dream, a fantasy, to help me through reality. And my destination makes it worth the while, pushing through the darkness still another mile.',
    'According to all known laws of aviation, there is no way that a bee should be able to fly. Its wings are too small to get its fat little body off the ground. The bee, of course, flies anyway. Because bees don\'t care what humans think is impossible.',
    'The gentleman cannot be appreciated in small things but is acceptable in great matters. A small man is not acceptable in great matters but can be appreciated in small things.',
    'It\'s important in life to conclude things properly. Only then can you let go. Otherwise you are left with words you should have said but never did, and your heart is heavy with remorse.',
    'There is matter to everything even air or shadow, too small to see. The Cut is something a Summoner can do, but it requires tremendous skill and I would only use it as a last resort. Like that ambush.',
    'There are approximately 1010300 words in the English language, but I could never string enough words together to properly express how much I want to hit you with a chair.',
]

hard = [  # texts 250+ characters in length
    'In this assignment, you will write a Python program of your choosing that shows off what you\'ve learned so far. This is your chance to be creative and expressive, and break free of the draconian, stultifying requirements that we teachers are always imposing on you.',
    'Never imagine yourself not to be otherwise than what it might appear to others that what you were or might have been was not otherwise than what you had been would have appeared to them to be otherwise.',
    'A father may have a child who is ugly and lacking in all the graces, and the love he feels for him puts a blindfold over his eyes so that he does not see his defects but considers them signs of charm and intelligence and recounts them to his friends as if they were clever and witty.',
    'Once upon a time there was a lovely princess. But she had an enchantment upon her of a fearful sort which could only be broken by love\'s first kiss. She was locked away in a castle guarded by a terrible fire-breathing dragon. Many brave knights had attempted to free her from this dreadful prison, but none prevailed. She waited in the dragon\'s keep in the highest room of the tallest tower for her true love and true love\'s first kiss.',
    'Now he saw the familiar wide river beside the path differently. He saw all of the light and color and history it contained and carried in its slow-moving water; and he knew that there was an Elsewhere from which it came, and an Elsewhere to which it was going.',
    'One of the reasons why we crave love, and seek it so desperately, is that love is the only cure for loneliness, and shame, and sorrow. But some feelings sink so deep into the heart that only loneliness can help you find them again. Some truths about yourself are so painful that only shame can help you live with them. And some things are just so sad that only your soul can do the crying for you.',
    "Why, some are born great, some achieve greatness, and some have greatness thrown upon them. I was one, sir, in this interlude; one Sir Topas, sir; but that's all one. By the Lord, fool, I am not mad. But do you remember? Madam, why laugh you at such a barren rascal? an you smile not, he's gagged: and thus the whirligig of time brings in his revenges.",
    "I started the day with some nothin' tea. Nothin' tea is easy to make. First, get some hot water, then add nothin'. I experimented with potato skin tea a few weeks ago. The less said about that the better.",
    'A glooming peace this morning with it brings. The sun for sorrow will not show its head. Go hence to have more talk of these sad things. Some shall be pardoned and some punished. For never was a story of more woe than this of Juliet and her Romeo.',
    'Farewell. We will likely meet again, should destiny dictate. If you mean to pursue the inhumans, follow the guidance of that brand. It reacts strongly to evil. But mind this: Yours is a black path through the night. When you confront those who lurk in the darkness, you also envelop yourself in it. Good journey, struggler.',
    'We can also determine the end behavior of a polynomial function from its equation. This is often helpful while trying to graph the function, as knowing the end behavior helps us visualize the graph at the "ends."',
    'Breyers was made 62 years before Dreyers was made, and Dreyers was made by William J Dreyers. William J Dreyers was a man of selfishness and greed. He strived to make as much currency as possible, and become a man of wealth. On the other hand, creator of Breyers, William A Breyers was a fine man. He wanted to make delicious treats for everybody to enjoy, making the ice cream cheap and tasty.'
]

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
            \033[0;31m(0) ***EXIT THE PROGRAM***{colorend}
            Please select one of these options (1, 2, or 3) by typing it into the console below.
            """, False)
    


breaker = f"\033[1;33m{'*'*5} {'~'*40} {'*'*5}{colorend}"

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
            print(f"""\033[1;34m({index+1}) - {i['time']}{colorend}
	- Difficulty: {i['difficulty'][1]}{i['difficulty'][0]}{colorend}
	- Words Per Minute: {i['wpm']}
	- Accuracy: {i['accuracy']}
""")
            averagewpm += i['wpm']
            averageacc += i['accuracy']

        print(
            f'Average WPM: {round(averagewpm/numtests, 2)}\nAverage Accuracy: {round(averageacc/numtests, 2)}%\nTotal Tests: {numtests}'
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
