# Kirby's Dream Land - Deep Learning Project

(WIP)

## Project Overview
For this project, we used deep reinforcement learning to learn how to play Kirby's Dream Land on the Nintendo Gameboy using Gym Retro. The following table includes a description of the files used in the project:

| File/Folder             | Description                                                                      |
|-------------------------|----------------------------------------------------------------------------------|
| [KirbysDreamLand-GameBoy](https://github.com/LucasHasting/KDL-DL-Project/tree/main/KirbysDreamLand-GB) | The integrated game KirbysDreamLand                                              |
| [kdl_csv.zip](https://github.com/LucasHasting/KDL-DL-Project/blob/main/kdl_csv.zip)                    | zip file that contains kdl.csv (the data used in the project)                |

Files included for potential future work are listed below:
| File/Folder             | Description                                                                      |
|-------------------------|----------------------------------------------------------------------------------|
| [KirbysDreamLand-GameBoy](https://github.com/LucasHasting/KDL-DL-Project/tree/main/KirbysDreamLand-GB) | The integrated game KirbysDreamLand                                              |
| [kdl_csv.zip](https://github.com/LucasHasting/KDL-DL-Project/blob/main/kdl_csv.zip)                    | zip file that contains kdl.csv (the data used in the project)                |

A report of this project can be read here (WIP), and a presentation of the project can be found here (WIP).

## Build Instructions - The Project

First, ensure python version 8.0 (64-bit) is installed, it can be installed [here](https://www.python.org/downloads/release/python-380/) and that git is installed, it can be installed [here](https://git-scm.com/install/). It is highly recommended to use a CUDA GPU (you may need to lookup if your GPU is supported). You can install CUDA drivers [here](https://developer.nvidia.com/cuda-downloads).

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
python -m pip install scikit-learn
python -m pip install matplotlib
python -m pip install pandas
python -m pip install keyboard
python -m pip uninstall -y setuptools
python -m pip install setuptools==65.5.0
python -m pip install git+https://github.com/openai/gym.git@9180d12e1b66e7e2a1a622614f787a6ec147ac40
python -m pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu117
python -m pip install matplotlib
python -m pip install tensordict
python -m pip install torchrl
python -m pip install requests
```

Next, in a separate window, move the KirbysDreamLand-GameBoy folder to the following directory: 
```sh
<directory of python installation>/Lib/site-packages/retro/data/stable/
```

Go back to the terminal/cmd window and run the following command, replace directory with the location of the KirbysDreamLand-GameBoy folder (on windows powershell, replace python with python.exe):

```sh
python -m retro.import <directory>
```

Now, you can open idle (python version 8.0) and open->run project.py to execute the project (train.py). 

## Build Instructions - The API (Future Work)
The API is designed to work with the project, so ensure the project has been built first. Next, ensure the latest python version (64-bit) is installed, it can be installed [here](https://www.python.org/downloads/).

Next, go to where python is installed in the terminal/cmd prompt using 

```sh
cd <directory>
```

The location is different based on the operating system. For windows, it is ```C:\Users\<user>\AppData\Local\Programs\Python\Python<version>```, for linux run the following command to find the path:

```
which python<version>
```

Once in the directory, on the command prompt, run the following commands (on windows, replace python with python.exe):

```sh
python -m pip install scikit-learn
python -m pip install joblib
python -m pip install pydantic
```

Return to the directory of the project in the command line: ```cd <directory>``` and run the following command:

```sh
uvicorn api:app
```

**Note: if you have issues using python, try replacing python with py.**
