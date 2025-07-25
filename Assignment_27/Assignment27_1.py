import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn import metrics
import matplotlib.pyplot as plt

def main():
    df = pd.read_csv("Advertising.csv")
    print(df.head())

    df.drop(labels='Unnamed: 0', axis="columns", inplace=True)
    print(df.head())

    print("The Null Values in The Dataset",df.isnull().sum())

    print("Statistics of Teh Datasets:")
    print(df.describe())

    print("Correlation matrix is :")
    print(df.corr())

    x = df[['TV','radio', 'newspaper']]
    y = df['sales']

    x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2, random_state=42)
    model = LinearRegression()
    model.fit(x_train,y_train)
    y_pred = model.predict(x_test)
    
    MSE = metrics.mean_squared_error(y_test,y_pred)
    RMSE = np.sqrt(MSE)
    r2 = metrics.r2_score(y_test,y_pred)

    print("Value of mean squared Error is:",MSE)
    print("Value of root mean squared Error is:",RMSE)
    print("Value of r2 :",r2)

    print("Model Coefficient are : ")
    for col, coef in zip(x.columns, model.coef_):
        print(f"{col} : {coef}")

    print("Y Intersept is:", model.intercept_)

    plt.figure(figsize=(8,5))
    plt.scatter(y_test, y_pred, color = 'blue')
    plt.xlabel("Actul sales")
    plt.ylabel("Predicted Sales")
    plt.title("Marvellous infosystems Advertisement")
    plt.grid(True)
    plt.show()

if __name__ == "__main__":

    main()