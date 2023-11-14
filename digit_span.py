# Import necessary libraries
import random
import time
import pygame
import os
import pandas as pd
import keyboard

# Set working directory
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

# Define functions

def generate_numbers_list(n):
    numbers_list = []
    for i in range(n):
        numbers_list.append(random.randint(0, 9))
    return numbers_list


def play_audio(number, sound_model):
    pygame.mixer.init()
    # set file path
    path = 'Soundmodels/' + str(sound_model) + '/'
    # get file name
    if number == 0:
        pygame.mixer.music.load(path + 'null.mp3')
    elif number == 1:
        pygame.mixer.music.load(path + 'yks.mp3')
    elif number == 2:
        pygame.mixer.music.load(path + 'kaks.mp3')
    elif number == 3:
        pygame.mixer.music.load(path + 'kolm.mp3')
    elif number == 4:
        pygame.mixer.music.load(path + 'neli.mp3')
    elif number == 5:
        pygame.mixer.music.load(path + 'viis.mp3')
    elif number == 6:
        pygame.mixer.music.load(path + 'kuus.mp3')
    elif number == 7:
        pygame.mixer.music.load(path + 'seitse.mp3')
    elif number == 8:
        pygame.mixer.music.load(path + 'kaheksa.mp3')
    elif number == 9:
        pygame.mixer.music.load(path + 'yheksa.mp3')
    
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)


# Predefine variables
os.system('cls')
status = True
mistakes_in_a_row = 0
loop_nr = 0

# Start the game
print('Welcome to digit span!')

# Ask for user's name
name = input('Please enter your name: ')
os.system('cls')

# Get current date
current_date = time.strftime("%d/%m/%Y")

# ask for user's conditions

# Practice or testing mode, practice 1, test 2
while True:
    print('Please choose mode:')
    print('1. Practice')
    print('2. Test')
    mode = input('---> ')
    if mode in {'1', '2'}:
        break
    else:
        print("Please enter a valid option.")
os.system('cls')

# how comfortable is the environment, 1 - not comfortable, 10 - very comfortable
while True:
    print('1 - NOT COMFORTABLE, 10 - VERY COMFORTABLE')
    location = input('How comfortable is the environment right now?')
    if location in {'1', '2', '3', '4', '5', '6', '7', '8', '9', '10'}:
        break
    else:
        print("Please enter a valid option.")
os.system('cls')

# tiredness level, 1 - not tired, 10 - tired
while True:
    print('1 - NOT TIRED, 10 - VERY TIRED')
    tiredness = input('How tired are you right now?')
    if tiredness in {'1', '2', '3', '4', '5', '6', '7', '8', '9', '10'}:
        break
    else:
        print("Please enter a valid option.")
os.system('cls')

# physical activity minutes
while True:
    print('Enter your active minutes for today:')
    physical_activity = input('How many activity minutes have you got today?')
    if physical_activity.isdigit():
        break
    else:
        print("Please enter a valid number.")
os.system('cls')

# mental state, 1 - not focused, 10- focused
while True:
    print('1 - NOT FOCUSED, 10 - VERY FOCUSED')
    mental_state = input('How focused are you right now?')
    if mental_state in {'1', '2', '3', '4', '5', '6', '7', '8', '9', '10'}:
        break
    else:
        print("Please enter a valid option.")
os.system('cls')

# motivation level, 1 - not motivated, 10 - very motivated
while True:
    print('1 - NOT MOTIVATED, 10 - VERY MOTIVATED')
    motivation = input('How motivated are you right now?')
    if motivation in {'1', '2', '3', '4', '5', '6', '7', '8', '9', '10'}:
        break
    else:
        print("Please enter a valid option.")
os.system('cls')

# Ask for starting n and ensure it is a number
while True:
    n_input = input('Please enter starting number count: ')
    if n_input.isdigit():
        n = int(n_input)
        break
    else:
        print("Please enter a valid number.")
os.system('cls')

# Ask for sound model and ensure it is a valid option
while True:
    print('Please enter sound model number:')
    print('1. Kaarel')
    print('2. Pille')
    print('3. Bot')
    sound_model = input('---> ')
    if sound_model in {'1', '2', '3'}:
        break
    else:
        print("Please enter a valid option.")
os.system('cls')

# ask for wait time between numbers'
if mode == '1':
    wait_time = float(input('Please enter wait time between numbers in seconds: '))
elif mode == '2':
    wait_time = 0
os.system('cls')

