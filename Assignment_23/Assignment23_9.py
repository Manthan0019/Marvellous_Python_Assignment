import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def FillNull():
    data2 = {
        'Name':['Amit','Sagar','Pooja'],
        'Math':[np.nan,90,78],
        'Science':[92,np.nan,80]
    }
    
    # creating DataFrame
    df = pd.DataFrame(data2)

    mean = df[['Math','Science']].mean()

    df.fillna(mean, inplace= True)

    print("Updated dataframe")
    print(df)
    
def main():
    FillNull()

if __name__ == "__main__":
    main()