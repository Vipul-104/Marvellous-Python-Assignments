import pandas as pd

def main():
    data = {'Salary':[25000,27000,29000,31000,50000,100000]}

    df = pd.DataFrame(data)

    Q1 = df['Salary'].quantile(0.25)
    Q3 = df['Salary'].quantile(0.75)

    IQR = Q3 - Q1

    Lower_Bound = Q1 - 1.5 * IQR
    Upper_Bound = Q3 + 1.5 * IQR

    outliers = df[(df['Salary'] < Lower_Bound) | (df['Salary'] > Upper_Bound)]

    print("Lower Bound is :  ",Lower_Bound)
    print("Lower Bound is :  ",Upper_Bound)
    print("Outliers are:")
    print(outliers)


if __name__ == "__main__":
    main()