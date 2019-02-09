# Importing libraries
import pandas as pd
import numpy as np

# Read csv file into a pandas dataframe

#If I had multiple sheets and wanted to read a different one https://www.dataquest.io/blog/excel-and-pandas/
#movies_sheet1 = pd.read_excel(excel_file, sheetname=0, index_col=0)
#movies_sheet1.head()

df = pd.read_csv("pizza.xlsx")
df.fillna(False, inplace=True)  #Checks empty spots and marks em as false
# z = df.iloc[[2][:]] this gives you an entire row [ [Row],[Columns] ], then list it
# Take a look at the first few rows
print(df.head())

#df['Failure Criteria'].isnull() returns true if something is empty
or just do df['Failure Criteria'] to get the entire column



#---------------------------------------------------------------
