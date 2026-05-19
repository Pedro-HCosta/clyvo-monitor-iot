# Clyvo Pet Monitor - Dashboard IoT

Dashboard em Python com Streamlit para visualizar os dados enviados pelo ESP32.

## Dados recebidos

- Temperatura
- Umidade
- Luminosidade

## Comunicação

O dashboard escuta mensagens MQTT no tópico:

```
clyvo/pet/ambiente
```

## Como instalar
Na raiz do projeto:

```
pip install streamlit pandas paho-mqtt
```
## Como executar

Dentro da pasta iot/dashboard:
```
streamlit run app.py
```

## Broker MQTT usado
```
broker.hivemq.com
```

## Observação

O ESP32 e o dashboard precisam usar o mesmo tópico MQTT.