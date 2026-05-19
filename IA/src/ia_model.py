import os
import pickle
import pandas as pd

from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

from config import TRAINING_DATA_FILE_PATH, MODEL_FILE_PATH, FEATURE_COLUMNS, TARGET_COLUMN


def train_model():
    if not os.path.exists(TRAINING_DATA_FILE_PATH):
        print("Dataset de treino não encontrado.")
        print(f"Crie o arquivo em: {TRAINING_DATA_FILE_PATH}")
        return

    dataset = pd.read_csv(TRAINING_DATA_FILE_PATH)

    missing_columns = []

    for column in FEATURE_COLUMNS + [TARGET_COLUMN]:
        if column not in dataset.columns:
            missing_columns.append(column)

    if missing_columns:
        print("Colunas ausentes no dataset:")
        for column in missing_columns:
            print(f"- {column}")
        return

    x = dataset[FEATURE_COLUMNS]
    y = dataset[TARGET_COLUMN]

    if len(dataset) < 5:
        print("Dataset muito pequeno para treino.")
        print("Adicione mais linhas ao dataset_treino.csv.")
        return

    x_train, x_test, y_train, y_test = train_test_split(
        x,
        y,
        test_size=0.25,
        random_state=42
    )

    model = DecisionTreeClassifier(random_state=42)
    model.fit(x_train, y_train)

    predictions = model.predict(x_test)

    accuracy = accuracy_score(y_test, predictions)

    print("Modelo treinado com sucesso.")
    print(f"Acurácia: {accuracy:.2f}")
    print()
    print(classification_report(y_test, predictions))

    os.makedirs(os.path.dirname(MODEL_FILE_PATH), exist_ok=True)

    with open(MODEL_FILE_PATH, "wb") as file:
        pickle.dump(model, file)

    print(f"Modelo salvo em: {MODEL_FILE_PATH}")


if __name__ == "__main__":
    train_model()