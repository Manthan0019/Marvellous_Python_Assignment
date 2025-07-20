import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder

def marksAccordingToGender():
    data = {
        'Name':['Amit','Sagar','Pooja'],
        'Math':[85,90,78],
        'Science':[92,88,80],
        'English':[75,85,82]
    }
    
    # creating DataFrame
    df = pd.DataFrame(data)

    df['Gender'] = ['Male','Male','Female']

    avg_marks = df.groupby('Gender')[['Math','Science','English']].mean()

    print("Average marks by gender : ")
    print(avg_marks)

def main():
    marksAccordingToGender()

if __name__ == "__main__":
    main()