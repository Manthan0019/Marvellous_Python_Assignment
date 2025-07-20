import pandas as pd
import numpy as np

def MathNormalized():
    data = {
        'Name':['Amit','Sagar','Pooja'],
        'Math':[85,90,78],
        'Science':[92,88,80],
        'English':[75,85,82]
    }
    
    # creating DataFrame
    df = pd.DataFrame(data)

    df['math_normalized'] = (df['Math'] - df['Math'].min()) / (df['Math'].max() - df['Math'].min()) # normalization using max ,min

    print(df)

def main():
    MathNormalized()

if __name__ == "__main__":
    main()