import pandas as pd

def main():
    data = {'Name':['A', 'B', 'C'], 'Age':[21.0,22.0,23.0]}

    df = pd.DataFrame(data)
    print("The Name Column DataType is:")
    print(df['Name'].dtype)

    print("The Age Column DataType is:")
    print(df['Age'].dtype)

    print("Datatype of Age column After The Conversion :")
    df['Age'] = df['Age'].astype(int)
    print(df['Age'].dtype)




if __name__ == "__main__":
    main()