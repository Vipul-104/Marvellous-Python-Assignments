import pandas as pd
from sklearn.model_selection import train_test_split


def main():
   data = {'Age':[22,25,47,52,46,56], 'Purchesed' : [0,1,1,0,1,0]}
   df = pd.DataFrame(data)

   x = df[['Age']]
   y = df[['Purchesed']]

   x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=42)
   print("DIMENSIONS of training Dataset ARE:",x_train.shape)
   print("DIMENSIONS of testin Dataset ARE:",x_test.shape)
   

if __name__ == "__main__":
    main()