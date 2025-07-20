import pandas as pd

def DescribeDataFrame():
    data = {
        'Name':['Amit','Sagar','Pooja'],
        'Math':[85,90,78],
        'Science':[92,88,80],
        'English':[75,85,82]
    }
    
    # creating DataFrame
    df = pd.DataFrame(data)

    print(df.describe())

def main():
    DescribeDataFrame()

if __name__ == "__main__":
    main()