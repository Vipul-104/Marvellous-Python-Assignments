import pandas as pd
import matplotlib.pyplot as plt


def MarvellousDataset(Dataset):
    line = "*"*69
    print(line)

    df = pd.DataFrame(Dataset) 
    x = df[df['Name'] == 'Sagar'][['Math','Science','English']].iloc[0]

    plt.figure(figsize=(8,9))
    plt.pie(x, labels=x.index)
    plt.title("Sagar's Marks")
    plt.show()

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