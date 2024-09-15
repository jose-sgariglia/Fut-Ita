import pandas
from utils.constant import DIR_RAW_DATA

dataset = pandas.read_csv(DIR_RAW_DATA + 'fascie_2019-2024.csv')
dataset = dataset.sort_values(by=['TIME', 'ETA1'])
dataset = dataset[dataset['Territorio'] == 'Italia']


print(dataset)