from operator import index

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df_maraton = pd.read_csv('filtrovanie_maraton.csv')
#prints the number of rows in the dataframe

def nedobehli(df):
    """Returns the number of rows with --- in the Čistý čas collum"""
    nedobehli = df[df["Čistý čas"] == "---"]
    return len(nedobehli)

def countKEN(df):
    """Returns the number of rows with KEN in the Nár. collum"""
    Kena = df[df["Nár."] == "KEN"]
    return len(Kena)

def countCZ(df):
    """Returns the number of rows with CZE in the Nár. collum"""
    CZ = df[df["Nár."] == "CZE"]
    return len(CZ)

def Kategorie(df):
    """Returns the number of unique elements in the Kategorie collum"""
    return np.unique(df["Kategórie"])

def M73(df, idx):
    """creates a dataframe m which only includes rows with M hlavná kategória in the Kategórie collum
    Returns the row with index idx in m"""
    m = df[df["Kategórie"] == "M hlavná kategória"]
    return m.iloc[idx]["Meno"]+" "+ m.iloc[idx]["Priezvisko"]

def Z73(df, idx):
    """creates a dataframe z which only includes rows with Z hlavná kategória in the Kategórie collum
    Returns the row with index idx in z"""
    z = df[df["Kategórie"] == "Ž hlavná kategória"]
    return z.iloc[idx]["Meno"]+" "+ z.iloc[idx]["Priezvisko"]

def Zmaxvek(df):
    """creates a dataframe z which only includes rows with Z 40-49 rokov in the Kategórie collum
    Returns the row with lowest element in the Roč. collum in z"""
    z = df[df["Kategórie"] == "Z 40-49 rokov"]
    return z[z["Roč."]==z["Roč."].min()]["Meno"]

def M1950(df):
    """creates a dataframe klub which only includes rows that dont have --- in the Klub collum
    Returns the entry in the "Meno" and "Priezvisko" collum in the row where Roč. = 1950"""
    Klub = df[df["Klub"] != "---"]
    return Klub[Klub["Roč."] == 1950]["Meno"]+" "+ Klub[Klub["Roč."] == 1950]["Priezvisko"]

def Roc1966(df):
    """Returns the number of rows with 1966 in the Roč. collum"""
    return len(df[df["Roč."] == 1966])

def MCZitnýOstrov(df):
    """returns the index of the entry with Marathon Club Žitný Ostrov in the Klub collum"""
    return df[df["Klub"] == "Marathon Club Žitný Ostrov"].index.values

def grafy(df):
    """Creates integers SK,CZ,HU,PL,AS and assigns the number of entries in their respective categories in collum Nár.
    Creates integer O and assigns the length of their categories in collum Nár. that arent SK,CZ,HU,PL,AS
    Creates a pie chart displaying SK,CZ,HU,PL,AS,O
    Counts the number of unique values in the Nár. collum and assigns the 10 most frequent to the dataframe Rockets
    Creates a new dataframe df_filtered that only includes elements that include elements from Rockets in the Nár. collum
    Creates a histogram from df_filtered
    """
    SK = len(df[df["Nár."] == "SVK"])
    CZ = len(df[df["Nár."] == "CZE"])
    HU = len(df[df["Nár."] == "HUN"])
    PL = len(df[df["Nár."] == "POL"])
    AS = len(df[df["Nár."] == "AUT"])
    O = len(df[(df["Nár."] != "SVK")& (df["Nár."] != "CZE")& (df["Nár."] != "POL")& (df["Nár."] != "HUN")& (df["Nár."] != "AUT")])
    pie = np.array([SK, CZ, HU, PL,AS, O])
    plt.pie(pie, labels=["SK", "CZ", "PL", "HU","AU", "O"])
    plt.show()
    Rockets = df['Nár.'].value_counts().head(10).index
    df_filtered = df[df['Nár.'].isin(Rockets)]
    plt.hist(df_filtered["Nár."], bins=np.arange(10) - 0.5, color="r", rwidth=0.8, alpha=0.5, )
    plt.show()
def boxViolin(df):
    """Creates a dataframe time that only includes elements that dont have --- in the Čistý čas collum
    creates a dataframe čas that converts the time dataframe into the pandas time format
    creates a boxplot with: y=čas,x= Kategórie collum
    creates a violinplot with: y=čas,x= Kategórie collum"""
    time = df[df["Čistý čas"] != "---"]
    čas=pd.to_timedelta(time["Čistý čas"])
    sns.boxplot(data=df,y=čas,x=df["Kategórie"])
    plt.show()
    sns.violinplot(data=df,x="Kategórie",y=čas)
    plt.show()
    plt.show()



boxViolin(df_maraton)
grafy(df_maraton)
print(nedobehli(df_maraton))
print(countKEN(df_maraton))
print(countCZ(df_maraton))
print(Kategorie(df_maraton))
print(M73(df_maraton, 73))
print(Z73(df_maraton,25))
print(Zmaxvek(df_maraton))
print(M1950(df_maraton))
print(Roc1966(df_maraton))
print(MCZitnýOstrov(df_maraton))