import pandas as pd

def MarvellousDataset(Dataset):

    df = pd.DataFrame(Dataset)
    
    print("The Dimensions of the Datasts are :")
    print(df.shape)

    print("The Columns in the Dataset are: ")
    print(df.keys())

    print("The DataTyeps Are :")
    print(df.dtypes)

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