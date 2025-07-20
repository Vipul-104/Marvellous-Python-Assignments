import pandas as pd

def MarvellousDataset(Dataset):

    df = pd.DataFrame(Dataset)
    df['Total'] = df['Math'] + df['Science'] + df['English'] 
    
    print("Total Column After The Descending Ordefr:")
    DescOrder = df.sort_values(by = 'Total', ascending=False)
    print(DescOrder)
   
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