# ask for memory method, 1 - no method, 2 - memory palace
while True:
    print('Please choose memory method that you practiced today: ')
    print('1. No method')
    print('2. Memory palace (visualization mnemonics)')
    print('3. Memory palace (name mnemonics)')
    print('4. Memory palace (connection mnemonics)')
    memory_method = input('---> ')
    if memory_method in {'1', '2', '3', '4'}:
        break
    else:
        print("Please enter a valid option.")
os.system('cls')

# Display game rules
print('Rules:')
print('1. You will hear a series of numbers')
print('2. You have to repeat the numbers in the same order')
print('3. If you repeat the numbers correctly, the series will get longer')
print('4. If you make a mistake, the series will stay the length once. Additional mistakes will shorten the series by one')
print('________________________')
print('Press enter to start')
input()
os.system('cls')

# Check if log file exists
if os.path.isfile('Logs/' + name + '_digit_span_log.csv'):
    df = pd.read_csv('Logs/' + name + '_digit_span_log.csv')
    session_nr = df['session_nr'].iloc[-1] + 1
else:
    df = pd.DataFrame(columns=['name', 'date', 'time', 'session_nr', 'loop_nr', 'numbers', 'user_number', 'outcome', 'mistakes_in_a_row',
                               'time_taken', 'sound_model', 'length', 'session_time', 'wait_time', 'memory_method', 'tiredness',
                               'physical_activity', 'mental_state', 'motivation', 'location', 'session_mode'])
    session_nr = 1
    
# start whole game timer
start_time_game = time.time()

# Game loop
while status:
    loop_nr += 1
    current_loop_n = n
    
    # Generate list of numbers
    numbers_list = generate_numbers_list(n)
    numbers_string = ''.join(str(number) for number in numbers_list)
    numbers_string = str(numbers_string)

    # Disable keyboard using import keyboard
    for i in range(150):
        keyboard.block_key(i)
    
    # Play audio for all numbers in the list
    for number in numbers_list:
        play_audio(number, sound_model)
        time.sleep(wait_time)

    # Measure time
    start_time = time.time()

    # Enable keyboard
    for i in range(150):
        keyboard.unblock_key(i)
    
    # Ask user to repeat numbers
    print('Current number length is ' + str(current_loop_n) + ' numbers')
    print('Please repeat the numbers in one line')
    user_number = str(input('--->'))
    os.system('cls')
    

    # Stop time measurement
    end_time = time.time()
    time_taken = end_time - start_time

    # Check if user repeated numbers correctly
    if user_number == numbers_string:
        outcome = 'correct'
        print('Correct!')
        n += 1
        mistakes_in_a_row = 0
    else:
        outcome = 'incorrect'
        print('Incorrect!')
        mistakes_in_a_row += 1
        if mistakes_in_a_row > 1:
            n -= 1

    # calculate total session time in hours, minutes and seconds
    session_time = time.strftime("%H:%M:%S", time.gmtime(time.time() - start_time_game))
    
    # Compose data
    data = {'name': name, 'date': current_date, 'time': time.strftime("%H:%M:%S"), 'session_nr': session_nr, 'loop_nr': loop_nr, 'numbers': numbers_string,
            'user_number': str(user_number), 'outcome': outcome, 'mistakes_in_a_row': mistakes_in_a_row, 'time_taken': time_taken, 'sound_model': sound_model,
            'length': current_loop_n, 'session_time': session_time, 'wait_time': wait_time, 'memory_method': memory_method, 'tiredness': tiredness,
            'physical_activity': physical_activity, 'mental_state': mental_state, 'location': location, 'motivation': motivation, 'session_mode': mode}

    # Add data to dataframe
    df = pd.concat([df, pd.DataFrame(data, index=[0])], ignore_index=True)
    
    # print elapsed time in hours, miutes and seconds
    print('__________________________')
    print('Time elapsed: ' + time.strftime("%H:%M:%S", time.gmtime(time.time() - start_time_game)))
    # print current loop number and length of series
    print('Current round number is: ' + str(loop_nr))
    print('Next number length: ' + str(n))
    print('__________________________')

    # Clear screen and wait for user input
    user_input = input('Press ENTER to continue or type "quit" to quit and save your results to a csv file: ')
    os.system('cls')
    if user_input.lower() == 'quit':
        feedback = input('Please enter your feedback (0 for no feedback) --->')
        # save feedback as a text file with session number, user name and date and time as object
        if feedback != '0':
            with open('Feedback/feedback_session_nr_' + str(session_nr) + '_' + name + '.txt', 'w') as f:
                f.write(feedback)
        status = False
        print('Thank you for playing!')
        # print elapsed time in hours, miutes and seconds
        print('Total time elapsed: ' + time.strftime("%H:%M:%S", time.gmtime(time.time() - start_time_game)))
        df.to_csv('Logs/' + name + '_digit_span_log.csv', index=False)