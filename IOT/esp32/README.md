# Clyvo Pet Monitor - ESP32 IoT

Este módulo coleta dados ambientais usando ESP32, DHT11 e LDR.

## Sensores

- DHT22: temperatura e umidade
- LDR: luminosidade ambiente

## Comunicação

Os dados são enviados via MQTT no tópico:

```
clyvo/pet/ambiente
```

## Payload enviado

```
{
  "temperatura": 26.5,
  "umidade": 61.0,
  "luminosidade": 1890
}
```

## Bibliotecas necessárias na Arduino IDE

- WiFi
- PubSubClient
- DHT sensor library
- Adafruit Unified Sensor

## Configuração
Edite no arquivo sketch.ino:
```
#define WIFI_SSID "NOME_DA_SUA_REDE"
#define WIFI_PASSWORD "SENHA_DA_SUA_REDE"
```

## Pinos usados
DHT11: GPIO 4
LDR: GPIO 34