import pandas as pd
import tqdm as progressbar


class FeatureEngineering:

    def __init__(self):
        # Definire i bin per l'intervallo di età come attributo della classe

        self.age_bins = [0, 9, 19, 29, 39, 49, 59, 69, 79, 89, 99, 109]

    def apply(self, datasets: list[pd.DataFrame]) -> list[pd.DataFrame]:
        """Applica il processo di feature engineering a una lista di DataFrame."""

        for i, dataset in progressbar.tqdm(enumerate(datasets), desc="Feature Engineering"):
            # Creare e unire la tabella pivot direttamente
            pivot_df = self.__create_pivot_table(dataset)
            datasets[i] = self.__merge_pivot_table(dataset, pivot_df)



        datasets = [dataset.drop_duplicates() for dataset in datasets]
        return datasets
    
    def __

    def __create_pivot_table(self, dataset: pd.DataFrame) -> pd.DataFrame:
        """Crea una tabella pivot per trasformare i dati in base agli intervalli di età."""
        # Utilizza pd.cut direttamente durante la creazione della tabella pivot
        age_groups = pd.cut(dataset['ETA1'], bins=self.age_bins, right=False)
        
        # Crea la tabella pivot con i range di età come colonne
        pivot_df = dataset.pivot_table(index=['TIME', 'SEXISTAT1'], 
                                       columns=age_groups, 
                                       values='Value', 
                                       aggfunc='sum', 
                                       fill_value=0,
                                       observed=False)
        
        # Resetta l'indice per ottenere un DataFrame piatto
        pivot_df.reset_index(inplace=True)
        return pivot_df

    def __merge_pivot_table(self, original_dataset: pd.DataFrame, pivot_df: pd.DataFrame) -> pd.DataFrame:
        """Unisce la tabella pivot al dataset originale, mantenendo solo le colonne con i range di età."""
        # Rimuovi le colonne che non sono necessarie prima di unire
        original_dataset = original_dataset.drop(columns=['Value', 'ETA1'])
        
        # Unisci il DataFrame pivotato con il dataset originale
        merged_dataset = pd.merge(original_dataset, pivot_df, on=['TIME', 'SEXISTAT1'], how='left')
        return merged_dataset




""" 
# Esempio di utilizzo
def main():
    # Simula il caricamento di dataset (sostituisci con il tuo codice di caricamento reale)
    datasets = [pd.DataFrame({'SEXISTAT1': ['1', '2'], 'ETA1': [10, 20], 'TIME': [2000, 2001], 'Value': [100, 200]})]

    feature_engineer = FeatureEngineering()

    print("Applicazione del Feature Engineering...")
    transformed_datasets = feature_engineer.apply(datasets)

    # Unisci i dataset trasformati in un singolo DataFrame
    merged_dataset = pd.concat(transformed_datasets, ignore_index=True)

    # Visualizza il dataset trasformato
    print(merged_dataset)

if __name__ == "__main__":
    main()

"""
