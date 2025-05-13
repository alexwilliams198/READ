# Importing libraries
import pandas as pd

# Transformation Steps 


df.dropna(subset=['Books', 'Customer ID'], inplace=True)

df['Books'] = df['Books'].str.strip()

df.drop_duplicates(subset=['Books','Customer ID', 'Book checkout'], inplace=True)

df = df[df['Book checkout'].notnull() & df['Book Returned'].notnull()]

df.reset_index(drop=True, inplace=True)

df['Book checkout'] = df['Book checkout'].astype(str).str.replace('"', '').str.strip()

df['Book checkout'] = pd.to_datetime(df['Book checkout'], dayfirst=True, errors='coerce')
df['Book Returned'] = pd.to_datetime(df['Book Returned'], dayfirst=True, errors='coerce')

cutoff_date = pd.to_datetime('2024-12-31')
df = df[df['Book checkout'] <= cutoff_date]


# Exporting to CSV code

df.to_csv('cleanedlibrarydata1.csv', index=False)






