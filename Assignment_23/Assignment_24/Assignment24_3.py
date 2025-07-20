import pandas as pd

def MarvellousDataset(Dataset):
    line = "*"*69
    print(line)

    df = pd.DataFrame(Dataset) 
    
    df['Gender'] = ['Male','Male','Female'] # Gender Column
    print("Actual Dataframe:")
    print(df)
    print(line)

    print("Dataframe Afer:")
    df = df.groupby('Gender')[['Math', 'Science', 'English']].mean()
    print(df)
    print(line)

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