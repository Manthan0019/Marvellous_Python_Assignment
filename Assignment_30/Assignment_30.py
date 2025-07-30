import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,confusion_matrix,roc_auc_score,classification_report

def PrepareData(Datapath):
    line = "-"*80

    df = pd.read_csv(Datapath,sep=';')

    print(line)
    print("Dtaset Loaded successfully..!")

    print("First five entries of dataset ")
    print(df.head())
    print(line)

    print("Statistical data of datadet : ")
    print(df.describe())
    print(line)

    print("Dimentions of data : ")
    print(df.shape)
    print(line)

    # encoding

    df['y'] = df['y'].map({'no': 0, 'yes': 1})

    df.drop(columns=['contact'])

    x = df.drop(columns=['y'])
    y = df['y']

    scaler = StandardScaler()
    x_scaled = scaler.fit_transform(x)

    x_train,x_test,y_train,y_test = train_test_split(x_scaled,y,test_size=0.2,random_state=42)

    BankFullLogisticRegretion(x_train,x_test,y_train,y_test)

def BankFullLogisticRegretion(x_train,x_test,y_train,y_test):
    model = LogisticRegression()

    model.fit(x_train,y_train)

    y_pred = model.predict(x_test)

    Accuracy = accuracy_score(y_test,y_pred)

    print("Accuracy is : ",Accuracy * 100,"%")
def main():
    PrepareData("bank-full.csv")
if __name__ == "__main__":
    main()