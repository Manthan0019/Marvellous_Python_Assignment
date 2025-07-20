import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def SagarPieplot():
    data = {
        'Name':['Amit','Sagar','Pooja'],
        'Math':[85,90,78],
        'Science':[92,88,80],
        'English':[75,85,82]
    }
    
    # creating DataFrame
    df = pd.DataFrame(data)

    x = ['Math','Science','English']
    y = df[df['Name']== 'Sagar'][x].values.flatten()

    plt.figure(figsize=(8,5))
    plt.pie(y,labels=x,autopct='%1.1f%%',startangle=140)
    plt.title("Sagar score")
    plt.axis('equal')
    plt.show()

def main():
    SagarPieplot()

if __name__ == "__main__":
    main()