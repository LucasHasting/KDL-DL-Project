# Kirby's Dream Land - Deep Learning Project
## Table of Contents

- [Project Overview](#project-overview)
- [Build Instructions - The Project](#build-instructions---the-project)
- [Build Instructions - The API (Future Work)](#build-instructions---the-api-future-work)
- [Sources](#sources)

## Project Overview
A report of this project can be read here (WIP), and a presentation of the project can be found here (WIP).

For this project, we used deep reinforcement learning to learn how to play Kirby's Dream Land on the Nintendo Gameboy using Gym Retro, Q-Learning, and PyTorch. The following table includes a description of the files used in the project:

| File/Folder             | Description                                                                      |
|-------------------------|----------------------------------------------------------------------------------|
| [KirbysDreamLand-GameBoy](https://github.com/LucasHasting/KDL-DL-Project/tree/main/KirbysDreamLand-GB) | The integrated game KirbysDreamLand.                                           |
| [train.py](https://github.com/LucasHasting/KDL-DL-Project/tree/main/train.py) | The driver program used to train the agents. |
| [functions.py](https://github.com/LucasHasting/KDL-DL-Project/tree/main/functions.py) | Includes helpful functions, the most helpful being the reward function. |
| [kirbyBoss.py](https://github.com/LucasHasting/KDL-DL-Project/tree/main/kirbyBoss.py) | Includes all methods used for the Q-Learning Algorithm, and includes model hyper-parameters. |
| [kirbyNet.py](https://github.com/LucasHasting/KDL-DL-Project/tree/main/kirbyNet.py) | The Neural Network used for the target/online network. |
| [logger.py](https://github.com/LucasHasting/KDL-DL-Project/tree/main/logger.py) | Includes several methods used for logging results. |
| [wrappers.py](https://github.com/LucasHasting/KDL-DL-Project/tree/main/wrappers.py) | Includes several wrappers used for extending the behavior of Gym Retro. |

Files included for potential future work, or are just helpful are listed below:
| File/Folder             | Description                                                                      |
|-------------------------|----------------------------------------------------------------------------------|
| [check.py](https://github.com/LucasHasting/KDL-DL-Project/blob/main/check.py) | File used to check to see if CUDA is enabled/can be used. |
| [kdl_state.zip](https://github.com/LucasHasting/KDL-DL-Project/blob/main/kdl_state.zip) | zip file that contains kdl.csv (the data used to create the decision tree) |
| [game_data_record.py](https://github.com/LucasHasting/KDL-DL-Project/blob/main/game_data_record.py) | File used to manually record game data with ways to manually classify states. |
| [DT.pkl](https://github.com/LucasHasting/KDL-DL-Project/blob/main/DT.pkl) | Binary data for the decision tree object. |
| [params.py](https://github.com/LucasHasting/KDL-DL-Project/blob/main/params.py) | File used to conduct a parameter search for model.py using the holdout method. |
| [model.py](https://github.com/LucasHasting/KDL-DL-Project/blob/main/model.py) | File used to build the scikit-learn model. |
| [api.py](https://github.com/LucasHasting/KDL-DL-Project/blob/main/api.py) | API used to make predicions using a scikit-learn model - in the file we use DT.pkl (a decision tree model). |
| [game_data_test.py](https://github.com/LucasHasting/KDL-DL-Project/blob/main/game_data_test.py) | File used to test the API. |

State files that can be used for train.py are listed below:

| File/Folder             | Description                                                                      |
|-------------------------|----------------------------------------------------------------------------------|
| [KirbysDreamLand-GameBoy/beginning.state](https://github.com/LucasHasting/KDL-DL-Project/blob/main/KirbysDreamLand-GB/begginning.state) | The beginning of the game. |
| [KirbysDreamLand-GameBoy/boss1.state](https://github.com/LucasHasting/KDL-DL-Project/blob/main/KirbysDreamLand-GB/boss1.state) | Poppy Bros. Sr. |
| [KirbysDreamLand-GameBoy/boss2.state](https://github.com/LucasHasting/KDL-DL-Project/blob/main/KirbysDreamLand-GB/boss2.state) | Whispy Woods |
| [KirbysDreamLand-GameBoy/boss3.state](https://github.com/LucasHasting/KDL-DL-Project/blob/main/KirbysDreamLand-GB/boss3.state) | Lololo/Lalala (mini-boss) |
| [KirbysDreamLand-GameBoy/boss4.state](https://github.com/LucasHasting/KDL-DL-Project/blob/main/KirbysDreamLand-GB/boss4.state) | Lololo/Lalala (boss) |
| [KirbysDreamLand-GameBoy/boss5.state](https://github.com/LucasHasting/KDL-DL-Project/blob/main/KirbysDreamLand-GB/boss5.state) | Kabula |
| [KirbysDreamLand-GameBoy/boss6.state](https://github.com/LucasHasting/KDL-DL-Project/blob/main/KirbysDreamLand-GB/boss6.state) | Kraco Jr. |
| [KirbysDreamLand-GameBoy/boss7.state](https://github.com/LucasHasting/KDL-DL-Project/blob/main/KirbysDreamLand-GB/boss7.state) | Kraco |
| [KirbysDreamLand-GameBoy/boss8.state](https://github.com/LucasHasting/KDL-DL-Project/blob/main/KirbysDreamLand-GB/boss8.state) | King DeDeDe |

Models created that can be loaded can be downloaded [here](https://drive.google.com/drive/folders/16GwztSHmjUXrzZdCYKxPJaLNn5nWr3sl?usp=sharing). The name of the file corresponds to the boss it is associated with. The Poppy Bros. Sr. model was used on both Lololo/Lalala fights.

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

Now, you can open idle (python version 8.0) and open->run train.py to execute the project. 

## Build Instructions - The API (Future Work)
The API is designed to work with the project (see the report for more details), so ensure the project has been built first. Next, ensure the latest python version (64-bit) is installed, it can be installed [here](https://www.python.org/downloads/).

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

## Sources 
* Old Project (this project expands the idea of this project): https://github.com/LucasHasting/Kirby-Dream-Land-AI
* Similar Project: https://raw.githubusercontent.com/lixado/PyBoy-RL/main/README/report.pdf
* Mario RL Tutorial: https://docs.pytorch.org/tutorials/intermediate/mario_rl_tutorial.html
* Atari Project: https://arxiv.org/abs/1312.5602 
* Kirby's Dream Land RAM Map: https://datacrystal.tcrf.net/wiki/Kirby%27s_Dream_Land/RAM_map
* Wiki on Kirby's Dream Land: https://kirby.fandom.com/wiki/Kirby%27s_Dream_Land 
* Inspiration for the project: https://www.youtube.com/watch?v=9YyQJIuN7n0

Theory:
* Machine Learning (breif intro): https://mitsloan.mit.edu/ideas-made-to-matter/machine-learning-explained 
* Deep Learning: http://www.deeplearningbook.org (Chapters 5, 6, and 9 are the most helpful)
* Holdout Method: https://mlbenchmarks.org/04-holdout-method.html 
* (extra) Convolutional Neural Networks: https://www.ibm.com/think/topics/convolutional-neural-networks 
* ADAM: https://www.geeksforgeeks.org/deep-learning/adam-optimizer
* Normalization: https://en.wikipedia.org/wiki/Feature_scaling

Gym Retro Related:
* https://openai.com/index/gym-retro/ 
* https://retro.readthedocs.io/en/latest/
* https://github.com/openai/retro/releases/tag/f347d7e
* https://stackoverflow.com/questions/71973392/importerror-cannot-import-rendering-from-gym-envs-classic-control
* https://github.com/openai/retro/issues/253

Other
* [FastAPI](geeksforgeeks.org/python/fastapi-uvicorn/#:~:text=Last%20Updated%20:%2023%20Jul%2C%202025,server%20interface%20for%20asynchronous%20frameworks.)
* [scikit-learn](https://scikit-learn.org/stable/api/index.html)
* [PyTorch](https://docs.pytorch.org/docs/stable/index.html)
* Applications of Reinforcement Learning: https://arxiv.org/pdf/1908.06973 
