import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score
import matplotlib.pyplot as plt

import seaborn as sns
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler

from sklearn.ensemble import VotingClassifier



def main():
    line = "-"*120
    print(line)
    diabetes = pd.read_csv('diabetes.csv')
    print(diabetes.head())
    print(line)

    print("The Dimenssions of the dataset:")
    print(diabetes.shape)
    print(line)

    print("Handeling Null Values:")
    print(line)
    Handel_null = diabetes.isnull()
    print(Handel_null)
    print(line)

    print("Description of the Dataset:")
    print(line)
    print(diabetes.describe())
    print(line)

    plt.figure(figsize=(10,6))
    sns.heatmap(diabetes.corr(), annot=True, cmap='coolwarm')
    plt.title('Diabetes Predictor')
    plt.show()

    x = diabetes.drop(columns=['Outcome'])
    y = diabetes['Outcome']

    scalar = StandardScaler() #Applicable on Numeric Value Only
    x_Scaled = scalar.fit_transform(x)

    x_train,x_test,y_train,y_test = train_test_split(x_Scaled,y, test_size=0.2,random_state=42)

    log_clf = LogisticRegression()
    dt_clf = DecisionTreeClassifier(max_depth=8)
    knn_clf = KNeighborsClassifier(n_neighbors=5)

    voting_clf = VotingClassifier(
        estimators=[
            ('lr',log_clf),
            ('dt',dt_clf),
            ('knn', knn_clf)
        ],
        voting='hard'
    )

    voting_clf.fit(x_train,y_train)

    y_pred = voting_clf.predict(x_test)

    accuracy = accuracy_score(y_test,y_pred)*100
    print("Accuracy is:",accuracy)

if __name__ == "__main__":
    main()