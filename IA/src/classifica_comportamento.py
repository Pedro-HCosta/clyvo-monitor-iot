import os
import pickle
import pandas as pd

from config import MODEL_FILE_PATH, FEATURE_COLUMNS


class BehaviorClassifier:
    def __init__(self):
        self.model = None
        self.load_model()

    def load_model(self):
        if not os.path.exists(MODEL_FILE_PATH):
            self.model = None
            return

        with open(MODEL_FILE_PATH, "rb") as file:
            self.model = pickle.load(file)

    def is_available(self):
        return self.model is not None

    def predict(self, metrics_data):
        if self.model is None:
            return "modelo_nao_treinado"

        input_data = pd.DataFrame([{
            column: metrics_data[column]
            for column in FEATURE_COLUMNS
        }])

        prediction = self.model.predict(input_data)

        return prediction[0]