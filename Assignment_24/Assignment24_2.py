import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder

def EncodedGender():
    data = {
        'Name':['Amit','Sagar','Pooja'],
        'Math':[85,90,78],
        'Science':[92,88,80],
        'English':[75,85,82]
    }
    
    # creating DataFrame
    df = pd.DataFrame(data)

    df['Gender'] = ['Male','Male','Female']

    print("After adding gender column")
    print(df)

    
    encoder = OneHotEncoder(drop='if_binary', dtype=int,sparse_output=False)
    encoded = encoder.fit_transform(df[['Gender']])

    df['Genderencoded'] = encoded

    print("After encoding")
    print(df)

def main():
    EncodedGender()

if __name__ == "__main__":
    main()