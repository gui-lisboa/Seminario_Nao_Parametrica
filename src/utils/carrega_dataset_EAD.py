import pandas as pd

#https://www.kaggle.com/datasets/mdmahmudulhasansuzan/students-adaptability-level-in-online-education
CAMINHO_CSV = './datasets/students_adaptability_level_online_education.csv'

def carrega_dataset_EAD():
    dataset = pd.read_csv(CAMINHO_CSV)
    dataset = dataset.convert_dtypes()
    return dataset