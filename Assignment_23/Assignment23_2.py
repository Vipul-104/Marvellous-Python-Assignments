import pandas as pd

def MarvellousDataset(Dataset):

    df = pd.DataFrame(Dataset)
    
    print("The Sescriptivr Statistic of the Datast is :")
    print(df.describe())
   
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