#Name:          Lucas Hasting
#Class:         DA 460
#Date:          12/7/2025
#Instructor:    Dr. Imbrogno
#Description:   Get summary stats of kdl.csv file
#Sources:       ChatGPT was used for syntax

#import libraries
import pandas as pd

#open the data file
df = pd.read_csv('kdl.csv')

#get all columns for screen data
columns = []

for i in range(40):
    for j in range(4):
        columns.append(f"screen{i+1}_{j}")

#run summary stats on screen only data - numeric
print(df[columns].stack().describe(), end='\n')
print("Name: Screen Data", end='\n\n')

#get all columns for tile data
columns = []

for i in range(41):
    for j in range(4):
        columns.append(f"tile{i+1}_{j}")

#run summary stats on tile only data - numeric
print(df[columns].stack().describe(), end='\n')
print("Name: Tile Data", end='\n\n')

#run summary stats on kirby's scroll x-value data - numeric
print(df["kirby_x_scrol"].describe(), end='\n\n')

#run summary stats on kirby's scroll y-value data - numeric
print(df["kirby_y_scrol"].describe(), end='\n\n')

#run summary stats on kirby's x-value data - numeric
print(df["kirby_x"].describe(), end='\n\n')

#run summary stats on kirby's y-value data - numeric
print(df["kirby_y"].describe(), end='\n\n')

#run summary stats on boss health data - numeric
print(df["boss_health"].describe(), end='\n\n')

#run summary stats on game state data - nominal
print(df["game_state"].value_counts(), end='\n\n')

#run summary stats on move data - nominal, output/prediction variable
print(df["move"].value_counts(), end='\n\n')

