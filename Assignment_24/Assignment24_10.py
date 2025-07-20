import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def BoxPlot():
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

    plt.figure(figsize=(6, 5))
    plt.boxplot(df['English'], patch_artist=True, boxprops=dict(facecolor='lightblue'))
    plt.title('Boxplot of English Marks')
    plt.ylabel('Marks')
    plt.grid(True)
    plt.show()

def main():
    BoxPlot()

if __name__ == "__main__":
    main()