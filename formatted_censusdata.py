import pandas as pd
import censusdata
from tabulate import tabulate

tract_file = []
tracts = ["003001", "003004", "003111", "003304", "003305", "003404", "003303", "003601", "003602","003501", "003502", 
          "004000", "003901", "003902", "004700", "004800", "004900", "005000", "005100"]
tables = ['B25070_001E', 'B11016_002E']
#'GROSS RENT AS A PERCENTAGE OF HOUSEHOLD INCOME IN THE PAST 12 MONTHS'
column_names = ['GRAPI', 'HOUSEHOLD TYPE BY HOUSEHOLD SIZE']
for t in tracts:
    df = censusdata.download('acs5',2015, censusdata.censusgeo([('state', '06'), ('county', '073'), ('tract',t)]), tables)
    tract_file.append(df)
df = pd.concat(tract_file)
df.columns = column_names
print(df)
