import os
import pandas as pd
import tqdm as progessbar

# !TODO: Merge dataset per creare due dataset:
#   1. chiave l'anno, quindi creare feature come "male_value", "female_value", "total_value"
#   2. chiave territorio, quindi creare feature come "state"

# !!TODO: Capire come funziona il modello di regressione polinomiale e implementarlo
# !!TODO: Capire il modello multi-output e implementarlo

PATH_DATASET = "dataset/"

def load_datasets() -> list[pd.DataFrame]:
    datasets = []

    for filename in progessbar.tqdm(os.listdir(PATH_DATASET)):
        if filename.endswith(".csv"):
            file_path = os.path.join(PATH_DATASET, filename)
            df = pd.read_csv(file_path)
            datasets.append(df)
    
    return datasets

def clean_datasets(datasets: list[pd.DataFrame]):
    # PULISCO I DATASET DA COLONNE INUTILI

    COLUMNS_TO_REMOVE = [
        "ITTER107", 
        "TIPO_DATO15", 
        "Tipo di indicatore demografico", 
        "Età", 
        "Sesso",
        "Seleziona periodo",
        "Flag Codes",
        "Flags"
    ]

    for dataset in datasets:
        dataset.drop(columns=COLUMNS_TO_REMOVE, inplace=True)
    return datasets

def merge_datasets(datasets: list[pd.DataFrame]) -> pd.DataFrame:
    merge_datasets = pd.concat(datasets, ignore_index=True)
    return merge_datasets

def save_dataset(dataset: pd.DataFrame, filename: str = "merged_dataset.csv"):
    dataset.to_csv(filename, index=False)

def main():
    print("Creating Dataset...")

    print("Loading Datasets...")
    datasets = load_datasets()

    print("Cleaning Datasets...")
    clean_datasets(datasets)

    print("Merging Datasets...")
    merged_dataset = merge_datasets(datasets)

    print("Saving Merged Dataset...")
    save_dataset(merged_dataset)


if __name__ == "__main__":
    main()