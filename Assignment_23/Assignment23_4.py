import pandas as pd

def ScienceHeighScore():
    data = {
        'Name':['Amit','Sagar','Pooja'],
        'Math':[85,90,78],
        'Science':[92,88,80],
        'English':[75,85,82]
    }
    
    # creating DataFrame
    df = pd.DataFrame(data)

    high_score = df[df['Science'] > 85] 

    print("Students who scored more than 85 in science : ")
    print(high_score)

def main():
    ScienceHeighScore()

if __name__ == "__main__":
    main()