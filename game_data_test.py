#Name:          Lucas Hasting
#Class:         MA 395
#Date:          ~/~/~
#Instructor:    Dr. Terwilliger
#Description:   Course Project - Test state model with API
#               - q to quit, z = a, x = b, arrow keys to move
#               https://retro.readthedocs.io/en/latest/index.html

#import libraries
import retro
import time
import keyboard
import pandas as pd
import requests

def min_max_normalization(x, old_min, old_max, new_min, new_max):
    return ((x - old_min) / (old_max - old_min) * (new_max - new_min) + new_min)

#set the frames per second
FPS = 60

#the starting game state
STATE_FILE = "begginning.state"
CSV_FILE_NAME = "kdl2.1.csv"

#create map of inputs to position in action array
INPUTS = {
    "A": 8,
    "B": 0,
    "UP": 4,
    "DOWN": 5,
    "LEFT": 6,
    "RIGHT": 7,
    "NONE": -1,
    "DOWN-LEFT": 1,
    "DOWN-RIGHT": 9,
    "UP-LEFT": 2,
    "UP-RIGHT": 3,
    "A-LEFT": 10,
    "A-RIGHT": 11,
    "B-LEFT": 12,
    "B-RIGHT": 13
}

#function used to make an action in the emulator
def make_action(enter):
    action = [0] * 9
    if(INPUTS[enter] == 1):
        action[5] = 1
        action[6] = 1
    elif(INPUTS[enter] == 2):
        action[4] = 1
        action[6] = 1
    elif(INPUTS[enter] == 3):
        action[4] = 1
        action[7] = 1
    elif(INPUTS[enter] == 9):
        action[5] = 1
        action[7] = 1
    elif(INPUTS[enter] == 10):
        action[8] = 1
        action[6] = 1
    elif(INPUTS[enter] == 11):
        action[8] = 1
        action[7] = 1
    elif(INPUTS[enter] == 12):
        action[0] = 1
        action[6] = 1
    elif(INPUTS[enter] == 13):
        action[0] = 1
        action[7] = 1
    elif(INPUTS[enter] == -1):
        pass
    else:
        action[INPUTS[enter]] = 1
    return action, enter

#get all the screen/tile data (there is alot)
def load_other_data(info,n,typ):
    data = []
    for i in range(n):
        for j in range(4):
            data.append(info[f"{typ}{i+1}_{j}"])
    return data

#load in all the data
def load_data(info):
#store the data
    screen_data = load_other_data(info, 40, "screen")
    tile_data = load_other_data(info, 41, "tile")
    boss_health = float(info["boss_health"])
    kirby_x_scrol = float(info["kirby_x_scrol"])
    kirby_x = min_max_normalization(float(info["kirby_x"]), 0, 65535, 0, 255)
    kirby_y_scrol = float(info["kirby_y_scrol"])
    kirby_y = min_max_normalization(float(info["kirby_y"]), 0, 65535, 0, 255)
    game_state = float(info["game_state"])
    game_state_array = [0.0]*9

    #accounts for dummys/min-max norm
    if(game_state == 1):
        game_state_array[0] = 255.0
    elif(game_state == 2):
        game_state_array[1] = 255.0
    elif(game_state == 3):
        game_state_array[2] = 255.0
    elif(game_state == 4):
        game_state_array[3] = 255.0
    elif(game_state == 5):
        game_state_array[4] = 255.0
    elif(game_state == 6):
        game_state_array[5] = 255.0
    elif(game_state == 7):
        game_state_array[6] = 255.0
    elif(game_state == 8):
        game_state_array[7] = 255.0
    elif(game_state == 11):
        game_state_array[8] = 255.0
    
    return {"data" : [*screen_data, *tile_data, boss_health, kirby_y, kirby_y_scrol, kirby_x_scrol, kirby_x, *game_state_array]}

#function is a new renderer that uses the FPS to determine speed
def new_render(env):
    time.sleep(1/FPS)
    env.render()

def main():
    state = ""
    
    #start gym retro enviornment
    env = retro.make('KirbysDreamLand-GB',STATE_FILE)
    env.reset()

    #declare a and b inputs on keyboard
    a = "z"
    b = "x"

    #create list to store data
    data = []

    while(True):
        prev_state = state
        
        #determine action from keyboard
        action, move = make_action("NONE")
        if keyboard.is_pressed('up') and keyboard.is_pressed('left'):
            action, move = make_action("UP-LEFT")
        elif keyboard.is_pressed('up') and keyboard.is_pressed('right'):
            action, move = make_action("UP-RIGHT")
        elif keyboard.is_pressed('down') and keyboard.is_pressed('left'):
            action, move = make_action("DOWN-LEFT")
        elif keyboard.is_pressed('down') and keyboard.is_pressed('right'):
            action, move = make_action("DOWN-RIGHT")
        elif keyboard.is_pressed('left') and keyboard.is_pressed(a):
            action, move = make_action("A-LEFT")
        elif keyboard.is_pressed('right') and keyboard.is_pressed(a):
            action, move = make_action("A-RIGHT")
        elif keyboard.is_pressed('left') and keyboard.is_pressed(b):
            action, move = make_action("B-LEFT")
        elif keyboard.is_pressed('right') and keyboard.is_pressed(b):
            action, move = make_action("B-RIGHT")
        elif keyboard.is_pressed('up'):
            action, move = make_action("UP")
        elif keyboard.is_pressed('down'):
            action, move = make_action("DOWN")
        elif keyboard.is_pressed('left'):
            action, move = make_action("LEFT")
        elif keyboard.is_pressed('right'):
            action, move = make_action("RIGHT")
        elif keyboard.is_pressed(a):
            action, move = make_action("A")
        elif keyboard.is_pressed(b):
            action, move = make_action("B")

        #state change buttons
        elif (keyboard.is_pressed('u')):
            state = "VERTICAL-UP"
        elif (keyboard.is_pressed('j')):
            state = "VERTICAL-DOWN"
        elif (keyboard.is_pressed('h')):
            state = "HORIZONTAL-LEFT"
        elif (keyboard.is_pressed('k')):
            state = "HORIZONTAL-RIGHT"
        elif (keyboard.is_pressed('n')):
            state = "NOTHING"
        elif (keyboard.is_pressed('b')):
            state = "BOSS"
        elif (keyboard.is_pressed('m')):
            state = "DOOR-PRESENT"

        #quit
        elif (keyboard.is_pressed('q')):
            break

        #make the action
        ob, rew, done, info = env.step(action)
        new_render(env)

        #predict state using model api
        url = 'http://127.0.0.1:8000//predict'
        response = requests.post(url, json=load_data(info))
        check = response.json()
        state = check["prediction"]

        if(prev_state != state):
            print(state)

    #close the gym retro enviornment
    env.render(close=True)
    env.close()

    print("FINISHED!")

main()
