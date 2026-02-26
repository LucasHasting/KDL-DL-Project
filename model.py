#Name:          Lucas Hasting
#Class:         MA 395
#Date:          ~/~/~
#Instructor:    Dr. Terwilliger
#Description:   Course Project - Build/Test DT model for Kirby's Dream Land
#               https://scikit-learn.org/stable/api/index.html

#include data wrangling library
import pandas as pd

#include plotting library
import matplotlib.pyplot as plt

#include model libraries
from sklearn.tree import DecisionTreeClassifier, export_text
from sklearn.neighbors import KNeighborsClassifier

#include test and accuracy libraries
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score, ConfusionMatrixDisplay

#include library used to save models
import joblib

#min-max norm function
def min_max_normalization(x, old_min, old_max, new_min, new_max):
    return ((x - old_min) / (old_max - old_min) * (new_max - new_min) + new_min)

#get data from csv
df = pd.read_csv('kdl2.1.csv')

#split data into dependent/independent variables
df = df[df["state"] != "NOTHING"]
y = df["state"]
df.drop("move", axis=1, inplace=True)
df.drop("state", axis=1, inplace=True)

#transform data
df = pd.get_dummies(df, columns=['game_state'], prefix='state', dtype=int)
for i in df.columns[df.columns.str.startswith('state_')]:
    lst = df[i].to_list()
    lst = [min_max_normalization(x, 0, 1, 0, 255) for x in lst]
    df[i] = pd.DataFrame(lst)

#min-max norm - kirby_x
lst = df["kirby_x"].to_list()
lst = [min_max_normalization(x, 0, 65535, 0, 255) for x in lst]
df["kirby_x"] = pd.DataFrame(lst)

#min-max norm - kirby_y
lst = df["kirby_y"].to_list()
lst = [min_max_normalization(x, 0, 65535, 0, 255) for x in lst]
df["kirby_y"] = pd.DataFrame(lst)

X = df

#Found max_depth in separate program
clf = DecisionTreeClassifier(random_state=42, max_depth=20) # Initialize the classifier
clf.fit(X, y) # Train the classifier

#save model
joblib.dump(clf, "DT.pkl")
print("DONE")
