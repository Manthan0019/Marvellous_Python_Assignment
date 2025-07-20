import pandas as pd
import matplotlib.pyplot as plt

def StudentLinePlot():
    data = {
        'Name':['Amit','Sagar','Pooja'],
        'Math':[85,90,78],
        'Science':[92,88,80],
        'English':[75,85,82]
    }
    
    # creating DataFrame
    df = pd.DataFrame(data)

    print(df)

    df = df.drop('English',axis='columns')

    print("Updated Data frame")
    print(df)

def main():
    StudentLinePlot()

if __name__ == "__main__":
    main()