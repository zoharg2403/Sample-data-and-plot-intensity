import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import ShowValues as sv

# import sampled data
sampled_data = pd.read_csv('Sampled data.csv')

Strains_list = list(pd.unique(sampled_data['Strain']))
Strains_list = [s for s in Strains_list if 'Control' not in s]

for strain in Strains_list:
    plot_data = sampled_data[(sampled_data['Strain'] == strain) | (sampled_data['Strain'] == 'BOL1-Control') |
                             (sampled_data['Strain'] == 'None') | (sampled_data['Strain'] == 'PDR3-Control') |
                             (sampled_data['Strain'] == 'SUR2-Control') | (sampled_data['Strain'] == 'MEX67-Control') |
                             (sampled_data['Strain'] == 'FAS2-Control') | (sampled_data['Strain'] == 'NVJ1-Control')]
    plt.figure(strain, figsize=[6.4 * 3.5, 4.8 * 3.5])
    p = sns.barplot(data=plot_data, y='Mean Intensity 488nm', x='Strain')
    p.set_xlabel('Strain', fontsize=20)
    p.set_ylabel('Mean Intensity 488nm', fontsize=20)
    p.set_title('Strain ' + strain + ' Mean Intensity', fontsize=20)
    plt.tick_params(axis='both', which='major', labelsize=20)
    sv.show_values_on_bars(p, space=0.6)
    plt.savefig('plate 2 - ' + strain + '.png', transparent=True, bbox_inches='tight')
    print('plate 2 - ' + strain)
