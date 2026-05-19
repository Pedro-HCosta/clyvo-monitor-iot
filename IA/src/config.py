CAMERA_INDEX = 0

MIN_CONTOUR_AREA = 1200

CSV_INTERVAL_SECONDS = 5

DATA_FILE_PATH = "IA/data/dados_comportamento.csv"

TRAINING_DATA_FILE_PATH = "IA/data/dataset_treino.csv"

MODEL_FILE_PATH = "IA/models/modelo_comportamento.pkl"

WINDOW_NAME = "Clyvo Pet Monitor - Vision AI"

REGIONS = {
    "agua": {
        "x": 40,
        "y": 300,
        "w": 160,
        "h": 130
    },
    "racao": {
        "x": 230,
        "y": 300,
        "w": 160,
        "h": 130
    },
    "cama": {
        "x": 420,
        "y": 180,
        "w": 180,
        "h": 160
    }
}

FEATURE_COLUMNS = [
    "tempo_parado_seg",
    "tempo_agua_seg",
    "tempo_racao_seg",
    "tempo_cama_seg",
    "visitas_agua",
    "visitas_racao",
    "visitas_cama",
    "movimentos"
]

TARGET_COLUMN = "classe"