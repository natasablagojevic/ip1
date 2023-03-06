import pandas as pd
import seaborn as sns

titanic = sns.load_dataset("titanic") #dataframe
# print(titanic)

print(titanic.shape())
print(titanic.info())
print(titanic.head())

# da li u skupu postoje NULL
print(titanic.isna().any().any())   # postoje nedostajuce vrednosti u skupu

print(titanic.isna().count())       # ne
print(titanic.isna().sum())         # konverzija bool u int i one se sumiraju



#   1. izbaciti sve nedostajuce
titanic1 = titanic.dropna()

print(len(titanic))
print(len(titanic1))
print(len(titanic1)/len(titanic)*1000)

# mozemo potencijalno da izbacimo kolone sa nedostajucim vrednostima
# ali time potencijalno gubimo znacajne informacije koje ce nam mozda trebati

# zamena NULL vrednosti sa nekim:
#   I nacin :   default values

titanic2 = titanic['age'].fillna(0)    # dobar kada imamo jako malo nedostajucih vrednosti
titanic2.hist()

titanic['deck'].unique()    # treba paziti

print(titanic['deck'].hist())

#   II nacin : popunjavanjem prosecnom vrednoscu

mean_age = int(titanic['age'].mean)
titanic3 = titanic['age'].fillna(mean_age)
titanic3.hist()

#   III nacin : NULL vrednosti se popunjavanju na osnovu prethodnih vrednosti
#               tako da nema bojaznosti od greske
#               - racunamo cov
#               - sortiramo pa koristimo ffill ili bfill

titanic4 = titanic['age'].ffill()
titanic4.hist()
titanic.hist()

# trazimo zavisnost medju kolonama, a ne po vrstama
# cov(X, Y) = E(XY) - E(X)E(Y)

# kalasa je u najvecoj koleraciji sa godinama
sns.heatmap(titanic.cvor())

#   IV nacin : srednaj vrednost ne svih nego svih onih kod kojih nema NULL vrednosti
