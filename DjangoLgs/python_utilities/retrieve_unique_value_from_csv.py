# import pandas as pd
import pandas as pd
  
## gapminder_csv_url ='http://bit.ly/2cLzoxH'
nome_file='data.csv'
# load the data with pd.read_csv
record = pd.read_csv(nome_file)
  
print(record['AUDITOR'].unique())