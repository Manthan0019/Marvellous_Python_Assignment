import pandas as pd

def ShowDataCharacteristics():
    data = {
        'Name':['Amit','Sagar','Pooja'],
        'Math':[85,90,78],
        'Science':[92,88,80],
        'English':[75,85,82]
    }
    
    # creating DataFrame
    df = pd.DataFrame(data)

    print(df.shape)   # Shape of dataframe

    print(df.columns) # colums of dataframe

    print(df.dtypes)  # data type of dataframe

def main():
    ShowDataCharacteristics()

if __name__ == "__main__":
    main()