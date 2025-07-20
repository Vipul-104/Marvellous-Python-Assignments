import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def MarvellousDataset(Dataset):
    line = "*"*69
    print(line)

    df = pd.DataFrame(Dataset) 
    
    plt.figure(figsize=(10,6))
    sns.boxplot(x = 'English', Dataset = df)
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