import pandas as pd

def SortDecending():
    data = {
        'Name':['Amit','Sagar','Pooja'],
        'Math':[85,90,78],
        'Science':[92,88,80],
        'English':[75,85,82]
    }
    
    # creating DataFrame
    df = pd.DataFrame(data)

    df['Total'] = df[['Math','Science','English']].sum(axis=1)

    print(df.sort_values(by='Total',ascending=False))

def main():
    SortDecending()

if __name__ == "__main__":
    main()