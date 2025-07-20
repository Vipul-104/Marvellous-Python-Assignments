import pandas as pd
import matplotlib.pyplot as plt

def MarvellousDataset(Dataset):

    df = pd.DataFrame(Dataset)
    df['Total'] = df['Math'] + df['Science'] + df['English'] 
    
    df.plot(kind ='bar', x='Name', y ='Total')
    plt.title('Marvellous Student Bar Graph')
    plt.xlabel('Student Names')
    plt.ylabel('Total Marks')
    #plt.grid()
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