import pandas as pd

airbnb = pd.read_csv(r"C:\Users\student\Downloads\archive\Airbnb_Open_Data.csv")

# print(airbnb.head())
#print(airbnb.columns)
# print(airbnb.info())
# print(airbnb['license'])

columns_to_keep = ['NAME', 'host id', 'host_identity_verified', 'host name',
       'neighbourhood group', 'neighbourhood', 'lat', 'long', 'country',
       'country code', 'instant_bookable', 'cancellation_policy', 'room type',
       'Construction year', 'price', 'service fee', 'minimum nights',
       'number of reviews', 'last review', 'availability 365',]
columns_to_drop = ['id', 'reviews per month',
       'review rate number', 'calculated host listings count',
        'house_rules', 'license']

# print(len(columns_to_keep))

# df = airbnb[columns_to_keep]
# print(df.head())

airbnb.drop(columns = columns_to_drop, inplace = True)
print(airbnb.columns)
print(airbnb.shape)
airbnb.rename(columns={'NAME': 'name'}, inplace=True)
print(airbnb.columns)

for i in airbnb.columns:
    print(i.upper())

new_columns_names = []
for i in airbnb.columns:
    new_columns_names.append(i.upper())

print(f'those are the columns from airbnb but uppercase \n {new_columns_names}')

# new_dataframe = airbnb.copy()
# new_dataframe.columns = new_columns_names
# print(new_dataframe)
# print(new_dataframe.columns)


# the duplicated raws
print(airbnb.duplicated().sum())
# shows if the first 5 are duplicates or not
print(airbnb.duplicated().head())

airbnb.drop_duplicates(inplace=True)
print(airbnb.duplicated().sum())

print(f'number of null values: {airbnb.isna().sum()}')


airbnb.dropna(inplace=True)
print(f'number: {airbnb.isna().sum()}')

airbnb["host_identity_verified"] = airbnb["host_identity_verified"].str.upper()
print(airbnb["host_identity_verified"])


airbnb["instant_bookable"] = airbnb["instant_bookable"].apply(lambda x: 1 if x ==True else 0)
print(airbnb["instant_bookable"])

print(airbnb.head(10))
#to not keep the old index we use drop=True
airbnb.reset_index(drop=True, inplace=True)
print(airbnb.head(10))

# check the type of data it is string we want int
# print(type(airbnb['price'][15]))
# print(airbnb['price'][15])

airbnb['price'] = airbnb['price'].str.replace("$", "")
#print(airbnb['price'][15])

# The price column contains strings with commas and spaces Python cannot directly convert '1,060 ' to an integer
airbnb['price'] = airbnb['price'].str.replace(',', '').str.strip().astype(int)
print(type(airbnb['price'][15]))

airbnb['price_per_night'] = airbnb['price'] / airbnb['minimum nights']
airbnb['has_reviews'] = (airbnb['number of reviews'] > 0).astype(int)

print(airbnb.columns)

print(airbnb.groupby('neighbourhood group')['price'].mean().sort_values(ascending=False))

print(airbnb.groupby('room type').agg(
    avg_price=('price', 'mean'),
    count=('price', 'count')
))

print(airbnb[airbnb["availability 365"] < 30])



