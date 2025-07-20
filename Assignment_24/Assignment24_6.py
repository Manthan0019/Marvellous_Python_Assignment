import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def CountPassed():
    data = {
        'Name':['Amit','Sagar','Pooja'],
        'Math':[85,90,78],
        'Science':[92,88,80],
        'English':[75,85,82]
    }
    
    # creating DataFrame
    df = pd.DataFrame(data)

    df['Total'] = df[['Math','Science','English']].sum(axis=1)

    df['Status'] = df['Total'].apply(lambda x: 'Pass' if x > 250 else 'Fail')

    Count = (df['Status'] == 'Pass').sum()

    print("Number of passed students",Count)

def main():
    CountPassed()

if __name__ == "__main__":
    main()