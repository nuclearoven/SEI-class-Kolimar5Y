import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
#reads the csv file and creates dataframes Company and year based on the Company and Date collum from the dataset
df = pd.read_csv("space_missions.csv")
Company = df["Company"]
df['Year'] = pd.DatetimeIndex(df['Date']).year
year = df["Year"]


#Creates a new dictionary with companies corresponding to countries
company_country = {
    'US Navy': 'USA',
    'NASA': 'USA',
    'AMBA': 'USA',
    'General Dynamics': 'USA',
    'US Air Force': 'USA',
    "Martin Marietta":"USA",
    'Lockheed': 'USA',
    'Northrop': 'USA',
    'Boeing': 'USA',
    'RVSN USSR': 'Russia',
    'Roscosmos': 'Russia',
    "Yuzhmash":"Russia",
    'OKB-586': 'Russia',
    "Kosmotras": "Russia",
    "VKS RF": "Russia",
    "GK LS": "Russia",
    'CASC': 'China',
    "CASIC": "China",
    "CAS Space": "China",
    "ESA":"EU",
    "CECLES":"EU",
    "RAE":"EU",#UK
    "Armée de l'Air": "EU",#FR
    'CNES': 'EU',#FR
    "ASI": "EU",
    "UT": "JapanKorea",
    'JAXA':'JapanKorea',
    "ISAS":"JapanKorea",
    "KARI":"JapanKorea",
    "IAI":"Iran",
    "IRGC":"Iran",
    "ISRO":"India",
}
#Creates a new collum "County" and maps it based of the Company collum using the company_country dictionary
df['Country'] = Company.map(company_country).fillna('Private')
def Timeline(df):
    """Creates two dataframes for the US and Russian launches and adds entries to them
    based on if their entry in the country collum in the base dataframe equals: "USA" or "Russia".
    -plots both on separate step histograms based on the "Year" collum
    -plots the total amount of launches on a histogram based on the "Year" collum
    -Creates a legend and labels axes"""
    plt.title('Launches per year')
    plt.hist(df["Year"], bins=65,color="0.5",alpha=0.5, label='All')
    plt.legend(loc='upper left')
    plt.xlabel("Year")
    plt.ylabel("Number of launches")
    plt.tight_layout()
    plt.show()
def TimelineCountries(df):
    """Creates 5 dataframes for the launches of China, EU(Combination of ESA france and UK for clarity),
    Japan/South Korea, India and Iran and adds entries to them based on if the country collum in the base dataframe equals their name.
    -plots all on the same stacked histograms based on the "Year" collum
    -plots the total amount of launches on a histogram based on the "Year" collum
    -Creates a legend and labels axes"""
    plt.title('Launches per year by other countries')
    CNLaunches = df[df["Country"] == "China"]
    EULaunches = df[df["Country"] == "EU"]
    JKLaunches = df[df["Country"] == "JapanKorea"]
    INLaunches = df[df["Country"] == "India"]
    IRLaunches = df[df["Country"] == "Iran"]
    plt.hist([CNLaunches["Year"],EULaunches["Year"],JKLaunches["Year"],INLaunches["Year"],IRLaunches["Year"]], bins=57,alpha=0.5,histtype='barstacked',color=["r","b","c","tab:orange","g"], label=['China',"EU","Japan/Korea","India","Iran"])
    plt.hist(df["Year"], bins=65, color="0.5", alpha=0.2, label='All')
    plt.legend(loc='upper left')
    plt.xlabel("Year")
    plt.ylabel("Number of launches")
    plt.tight_layout()
    plt.show()
def Companies(df):
    """Creates a new dataframe "Owner" and labels each entry as Private or Government based on if the country collum in the base dataframe equals
     private or one of the above mentioned countries.
    -Creates three dataframes called private, SpaceX and Government
    -Assigns entries to "Private" if their entry in the "Owner" dataframe equals private and their entry in the "Company" collum in the base dataframe doesnt equal "SpaceX"
    -Assigns entries to "SpaceX" if their entry in the "Company" collum in the base dataframe equals "SpaceX"
    -Assigns entries to "Private" if their entry in the "Owner" dataframe equals "Government".
    -plots all on the same stacked histograms based on the "Year" collum
    -Creates a legend and labels axes"""
    plt.title('Private vs. Government agencies')
    Owner = df['Country'].apply(lambda x: 'Private' if x == "Private" else 'Government')
    Private = df[(Owner == 'Private') & (df['Company'] != "SpaceX")]
    SpaceX = df[df["Company"] == "SpaceX"]
    Government = df[Owner == "Government"]
    plt.hist([Government["Year"],Private["Year"],SpaceX["Year"]], bins=65,color=["0.5","r","k"],alpha=0.5,stacked=True, label=["State owned","Private","Space X"])
    plt.legend(loc='upper left')
    plt.xlabel("Year")
    plt.ylabel("Number of launches")
    plt.tight_layout()
    plt.show()
def Rockets(df,Count):
    """-Creates a new dataframe "Rockets", it counts how many instances of the rocket type
    there are in the dataframe and only adds the highest numbers based on the "Count" variable
    -Creates a new dataframe df_filtered and adds rows if their entry in the "Rocket" collum is in the "Rockets" dataframe.
    -plots the df_filtered dataframe on a histogram
    -Creates a legend and labels axes
    """
    plt.title('Most common rocket types')
    Rockets = df['Rocket'].value_counts().head(Count).index
    df_filtered = df[df['Rocket'].isin(Rockets)]
    df_filtered.sort_values(by=['Rocket'], ascending=True, inplace=True)
    plt.hist(df_filtered["Rocket"], bins=np.arange(Count)-0.5,color="r",rwidth=0.8,alpha=0.5,)
    plt.xlabel("Rocket type")
    plt.ylabel("Number of launches")
    plt.show()
def Price(df):
    """Creates a new dataframe "Filter" and removes entries that are null
    -Creates a new dataframe sum which groups and sums all entries in a given year
    -Creates a new dataframe Average which groups and averages all entries in a given year
    -plots the df_filtered dataframe on a histogram
    -Creates a legend and labels axes
    """
    plt.title('Correlation between year and spending')
    Filter = df[df['Price'].astype(float).notnull()]
    Sum = Filter.groupby('Year')["Price"].sum()
    Average = Filter.groupby('Year')["Price"].mean()
    plt.plot(Average,color='b',label="Average")
    plt.plot(Sum,color='r',label="Sum")
    plt.legend(loc='upper left')
    plt.xlabel("Year")
    plt.ylabel("Spending(Millions of USD)")
    plt.show()

Timeline(df)
TimelineCountries(df)
Companies(df)
Rockets(df,10)
Price(df)