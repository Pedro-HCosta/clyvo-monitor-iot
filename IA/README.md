# Clyvo Pet Monitor - IA
Módulo responsável pela análise comportamental do pet utilizando visão computacional e inteligência artificial.

## Objetivo
O objetivo deste módulo é monitorar o comportamento do pet através de webcam, detectando movimentação, permanência em regiões específicas e padrões comportamentais.

## Tecnologias utilizadas
- Python
- OpenCV
- Scikit-learn
- Pandas
- NumPy

## Funcionalidades
- Captura de vídeo pela webcam
- Detecção de movimento
- Rastreamento de regiões
- Contagem de movimentações
- Tempo parado
- Registro de dados em CSV
- Geração de dataset
- Classificação comportamental com IA

## Regiões monitoradas
- Água
- Ração
- Cama

## Classes comportamentais
- `normal`
- `baixa_atividade`
- `agitacao`

## Estrutura do módulo
```
IA/
│
├── data/
│   ├── dados_comportamento.csv
│   └── dataset_treino.csv
│
├── models/
│   └── modelo_comportamento.pkl
│
├── src/
│   ├── main.py
│   ├── camera.py
│   ├── config.py
│   ├── detecta_mov.py
│   ├── detecta_reg.py
│   ├── metricas.py
│   ├── csv_registro.py
│   ├── ia_model.py
│   └── classifica_comportamento.py
│
└── README.md
```

## Fluxo de funcionamento
```
Webcam
   ↓
OpenCV
   ↓
Detecção de movimento
   ↓
Extração de métricas
   ↓
Registro em CSV
   ↓
Scikit-learn
   ↓
Classificação comportamental
```

## Como executar
```bash
cd IA/src
python main.py
```

## Como treinar o modelo
```bash
cd IA/src
python ia_model.py
```

## Arquivo de dados gerado
```
IA/data/dados_comportamento.csv
```

## Dataset de treino
```
IA/data/dataset_treino.csv
```

## Modelo treinado
```
IA/models/modelo_comportamento.pkl
```

## Observação
Este módulo possui finalidade acadêmica e experimental.

A classificação realizada pela IA não representa diagnóstico veterinário profissional.