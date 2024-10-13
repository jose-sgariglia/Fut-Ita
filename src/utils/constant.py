# ---------- Data constants ----------

# Area constants
MAPPING_REGION = {
    "Abruzzi": "Abruzzo",
    "Abruzzo": "Abruzzo",
    "Basilicata": "Basilicata",
    "Calabria": "Calabria",
    "Campania": "Campania",
    "Emilia-Romagna": "Emilia-Romagna",
    "Emilia-romagna": "Emilia-Romagna",
    "Friuli-Venezia Giulia": "Friuli-Venezia Giulia",
    "Friuli-venezia giulia": "Friuli-Venezia Giulia",
    "Friuli-venezia Giulia": "Friuli-Venezia Giulia",
    "Italia": "Italia",
    "Italy": "Italia",
    "Lazio": "Lazio",
    "Liguria": "Liguria",
    "Lombardia": "Lombardia",
    "Marche": "Marche",
    "Molise": "Molise",
    "Piemonte": "Piemonte",
    "Puglia": "Puglia",
    "Sardegna": "Sardegna",
    "Sicilia": "Sicilia",
    "Toscana": "Toscana",
    "Trentino-Alto Adige": "Trentino-Alto Adige/Südtirol",
    "Trentino-alto Adige": "Trentino-Alto Adige/Südtirol",
    "Trentino-Alto Adige/SÃ¼dtirol": "Trentino-Alto Adige/Südtirol",
    "Trentino-alto adige": "Trentino-Alto Adige/Südtirol",
    "Trentino Alto Adige / SÃ¼dtirol": "Trentino-Alto Adige/Südtirol",
    "Umbria": "Umbria",
    "Valle D'Aosta/VallÃ©e D'Aoste": "Valle D'Aosta/Vallée D'Aoste",
    "Valle d'Aosta/VallÃ©e d'Aoste": "Valle D'Aosta/Vallée D'Aoste",
    "Valle d'Aosta / VallÃ©e d'Aoste": "Valle D'Aosta/Vallée D'Aoste",
    "Valle d'aosta": "Valle D'Aosta/Vallée D'Aoste",
    "Valle D'aosta": "Valle D'Aosta/Vallée D'Aoste",
    "Veneto": "Veneto"
}

ITALIAN_REGION_CODE = {
    "Italia": "ITA",
    "Abruzzo": "ABR",
    "Basilicata": "BAS",
    "Calabria": "CAL",
    "Campania": "CAM",
    "Emilia-Romagna": "EMR",
    "Friuli-Venezia Giulia": "FVG",
    "Lazio": "LAZ",
    "Liguria": "LIG",
    "Lombardia": "LOM",
    "Marche": "MAR",
    "Molise": "MOL",
    "Piemonte": "PIE",
    "Puglia": "PUG",
    "Sardegna": "SAR",
    "Sicilia": "SIC",
    "Toscana": "TOS",
    "Trentino-Alto Adige/Südtirol": "TAA",
    "Umbria": "UMB",
    "Valle D'Aosta/Vallée D'Aoste": "VDA",
    "Veneto": "VEN"
}

ITALIAN_REGIONE_BY_CODE = {
    "ITA": "Italia",
    "ABR": "Abruzzo",
    "BAS": "Basilicata",
    "CAL": "Calabria",
    "CAM": "Campania",
    "EMR": "Emilia-Romagna",
    "FVG": "Friuli-Venezia Giulia",
    "LAZ": "Lazio",
    "LIG": "Liguria",
    "LOM": "Lombardia",
    "MAR": "Marche",
    "MOL": "Molise",
    "PIE": "Piemonte",
    "PUG": "Puglia",
    "SAR": "Sardegna",
    "SIC": "Sicilia",
    "TOS": "Toscana",
    "TAA": "Trentino-Alto Adige/Südtirol",
    "UMB": "Umbria",
    "VDA": "Valle D'Aosta/Vallée D'Aoste",
    "VEN": "Veneto"
}

# Age group constants

AGE_GROUP = {
    "categories": [range(0, 5), range(5, 10), range(10, 15), range(15, 20), range(20, 25), range(25, 30), range(30, 35), range(35, 40), range(40, 45), range(45, 50), range(50, 55), range(55, 60), range(60, 65), range(65, 70), range(70, 75), range(75, 80), range(80, 85), range(85, 150)],
    "age_bins": [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 150],
    "age_labels": ["0-4", "5-9", "10-14", "15-19", "20-24", "25-29", "30-34", "35-39", "40-44", "45-49", "50-54", "55-59", "60-64", "65-69", "70-74", "75-79", "80-84", "85+"]
}

def get_age_group(age):
    for i, group in enumerate(AGE_GROUP["categories"]):
        if age in group:
            return AGE_GROUP["age_labels"][i]
    return None

# ---------- Path ----------
PROJECT_PATH =  "../products/"

# ----- Data path -----

RAW_DATA_DEMOGRAPHICS = PROJECT_PATH + "data/demographics/raw/"
RAW_DATA_ECONOMICS = PROJECT_PATH + "data/economics/raw/"
RAW_DATA_CLIMATE_CHANGE = PROJECT_PATH +  "data/climate_change/raw/"

PROCESSED_DATA_DEMOGRAPHICS = PROJECT_PATH + "data/demographics/processed/"

CLEANED_DATA_DEMOGRAPHICS = PROJECT_PATH + "data/demographics/cleaned/"
CLEANED_DATA_ECONOMICS = PROJECT_PATH + "data/economics/cleaned/"
CLEANED_DATA_CLIMATE_CHANGE = PROJECT_PATH + "data/climate_change/cleaned/"
CLEANED_DATA_COMBINED = PROJECT_PATH + "data/combined/"

# ----- Chart path -----

DEMO_CHART_PATH = PROJECT_PATH + "charts/demographics/"
DEMO_TOTAL_CHART_PATH = PROJECT_PATH + "charts/demographics/total/"
DEMO_YEAR_CHART_PATH = PROJECT_PATH + "charts/demographics/year/"
DEMO_GROWTH_CHART_PATH = PROJECT_PATH + "charts/demographics/growth/"
DEMO_MODEL_CHART_PATH = PROJECT_PATH + "charts/demographics/model/{code}/"

ECONOMICS_CHART_PATH = PROJECT_PATH + "charts/economics/"
ECONOMICS_ORIGINAL_CHART_PATH = PROJECT_PATH+  "charts/economics/original/"
ECONOMICS_PREDICTION_CHART_PATH = PROJECT_PATH + "charts/economics/prediction/"
ECONOMICS_MODEL_CHART_PATH = PROJECT_PATH + "charts/economics/model/"

CLIMATE_CHANGE_CHART_PATH = PROJECT_PATH + "charts/climate_change/"

COMBINED_CHART_PATH = PROJECT_PATH + "charts/combined/"

# ----- Model path -----
MODEL_PATH = PROJECT_PATH + "models/"

DEMO_MODEL_PATH = PROJECT_PATH + "models/demographics/"

DEMO_LR_MODEL_PATH = PROJECT_PATH + "models/demographics/{}/linear_regression/"
DEMO_PR_MODEL_PATH = PROJECT_PATH + "models/demographics/{}/polynomial_regression/"
DEMO_RF_MODEL_PATH = PROJECT_PATH + "models/demographics/{}/random_forest/"

ECO_MODEL_PATH = PROJECT_PATH + "models/economics/"

CCH_MODEL_PATH = PROJECT_PATH + "models/climate_change/"

ALL_MODEL_PATH = PROJECT_PATH + "models/combined/"