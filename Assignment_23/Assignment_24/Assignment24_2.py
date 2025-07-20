import pandas as pd

def MarvellousDataset(Dataset):
    line = "*"*69
    print(line)

    df = pd.DataFrame(Dataset) 
    
    df['Gender'] = ['Male','Male','Female'] # Gender Column

    print(df)
    print(line)

    df['Gender'] = df['Gender'].map({'Male':1, 'Female':0}) # one-hot Encoding

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