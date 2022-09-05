import pandas as pd
import numpy as np

# import data file
data = pd.read_csv('ParameterData_plate2.txt', sep='\t')

# add 'Strain' column
wells_list = sorted(pd.unique(data['Well ']))
strains_list = list(pd.read_csv('Strains names.csv')['gene'])
data['Strain'] = data['Well '].replace(wells_list, strains_list)

# remove objects out of gate ('R01')
data = data[data['R01'] == 1].reset_index(drop=True)

# sample 500 cells from each strain
sampled_data_dict = {}
unique_strains = pd.unique(strains_list)
for s in unique_strains:
    strain_data = data[data['Strain'] == s]
    sampled_data_dict[s] = strain_data.sample(n=500, replace=True)
# Append sampled data to one dataframe:
sampled_data = sampled_data_dict[unique_strains[0]]
for s1 in unique_strains[1:]:
    sampled_data = sampled_data.append(sampled_data_dict[s1], ignore_index=True)
# save sampled data to csv file
sampled_data.to_csv('Sampled data - plate2.csv', index=False)

# get mean to each strain
# import sampled data
sampled_data = pd.read_csv('Sampled data - plate2.csv')
# creat and fill new dataframe
plot_labels_data = pd.DataFrame()
plot_labels_data['Strain'] = pd.unique(sampled_data['Strain'])
plot_labels_data['Mean Intensity'] = np.nan
for s2 in plot_labels_data['Strain']:
    plot_labels_data.loc[plot_labels_data['Strain'] == s2, 'Mean Intensity'] = sampled_data[sampled_data['Strain'] == s2]['Mean Intensity 488nm'].mean()
# save plot_lables_data to csv
plot_labels_data.to_csv('Bar labels (strain mean intensity) - plate2.csv', index=False)
