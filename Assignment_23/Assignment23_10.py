import pandas as pd
import matplotlib.pyplot as plt

def MarvellousDataset(Dataset):

    df = pd.DataFrame(Dataset)

    df.drop(columns=['English'], inplace=True)

    df['Total'] = df['Math'] + df['Science']
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