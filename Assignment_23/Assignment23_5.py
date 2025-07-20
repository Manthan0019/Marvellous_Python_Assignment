import pandas as pd

def Replacename():
    data = {
        'Name':['Amit','Sagar','Pooja'],
        'Math':[85,90,78],
        'Science':[92,88,80],
        'English':[75,85,82]
    }
    
    # creating DataFrame
    df = pd.DataFrame(data)

    df['Name'] = df['Name'].replace('Pooja','Puja') 

    print("Updated Dataframe : ")
    print(df)

def main():
    Replacename()

if __name__ == "__main__":
    main()