# vedere qui: https://realpython.com/pandas-read-write-files/
# vedere qui: https://towardsdatascience.com/tips-and-tricks-to-work-with-text-files-in-python-89f14a755315
# vedere qui: http://songhuiming.github.io/pages/2017/04/02/jupyter-and-pandas-display/

import csv

import pandas as pd
  
## gapminder_csv_url ='http://bit.ly/2cLzoxH'
nome_file='data.csv'
testo="qualche riga di testo"
# load the data with pd.read_csv
risultato = pd.read_csv((nome_file), usecols=['AUDITOR'],nrows=4)
# risultato.map('I am a {}'.format)

risultato1=risultato.add_prefix('item_')


print(risultato1)