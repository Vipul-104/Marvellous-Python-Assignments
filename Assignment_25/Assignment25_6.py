import pandas as pd
from sklearn.model_selection import train_test_split


def main():
   data = {'Grade':['A+','B','A','C','B+']}
   df = pd.DataFrame(data)

   print("Dataset Bfore ReplaceMent::")
   print(df)

   print("Dataset After The replacements:")
   Grades = df['Grade'].replace({'A+':'Excellent','A':'Very Good','B+':'Good','B':'Average','C':'Poor'})
   print(Grades)
   

if __name__ == "__main__":
    main()