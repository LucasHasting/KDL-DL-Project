# Kirby's Dream Land - Deep Learning Project

## Project Overview
For this project, ... WIP

| File/Folder             | Description                                                                      |
|-------------------------|----------------------------------------------------------------------------------|
| [KirbysDreamLand-GameBoy](https://github.com/LucasHasting/KDL-DL-Project/tree/main/KirbysDreamLand-GB) | The integrated game KirbysDreamLand                                              |
| [kdl_csv.zip](https://github.com/LucasHasting/KDL-DL-Project/blob/main/kdl_csv.zip)                    | zip file that contains kdl.csv (the data used in the project)                |
| [get_data.py](https://github.com/LucasHasting/KDL-DL-Project/blob/main/get_data.py)                    | python file to data.json used in KirbysDreamLand-GameBoy                 |
| [game_data.py](https://github.com/LucasHasting/KDL-DL-Project/blob/main/game_data.py)                    | python file to create kdl.csv                |
| [summary_statistics.py](https://github.com/LucasHasting/KDL-DL-Project/blob/main/summary_statistics.py)                    | python program to output summary statistics of the data                |

## Build Instructions

First, ensure python version 8.0 is installed, it can be installed [here](https://www.python.org/downloads/release/python-380/).

Next, go to where python is installed in the terminal/cmd prompt using 

```sh
cd <directory>
```

The location is different based on the operating system. For windows, it is ```C:\Users\<user>\AppData\Local\Programs\Python\Python38```, for linux run the following command to find the path:

```
which python38
```

Once in the directory, on the command prompt, run the following commands (on windows, replace python with python.exe):

```sh
python -m pip install --upgrade pip
python -m pip install gym-retro
python -m pip install gym==0.21
python -m pip install scikit-learn
python -m pip install matplotlib
python -m pip install pandas
python -m pip install keyboard
```

Next, in a separate window, move the KirbysDreamLand-GameBoy folder to the following directory: 
```sh
<directory of python installation>/Lib/site-packages/retro/data/stable/
```

Go back to the terminal/cmd window and run the following command, replace directory with the location of the KirbysDreamLand-GameBoy folder (on windows, replace python with python.exe):

```sh
python -m retro.import <directory>
```

Now, you can open idle (python version 8.0) and open->run project.py to execute the project. 
