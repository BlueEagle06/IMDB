import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option('display.max_columns',20)


df=pd.read_csv(r"C:\Users\Gurmehar\Desktop\PC stuff\python course\imdb\imdb.csv",index_col=[0])
df1=df.dropna(subset=['Runtime','Metacritic Score', 'Budget', 'Gross Box Office Worldwide', 'Certificate', 'Popularity Ranking'])

df1["User Reviews"]=df1["User Reviews"].str.replace(".","")
df1["User Reviews"]=df1["User Reviews"].str.replace("K","00")
df1["User Reviews"]=(pd.to_numeric(df1["User Reviews"]))
df1["User Reviews"]=df1["User Reviews"].astype(int)
print(df.info())
#print(df1.describe())
#print(df.columns)
#print(rows_not_in_dollars)
df1["Runtime"]=df1["Runtime"].str.strip()
#print(df1["Runtime"].head(60))

def transformRuntime(runtime):

    if len(str(runtime))==5:
        return int(runtime[0])*60 + int(runtime[-2])
    elif len(str(runtime))==6:
        return int(runtime[0])*60 + int(runtime[-3:-1])
    elif len(str(runtime))==2:
        return int(runtime[0])*60
    else:
        raise ValueError('clean your dataset')


df1["Duration"]=df1["Runtime"].apply(lambda x: transformRuntime(x))
#print(df1["Duration"].head(60))
df1["Popularity Ranking"]=pd.to_numeric(df1["Popularity Ranking"].str.replace(",",""))
#print(df1["Popularity Ranking"].head(60))
#print(df1.columns)


a=(df1.loc[df1["Budget"].str.contains("$",regex=False)==False]).index
print(a)
df1.drop(a,inplace=True)
print(df1)
b=(df1.loc[df1["Gross Box Office Worldwide"].str.contains("$",regex=False)==False]).index
df1.drop(b,inplace=True)
df1["Budget"]=df1["Budget"].str.strip("$")
df1["Budget"]=df1["Budget"].str.strip("R$")
df1["Budget"]=df1["Budget"].str.replace(",","")
df1["Budget"]=df1["Budget"].str.replace(" (estimated)","",regex=False)
df1["Budget"]=pd.to_numeric(df1["Budget"].str.strip())
print(df1)
print(b)


df1.to_csv("CleanedIMDB.csv")
print(df1.info())



sns.relplot(x="Release Year",y="Budget",data=df1,kind="line")
plt.show()
sns.lmplot(x="IMDB Rating",y="Metacritic Score",data=df1)
plt.show()

ab=pd.crosstab(df1["IMDB Rating"],df1["Metacritic Score"])
sns.heatmap(ab)
plt.show()
sns.lmplot(x="IMDB Rating",y="Popularity Ranking",data=df1)
plt.show()
sns.lmplot(x="User Reviews",y="Popularity Ranking",data=df1)
plt.show()
sns.lmplot(x="User Reviews",y="Critic Reviews",data=df1)
plt.show()
sns.catplot(x="Genres",y="Popularity Ranking",data=df1,kind="bar")
plt.show()

print(df1["Genres"].unique())
