import csv
import os
from datetime import datetime


class CSVLogger:
    def __init__(self, file_path):
        self.file_path = file_path
        self.headers = [
            "timestamp",
            "regiao_atual",
            "status",
            "tempo_parado_seg",
            "tempo_agua_seg",
            "tempo_racao_seg",
            "tempo_cama_seg",
            "visitas_agua",
            "visitas_racao",
            "visitas_cama",
            "movimentos"
        ]

        self.create_file_if_not_exists()

    def create_file_if_not_exists(self):
        directory = os.path.dirname(self.file_path)

        if directory:
            os.makedirs(directory, exist_ok=True)

        if not os.path.exists(self.file_path):
            with open(self.file_path, "w", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerow(self.headers)

    def save(self, data):
        row = [
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            data["regiao_atual"],
            data["status"],
            data["tempo_parado_seg"],
            data["tempo_agua_seg"],
            data["tempo_racao_seg"],
            data["tempo_cama_seg"],
            data["visitas_agua"],
            data["visitas_racao"],
            data["visitas_cama"],
            data["movimentos"]
        ]

        with open(self.file_path, "a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(row)