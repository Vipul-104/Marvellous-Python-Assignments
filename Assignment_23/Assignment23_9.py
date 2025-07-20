import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def MarvellousDataset(Dataset):

    df = pd.DataFrame(Dataset)
    
    meanMath = df['Math'].mean()
    meanSci = df['Science'].mean()

    df['Math'].fillna(meanMath, inplace=True)
    df['Science'].fillna(meanSci, inplace=True)

    print(df.head())
   
def main():

    data2 = {
            'Name': ['Amit', 'Sagar', 'Pooja'],
            'Math': [np.nan , 76, 88],
            'Science': [91, np.nan, 85],

        }

    MarvellousDataset(data2)

if __name__ == "__main__":
    main()