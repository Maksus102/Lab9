import pandas as pd

cleaned_data = pd.read_csv('data/prepared/clean_data.csv', header=None)

ndf = pd.DataFrame({
   "Weapon_Quality": cleaned_data[0],
   "Maintenance_level": cleaned_data[1],
   "Fails": cleaned_data[2],
   "Crit_fails": cleaned_data[3],
   "Mag_size": cleaned_data[4],
   "Sec_level": cleaned_data[5],
   "Accuracy" : cleaned_data[6]})

with pd.HDFStore('data/prepared/cleaned_data.hdf5', mode='w') as store:
   store.put('data',ndf)

print("Данные:")
print(pd.read_hdf("data/prepared/cleaned_data.hdf5", 'data'))