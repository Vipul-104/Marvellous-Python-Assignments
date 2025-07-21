import pandas as pd

def main():
    data = {'Department':['HR','IT','FInance','HR','IT']}

    df = pd.DataFrame(data)
    print(df)

    df = pd.get_dummies(df, columns=['Department'])
    print(df)

    # df['Department'] = df['Department'].map({'HR':0, 'IT':1, 'Finance':2})
    # print(df)


if __name__ == "__main__":
    main()