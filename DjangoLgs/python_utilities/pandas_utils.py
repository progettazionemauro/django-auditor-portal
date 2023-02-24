import pandas as pd
import re
import textwrap
idx=pd.RangeIndex(20,30)

# Library vedere se le seguenti fonti:https://www.digitalocean.com/community/tutorials/how-to-obtain-a-pandas-dataframe-from-an-unordered-api-endpoint
# https://pandas.pydata.org/docs/user_guide/merging.html
# come creare un report in pdf: https://dev.to/ritza/generate-pdf-reports-from-spreadsheet-data-a3o
# advanced: https://dev.to/julienkervizic/become-a-pro-at-pandas-python-s-data-manipulation-library-2161
# 

## funzione che per individuare le righe dispari

""" def even_rows(index):
    if index%2 == 0:
        return True
    return False """
 

df  = pd.read_csv('data.csv', #"https://raw.githubusercontent.com/cs109/2014_data/master/countries.csv",
                     # skiprows=lambda x: even_rows (x),
                     
                    # header=None , # forza alla prima riga
                                         
                    # usecols=['Country'],
                    # header=0,
                     
                    #names=['AUDITOR'],
                    # header=0,
                   
                   # index_col=['Country'],
                   # index_col=None,
                    # nrows=5, #read the first n row
                    usecols=[1], # usa le colonne nominate
                    # skiprows=1,
                    # verbose=True,
                    # ).head().applymap('I am from {}'.format, na_action='ignore') ## applica la formattazione
                )
## merge two columns apply(lambda x: '_'.join(x), axis=1)
## inserisce una nuova colonna: assign(nuova_colonna='Contry')
## separa ogni lettera: applymap("-".join)
## applicare una stringa: head().applymap('I am from {}'.format, na_action='ignore') # questa è la funzione corretta da applicare per generare testo a read_csv https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.applymap.html

#print(adult)
# print(f'\t{us_state.iloc[1]} works in the Mauro') # concatenate text from various indexes
# print(f'\t{us_state.loc[1]} works in the Mauro') # concatenate text from various indexes
#print(df)

print(df['AUDITOR'].unique())


df[AUDITOR].unique.to_string(buf='output.txt')         # TRASFORMA IL  DATA FRAME IN FILE DI TESTO
# print(df.shape) # dimensione della matrice
# print(df.columns)
# print(df.dtypes)

file_string_iniziale = open('output.txt', 'r+') # APRE IN READ MODE IL FILE DI TESTO
# file_string_finale=("out-finale.txt", "w")

REPLACEMENTS = [
    ("Algeria", "😤"),  
    ("Angola", "Aricchia"),
    ("Benin", "Perù"),
    ("Botswana", "Bolivia"),    
]

# data=file_string_iniziale.read()  #sostituzione di eleemnti da REPLACEMENTS

for old, new in REPLACEMENTS:               # old, new coincidodono con i due valori dell'array REPLACEMENT
    data = data.replace(old, new)
# data=data.replace('Algeria','Albano')


rgx=r'[0-9]' # rimuove i  numeri
# rgx="am"
data1=re.sub(rgx, "", data)

print(data1)



#lunghezza_df=len(data)   # calcola la lunghezza della stringa
#print(lunghezza_df)

file_string_iniziale.close ()
print ('èstato chiuso!!')

    
file_string_iniziale=open('output.txt', 'w')

file_string_iniziale.write(data1)



file_string_iniziale.close ()

file_string_iniziale=open('output.txt', 'r')

data2=df.to_string(buf='output.txt') 

rgx=r'[0-9]' # rimuove i  numeri
# rgx="am"
data3=re.sub(rgx, "", data2)

# print(data3.ljust)
# print(file_string_iniziale.read().ljust)
# print(f"{file_string_iniziale.read(): >30}") # questo tipo di formattazione è valido per file di testo



print ('èstato RI-chiuso!!')




