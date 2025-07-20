import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def MarkHistogram():
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

    plt.figure(figsize=(8,5))
    plt.hist(df['Math'],color='lightblue',edgecolor='black')
    plt.xlabel("Math Marks")
    plt.ylabel("Number of students")
    plt.title("Math Marks Histogram")
    plt.show()

def main():
    MarkHistogram()

if __name__ == "__main__":
    main()