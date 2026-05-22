# Clyvo Monitor IoT
Sistema de monitoramento ambiental e comportamental para pets utilizando IoT, visão computacional e inteligência artificial.

## Objetivo
O projeto foi desenvolvido como proposta para o desafio da empresa Clyvo, com o objetivo de criar uma solução tecnológica capaz de auxiliar no monitoramento contínuo do ambiente e do comportamento de pets.

A solução combina sensores IoT, visão computacional e análise comportamental para gerar informações preventivas que podem apoiar tutores e clínicas veterinárias.

## Estrutura do Projeto
```
clyvo-monitor-iot/
│
├── IA/
│   ├── data/
│   ├── models/
│   ├── src/
│   └── README.md
│
├── IOT/
│   ├── esp32/
│   └── dashboard/
│
├── README.md
└── requirements.txt
```

## Módulo IoT
O módulo IoT é responsável pelo monitoramento ambiental utilizando ESP32 e sensores físicos.

- ESP32
- DHT22
- LDR
- MQTT
- Dashboard em Streamlit

O sistema coleta:
- temperatura;
- umidade;
- luminosidade;

e transmite os dados em tempo real para o dashboard utilizando MQTT.

## Módulo IA
O módulo de IA realiza análise comportamental utilizando webcam, OpenCV e Scikit-learn.

- Detecção de movimento
- Rastreamento por regiões
- Contagem de visitas
- Tempo parado
- Geração de dataset
- Classificação comportamental

A IA utiliza métricas extraídas da webcam para classificar padrões básicos de comportamento do pet.

## Classes comportamentais
- normal
- baixa_atividade
- agitacao

## Tecnologias utilizadas
- Python
- OpenCV
- Scikit-learn
- Streamlit
- MQTT
- ESP32
- DHT11
- LDR
- Pandas

# Como executar
## 1. Criar ambiente virtual
```
python -m venv venv
```
## 2. Ativar ambiente virtual
```
venv\Scripts\activate
```

## 3. Instalar dependências
```
pip install -r requirements.txt
```

## Executando o módulo IA
```
cd IA/src
python main.py
```

## Treinando o modelo de IA
```
cd IA/src
python ia_model.py
```

## Executando o dashboard IoT
```
cd IOT/dashboard
streamlit run app.py
```

## Estrutura de funcionamento
```
ESP32 + Sensores
        ↓
      MQTT
        ↓
 Dashboard IoT
        ↓
 Dados ambientais
```
```
Webcam
   ↓
 OpenCV
   ↓
 Métricas comportamentais
   ↓
 Scikit-learn
   ↓
 Classificação de comportamento
```

## Objetivos futuros
- Integração total entre IoT e IA
- Histórico longitudinal
- Banco de dados
- Dashboard avançado
- Alertas automáticos
- Automação do ambiente
- Melhorias no modelo de IA

## Repositório
https://github.com/Pedro-HCosta/clyvo-monitor-iot.git