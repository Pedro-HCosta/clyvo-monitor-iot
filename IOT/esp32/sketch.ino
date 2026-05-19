#include <WiFi.h>
#include <PubSubClient.h>
#include <DHT.h>
#include "config.h"

WiFiClient espClient;
PubSubClient mqttClient(espClient);
DHT dht(DHT_PIN, DHT_TYPE);

unsigned long lastSendTime = 0;

void connectWiFi() {
  Serial.print("Conectando ao WiFi");

  WiFi.begin(WIFI_SSID, WIFI_PASSWORD);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println();
  Serial.println("WiFi conectado");
  Serial.print("IP: ");
  Serial.println(WiFi.localIP());
}

void connectMQTT() {
  while (!mqttClient.connected()) {
    Serial.print("Conectando ao MQTT...");

    String clientId = "clyvo-pet-iot-";
    clientId += String(random(0xffff), HEX);

    if (mqttClient.connect(clientId.c_str())) {
      Serial.println("conectado");
    } else {
      Serial.print("falhou, rc=");
      Serial.print(mqttClient.state());
      Serial.println(" tentando novamente em 2s");
      delay(2000);
    }
  }
}

void sendSensorData() {
  float temperatura = dht.readTemperature();
  float umidade = dht.readHumidity();
  int luminosidade = analogRead(LDR_PIN);

  if (isnan(temperatura) || isnan(umidade)) {
    Serial.println("Erro ao ler DHT11");
    return;
  }

  String payload = "{";
  payload += "\"temperatura\":";
  payload += String(temperatura, 1);
  payload += ",";
  payload += "\"umidade\":";
  payload += String(umidade, 1);
  payload += ",";
  payload += "\"luminosidade\":";
  payload += String(luminosidade);
  payload += "}";

  mqttClient.publish(MQTT_TOPIC, payload.c_str());

  Serial.print("Publicado: ");
  Serial.println(payload);
}

void setup() {
  Serial.begin(115200);

  dht.begin();

  connectWiFi();

  mqttClient.setServer(MQTT_SERVER, MQTT_PORT);
}

void loop() {
  if (!mqttClient.connected()) {
    connectMQTT();
  }

  mqttClient.loop();

  unsigned long currentTime = millis();

  if (currentTime - lastSendTime >= SEND_INTERVAL) {
    sendSensorData();
    lastSendTime = currentTime;
  }
}