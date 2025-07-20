import pandas as pd

def MarvellousDataset(Dataset):

    df = pd.DataFrame(Dataset)
    df['Total'] = df['Math'] + df['Science'] + df['English'] 
    
    print("Dataframe After The Replacement: ")
    df.loc[df['Name'] == 'Pooja', 'Name'] = 'Puja' # Loc method is to Replace
    print(df.head())

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