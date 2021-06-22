import pandas as pd
df = pd.read_excel(r'C:\Users\DELL\OneDrive\Documents\Job\Trusting Social\To_send_to_candidates\messy.xlsx')
# Clean the names of columns to lowercase separated by “_”, remove any empty column if necessary
df.columns = df.columns.str.lower()
df.columns = df.columns.str.strip().str.replace(' ', '_').str.replace('%','')
df = df.dropna(how='all', axis=1)
#Change the date column to the same format ‘YYYY-MM-DD’.
df['join_date'] = pd.to_datetime(df['join_date'], errors='coerce')
df['join_date'] = df['join_date'].dt.strftime('%Y/%m/%d')
# Change the name column to the title case
df.fll_nam=df.fll_nam.str.title()
# Make a new “email” column with form: {last_name}.{first_name}.{id}@yourcompany.com
df['cust_id'] = df['cust_id'].astype(str)
df[['first_name','last_name']] = df.fll_nam.str.split(expand=True)
df.loc[:,'email']=df.first_name + '.' + df.last_name + '.' + df.cust_id + '@yourcompany.com'
# Change the phone number column to the format “84……”
df['mobiles'] = df['mobiles'].astype(str)
df['mobiles'] = df['mobiles'].str.lstrip('84')
df['mobiles'] = '84' + df['mobiles']
# Find any duplicated ID and remove those who join later
df['cust_id']=df['cust_id'].drop_duplicates(keep='first', inplace=False)
df.head()
