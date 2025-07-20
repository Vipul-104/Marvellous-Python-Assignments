import pandas as pd

def MarvellousDataset(Dataset):

    df = pd.DataFrame(Dataset) 
    
    Minmath = df['Math'].min()
    Maxmath = df['Math'].max()

    #(x' }=(x - min(value) / (max(value) - min(value))
    df['MathNormalized'] = (df['Math'] - Minmath) / (Maxmath - Minmath)

    print("Dataframe After the Min - max Scaling:")
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