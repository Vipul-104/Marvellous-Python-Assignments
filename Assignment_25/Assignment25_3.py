import pandas as pd

def main():
    data = {'City':['Pune','Mumbai', 'Dehli','Pune','Dehli']}

    df = pd.DataFrame(data)
    df['City'] = df['City'].astype('category').cat.codes
    print(df)
   



if __name__ == "__main__":
    main()