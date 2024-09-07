import os
import pandas as pd
import tqdm as progressbar
from .constant import ITA_STATE

class DatasetCleaner:
    def __init__(self, columns_to_keep : list[str] = None):
        # Inizializza la classe con le colonne da mantenere

        self.columns_to_keep = columns_to_keep or ["Territorio", "SEXISTAT1", "ETA1", "TIME", "Value"]

    def _remove_records_with_value(self, df: pd.DataFrame, column_name: str, value) -> pd.DataFrame:
        """Rimuove i record dal DataFrame dove la colonna specificata ha un valore dato."""

        return df.loc[df[column_name] != value]

    def clean(self, datasets: list[pd.DataFrame]) -> list[pd.DataFrame]:
        """Applica il processo di pulizia a una lista di DataFrame."""

        for i, dataset in progressbar.tqdm(enumerate(datasets), desc="Pulizia dei Dataset"):
            # Mantieni solo le colonne necessarie
            dataset.drop(columns=[col for col in dataset.columns if col not in self.columns_to_keep], inplace=True)

            # Rimuovere i record con valori indesiderati
            dataset = dataset[dataset['SEXISTAT1'] != 9]
            dataset = dataset[dataset['ETA1'] != 'TOTAL']
            dataset = dataset[dataset['Territorio'].isin(ITA_STATE)]

            # Rimuovi stringhe specifiche e converti in numerici
            dataset['ETA1'] = dataset['ETA1'].replace({'Y_GE100': '100'}).str.replace('Y', '')
            dataset['ETA1'] = pd.to_numeric(dataset['ETA1'], errors='coerce')  # Converti in numerico e gestisci errori

            # Rimuovi i record con valori mancanti dopo la conversione
            dataset.dropna(subset=['ETA1'], inplace=True)

            # Verifica che i dati siano del tipo corretto
            self.__verify_column_type(dataset, 'ETA1', int)

            datasets[i] = dataset
            
        return datasets


    def __verify_column_type(self, dataset: pd.DataFrame, column_name: str, expected_type):
        """Verifica se una colonna contiene solo valori di un tipo specificato."""

        if not all(isinstance(x, expected_type) for x in dataset[column_name].dropna()):
            raise ValueError(f"La colonna {column_name} contiene ancora tipi non {expected_type.__name__}")


    def save(self, dataset: pd.DataFrame, filename: str):
        """Salva il DataFrame pulito in un file CSV."""

        if not os.path.exists(filename):
            os.makedirs(os.path.dirname(filename), exist_ok=True)

        dataset.to_csv(filename, index=False)
        print(f"Dataset salvato come {filename}")



""" 
# Esempio di utilizzo
def main():
    # Simula il caricamento di dataset (sostituisci con il tuo codice di caricamento reale)
    datasets = [pd.DataFrame({'SEXISTAT1': ['1', '9', '1'], 'ETA1': ['Y_GE100', 'TOTAL', 'Y10'], 'Value': [100, 200, 300]})]

    cleaner = DatasetCleaner()

    print("Pulizia dei Dataset...")
    cleaned_datasets = cleaner.clean(datasets)

    # Unisci i dataset puliti in un singolo DataFrame
    merged_dataset = pd.concat(cleaned_datasets, ignore_index=True)

    # Salva il dataset pulito
    cleaner.save(merged_dataset, "cleaned_dataset.csv")

if __name__ == "__main__":
    main()
 """