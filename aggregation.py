#importing relevant libraries 
import pandas as pd
import glob
import os

# Importing data for all countries into one 
path = r'/path/africa_building_emissions' #appropriate path was used
filenames = glob.glob(os.path.join(path, "*.csv")) 
dfs = []
for filename in filenames:
    dfs.append(pd.read_csv(filename))
    
# Concatenating the data for the ten countries into one df
all_countries = pd.concat(dfs, ignore_index=True)

# Writing the dataframe to a csv file
all_countries.to_csv("all_countries.csv", index=False)

# Reading the csv files into two dataframes
all_countries = pd.read_csv("all_countries.csv")
population = pd.read_csv("population.csv")

# Merging the two dataframes by the "iso" column using an inner join
merged = pd.merge(all_countries, population, on="iso", how="inner")

# Writing the merged dataframe to a new csv file
merged.to_csv("buildings_data.csv", index=False)
