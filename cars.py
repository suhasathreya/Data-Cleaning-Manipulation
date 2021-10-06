import pandas as pd
cars = pd.read_csv(r'C:\Users\suhasathreya\Downloads\2. Cars Data1.csv')
cars.head()
cars.shape
print(cars.isnull().sum())

#Replace null values with mean of column
cars['Cylinders'].fillna(cars['Cylinders'].mean(), inplace = True)


#Different makes and no. of each occurance
cars['Make'].value_counts()

#Records where origin in Asia or Europe
cars[cars['Origin'].isin(['Asia','Europe'])]

#Remove all records where weight > 2000
cars[~cars['Weight']>4000]

#Increase values oof MPG_City coolumn by 3
cars['MPG_City'] = cars['MPG_City'].apply(lambda x:x+3)



