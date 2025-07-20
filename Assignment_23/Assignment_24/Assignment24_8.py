import pandas as pd
import matplotlib.pyplot as plt


def MarvellousDataset(Dataset):
    line = "*"*69
    print(line)

    df = pd.DataFrame(Dataset) 
    
    plt.figure(figsize=(10,6))
    plt.hist(df['Math'], bins = 10, color='skyblue', edgecolor = 'black')
    plt.xlabel('Math Marks')
    plt.ylabel('Frequency')
    plt.title("Mathematics Marks")
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