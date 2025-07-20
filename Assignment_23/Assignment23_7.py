import pandas as pd
import matplotlib.pyplot as plt

def StudentMarksBarPlot():
    data = {
        'Name':['Amit','Sagar','Pooja'],
        'Math':[85,90,78],
        'Science':[92,88,80],
        'English':[75,85,82]
    }
    
    # creating DataFrame
    df = pd.DataFrame(data)

    df['Total'] = df[['Math','Science','English']].sum(axis=1)

    plt.figure(figsize=(8,5))
    plt.bar(x=df['Name'],height=df['Total'],color = 'blue')
    plt.xlabel("Student Names")
    plt.ylabel("Total marks")
    plt.title("Students Total Marks Bar Plot")
    plt.show()

def main():
    StudentMarksBarPlot()

if __name__ == "__main__":
    main()