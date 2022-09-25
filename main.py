import os
import time
import random

colorend = '\033[0m'

easy = ['The quick brown fox jumps over the lazy dog.']
medium = [
    'The mark of the immature man is that he wants to die nobly for a cause, while the mark of the mature man is that he wants to live humbly for one.'
]
hard = [
    'Never imagine yourself not to be otherwise than what it might appear to others that what you were or might have been was not otherwise than what you had been would have appeared to them to be otherwise.'
]


def printdelay(string, dobreaker=True):
    """Prints text with a delay, based on how long each line is"""
    string = string.split('\n')
    if dobreaker:
        print(breaker)
    for i in string:
        print(i)

        # if i == '':
        #   continue

        # delay = len(list(i)) * 0.015

        # if i[0] == '*':
        #   delay = len(list(i)) * 0.01

        # if delay < 0.2:
        #   delay = 0.3

        # time.sleep(delay)
    if dobreaker:
        print(breaker)

breaker = f"\033[1;33m{'*'*5} {'~'*40} {'*'*5}{colorend}"

printdelay(f"""
\033[1;33mWelcome to Sands of Typing!{colorend}

This program, desert and sand themed, is the \033[0;31mall-in-one package{colorend} for typing. It includes benchmarks, different tests based on \033[0;34mwords and length{colorend}, and a place for you to practice typing. Your tests will be \033[0;32mtimed and recorded{colorend} using an hourglass filled with sand. You will select options by typing into the Python console.
\n\033[1mGood Luck!{colorend}
""")

printdelay(
    f"""\033[1mOptions
\033[0;34m(1) Camel Racing (start a test)
\033[0;32m(2) Visit the Sand Bar (view my previous times)
\033[0;31m(3) Scour the Dunes (improve your typing skills){colorend}
Please select one of these options (1, 2, or 3) by typing it into the console below.
""", False)

while True:
    response = input()
    if response in ['1', 'one', 's'] or response.startswith('start'):
        os.system('clear')
    
        printdelay(f"""\033[1;34mCamel Racing (typing test){colorend}\n
\033[1mDifficulty Options
\033[0;32m(1) Carcross (easy)
\033[0;33m(2) Gobi (medium)
\033[0;31m(3) Sahara (hard){colorend}
    """)
    
        selectedtext = []
        while True:
            difficulty = input('Please select one of these options (1, 2, or 3) by typing it into the console below.\n\n')
    
            if difficulty.lower() in ['1', 'easy', 'carcross', 'one']:
                selectedtext = [random.choice(easy), 'easy']
                break
            elif difficulty.lower() in ['2', 'medium', 'gobi', 'two']:
                formatted = True
                selectedtext = [random.choice(medium), 'medium']
                break
            elif difficulty.lower() in ['3', 'hard', 'sahara', 'three']:
                formatted = True
                selectedtext = [random.choice(hard), 'hard']
                break
            continue
    
        os.system('clear')
        printdelay(f"""\033[1mSelected difficulty: \033[0;32m{selectedtext[1]}{colorend}
				
When you see the text appear, you will have some time to prepare, depending on how long the text is. Then, type it out as fast as you can. The test ends when you press \033[1mENTER, so be sure not to press it before then.
    """)
        isready = input('Please type ready when you are ready to start.\n\n')

        if isready.lower() != 'ready':
		        while True:
		            isready = input('Please type ready when you are ready to start.\n')
		            if isready.lower() == 'ready':
		                break

        os.system('clear')
        printdelay(f"""\033[1mYour text is:{colorend}\n
\033[1;34m{selectedtext[0]}{colorend}\n
Take this time to read the text. You will see "GO!" when you are allowed to start. Press ENTER when you have finished the test.
""")
        time.sleep(2)
        now = int(round(time.time() * 1000))
        typed = input('GO!\n\n')
        elapsed = round(int(round(time.time() * 1000)) - now) / 1000
        perminute = 60 / elapsed

        totalletters = len(list(selectedtext))
        typedletters = len(list(typed))
				
        difference = abs(totalletters - typedletters)
        accuracy = round((1 - (difference / typedletters) )) * 100

        cpm = typedletters / perminute
        rawwpm = cpm / 4.7
        abswpm = rawwpm * accuracy
			
        os.system('clear')
        printdelay(f"""You typed:\n
\033[1;34m{typed}{colorend}\n
Your stats:\n
- Time Taken: {elapsed}s
- Accuracy: {accuracy}%
- Characters Per Minute: {cpm}
- Raw Words Per Minute: {rawwpm}
- Words Per Minute: {abswpm}
- perminute: {perminute}
""")