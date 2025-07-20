import pandas as pd
import matplotlib.pyplot as plt


def MarvellousDataset(Dataset):
    line = "*"*69
    print(line)

    df = pd.DataFrame(Dataset)

    Total = {'Total': [0] * len(df['Name'])}

    for i in range(len(Dataset['Name'])):
        Total['Total'][i] = int(df['Math'][i]) + int(df['Science'][i]) +int(df['English'][i])
    df['Total'] = Total['Total']

    print(df)
    

    Status = {'Status':[0] * len(df['Name'])}

    for i in range(len(Dataset['Name'])):
        if(df['Total'][i] >= 250):
            Status['Status'][i] = 'pass'
        else:
            Status['Status'][i] = 'fail'

    df['Status'] = Status['Status']
    print(df)

def main():

    data = {
            'Name': ['Amit', 'Sagar', 'Pooja'],
            'Math': [85, 90, 78],
            'Science': [92, 88, 80],
            'English': [75, 85, 82],

        }

    MarvellousDataset(data)

if __name__ == "__main__":
    main()