#Name:          Lucas Hasting
#Class:         DA 460
#Date:          12/7/2025
#Instructor:    Dr. Imbrogno
#Description:   Course Project - Record game data and movements made by the player of Kirby's Dream Land
#               - q to quit, z = a, x = b, arrow keys to move
#Sources:       ChatGPT was used for syntax
#               https://retro.readthedocs.io/en/latest/index.html

#import libraries
import retro
import time
import keyboard
import pandas as pd

#set the frames per second
FPS = 60

#the starting game state
STATE_FILE = "begginning.state"

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
def load_data(info, move):
    screen_data = load_other_data(info, 40, "screen")
    tile_data = load_other_data(info, 41, "tile")
    boss_health = info["boss_health"]
    kirby_x_scrol = info["kirby_x_scrol"]
    kirby_x = info["kirby_x"]
    kirby_y_scrol = info["kirby_y_scrol"]
    kirby_y = info["kirby_y"]
    game_state = info["game_state"]

    return [*screen_data, *tile_data, game_state, boss_health, kirby_y, kirby_y_scrol, kirby_x_scrol, kirby_x, move]

#write the data to a csv file
def write_to_csv(data, filename):
    #create column names
    column = []

    for i in range(40):
        for j in range(4):
            column.append(f"screen{i+1}_{j}")

    for i in range(41):
        for j in range(4):
            column.append(f"tile{i+1}_{j}")

    column += ["game_state", "boss_health", "kirby_y", "kirby_y_scrol"]
    column += ["kirby_x_scrol", "kirby_x", "move"]

    #save file
    df = pd.DataFrame(data, columns=column)
    df.to_csv(filename, index=False)

#function is a new renderer that uses the FPS to determine speed
def new_render(env):
    time.sleep(1/FPS)
    env.render()

def main():
    #start gym retro enviornment
    env = retro.make('KirbysDreamLand-GB',STATE_FILE)
    env.reset()

    #declare a and b inputs on keyboard
    a = "z"
    b = "x"

    #create list to store data
    data = []

    while(True):
        #determine action from keyboard, if q is pressed, quite game and store data
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
        elif (keyboard.is_pressed('q')):
            break

        #make the action
        ob, rew, done, info = env.step(action)
        new_render(env)

        #record the data
        data.append(load_data(info, move))

    #close the gym retro enviornment
    env.render(close=True)
    env.close()

    #write data to file
    write_to_csv(data, "kdl.csv")

    print("FINISHED!")

main()
