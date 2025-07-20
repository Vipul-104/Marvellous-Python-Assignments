import pandas as pd
import matplotlib.pyplot as plt

def MarvellousDataset(Dataset):

    df = pd.DataFrame(Dataset)
    df['Total'] = df['Math'] + df['Science'] + df['English'] 
    
    Amit_Subjects = df.columns.tolist()
    Amit_Subjects.remove('Total')
    Amit_Subjects.remove('Name')
    print(Amit_Subjects)

    # amit's marks
    Amit_marks = []
    for i in Amit_Subjects:
        # Amit_marks.append(df.at[0, i])
        value = df.at[0, i]
        Amit_marks.append(value)        
    
    # line chart
    plt.plot(Amit_Subjects, Amit_marks, marker = 'o', color='skyblue')
    plt.xlabel("Amit's Subjects")
    plt.ylabel("Amit's Marks")
    plt.title("Amit's Result")
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



#     import pandas as pd
# import matplotlib.pyplot as plt
# import numpy as np

# def main():
#     data = {'Name' : ['Amit', 'Sagar', 'Pooja'], 'Math' : [85,90,75], 'Science' : [92,88,80], 'English' : [75,80,82]}

#     df = pd.DataFrame(data)     # dataframe 'df' create

#     df['Total'] = df['Math'] + df['Science'] + df['English']
#     # print(df)

#     # amit's data
#     # amit's index = 0
#     Amit_Subjects = df.columns.tolist()
#     Amit_Subjects.remove('Total')
#     Amit_Subjects.remove('Name')
#     print(Amit_Subjects)

#     # amit's marks
#     Amit_marks = []
#     for i in Amit_Subjects:
#         # Amit_marks.append(df.at[0, i])
#         value = df.at[0, i]
#         Amit_marks.append(value)        
    
#     # line chart
#     plt.plot(Amit_Subjects, Amit_marks, marker = 'o', color='skyblue')
#     plt.xlabel("Amit's Subjects")
#     plt.ylabel("Amit's Marks")
#     plt.title("Amit's Result")
#     plt.show()

    
            

# if _name_ == "_main_":
#     main()