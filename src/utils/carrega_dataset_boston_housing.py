import pandas as pd

CAMINHO_CSV = './datasets/boston_housing.csv'

def carrega_dataset_boston_housing():
    dataset = pd.read_csv(CAMINHO_CSV)
    dataset = dataset.convert_dtypes()
    return dataset