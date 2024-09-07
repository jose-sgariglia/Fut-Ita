import os
import pandas as pd
from .constant import DIR_CLEANED

class DatasetMerger:
    def __init__(self, output_dir: str = None, output_filename: str = "merged_dataset.parquet"):
        self.output_dir = output_dir or DIR_CLEANED
        self.output_filename = output_filename

    def merge_datasets(self, datasets: list[pd.DataFrame]) -> pd.DataFrame:
        """Unisce una lista di DataFrame in un unico DataFrame, gestendo i tipi di dati non supportati e ordinando per anno."""
        print("Merging datasets...")
        # Unisce i dataset
        merged_dataset = pd.concat(datasets, ignore_index=True)
        print("Datasets merged!")

        # Gestisce la conversione dei tipi di dati non supportati
        merged_dataset = self._convert_unsupported_types(merged_dataset)

        # Ordina il dataset in base all'anno
        merged_dataset = self._sort_by_year(merged_dataset)

        return merged_dataset

    def _convert_unsupported_types(self, dataset: pd.DataFrame) -> pd.DataFrame:
        """Converte i tipi di dati non supportati da Parquet in tipi supportati."""
        for col in dataset.columns:
            if pd.api.types.is_categorical_dtype(dataset[col]):
                dataset[col] = dataset[col].astype(str)
            elif pd.api.types.is_interval_dtype(dataset[col]):
                dataset[col] = dataset[col].apply(lambda x: str(x) if pd.notnull(x) else None)
            elif pd.api.types.is_object_dtype(dataset[col]):
                dataset[col] = dataset[col].astype(str)
        return dataset

    def _sort_by_year(self, dataset: pd.DataFrame) -> pd.DataFrame:
        """Ordina il DataFrame in base alla colonna TIME."""
        # Controlla se la colonna TIME1 è numerica; se no, la converte
        if not pd.api.types.is_numeric_dtype(dataset['TIME']):
            dataset['TIME1'] = pd.to_numeric(dataset['TIME'], errors='coerce')

        # Ordina per la colonna TIME
        dataset = dataset.sort_values(by='TIME', ascending=True)
        return dataset

    def save_to_parquet(self, dataset: pd.DataFrame):
        """Salva il DataFrame unito in un file Parquet."""
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)  # Crea la cartella se non esiste

        file_path = os.path.join(self.output_dir, self.output_filename)
        try:
            dataset.to_parquet(file_path, index=False)
            print(f"Dataset saved to {file_path}!")
        except Exception as e:
            print(f"Error while saving to Parquet: {e}")

    def process_and_save(self, datasets: list[pd.DataFrame]):
        """Processa i dataset e li salva in formato Parquet."""
        merged_dataset = self.merge_datasets(datasets)
        self.save_to_parquet(merged_dataset)


""" 
# Esempio di utilizzo
if __name__ == "__main__":
    # Definisci la directory di output e il nome del file
    output_dir = "output"
    output_filename = "merged_dataset.parquet"

    # Crea un'istanza della classe DatasetMerger
    merger = DatasetMerger(output_dir, output_filename)

    # Esempio di liste di DataFrame (sostituisci con i tuoi dataset)
    datasets = [
        pd.DataFrame({'TIME1': [2022, 2020], 'A': [1, 2], 'B': [3, 4]}),
        pd.DataFrame({'TIME1': [2021, 2019], 'A': [5, 6], 'B': [7, 8]})
    ]

    # Processa e salva il dataset
    merger.process_and_save(datasets)
"""
