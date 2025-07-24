#Load The Data

import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score,confusion_matrix

def CheckAccuracy(x_train,x_test,y_train,y_test):
    accuracy_scores = []
    K_range = range(1,14)
    
    for i in K_range:
        model = KNeighborsClassifier(n_neighbors=i)
        model.fit(x_train,y_train)
        y_pred = model.predict(x_test)
        accuracy = accuracy_score(y_test,y_pred)
        accuracy_scores.append(accuracy)

    best_K = K_range[accuracy_scores.index(max(accuracy_scores))]
    print("Best value Of the K is : ",best_K)

    model = KNeighborsClassifier(n_neighbors= best_K)
    model.fit(x_train,y_train)
    y_pred = model.predict(x_test)
    accuracy = accuracy_score(y_test, y_pred)

    print("Accuracy is : ",accuracy*100)

    cm = confusion_matrix(y_test,y_pred)
    print("The Confusion Matrics is :",cm)


def MarvellousPlayPredictKNN(Datapath):
    df = pd.read_csv(Datapath)
    print(df.head())
    print("The Dimnssions Of The Dataset is: ")
    print(df.shape)

    df.drop(labels=['Unnamed: 0'],axis='columns',inplace=True)
    print(df.head())

    #Encoding:
    label_Encoder = LabelEncoder()
    df['Play'] = label_Encoder.fit_transform(df['Play'])
    df['Whether'] = label_Encoder.fit_transform(df['Whether'])
    df['Temperature'] = label_Encoder.fit_transform(df['Temperature'])

    print("Updated DataSet is :")
    print(df.head())

    x = df.drop(labels='Play', axis='columns')
    y = df['Play']

    x_train,x_test,y_train,y_test = train_test_split(x,y, test_size=0.2, random_state=42)
    CheckAccuracy(x_train,x_test,y_train,y_test)
    

def main():
    MarvellousPlayPredictKNN("PlayPredictor.csv")
   
if __name__ == "__main__":
    main()