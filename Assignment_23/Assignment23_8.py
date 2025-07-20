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

    df['Total'] = df[['Math','Science','English']].sum(axis=1)

    x = ['Math', 'Science', 'English']

    y = df[df['Name'] == 'Amit'][['Math', 'Science', 'English']].values[0]

    plt.figure(figsize=(8,5))
    plt.plot(x,y,color= 'blue',marker='o')
    plt.xlabel("Subjects")
    plt.ylabel("Marks")
    plt.title("Amit's Score")
    plt.grid(True)
    plt.show()

def main():
    StudentLinePlot()

if __name__ == "__main__":
    main()