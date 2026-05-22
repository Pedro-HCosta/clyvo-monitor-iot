#include <WiFi.h>
#include <PubSubClient.h>
#include <DHT.h>

#define WIFI_SSID "NOME_DA_SUA_REDE"
#define WIFI_PASSWORD "SENHA_DA_SUA_REDE"

#define MQTT_SERVER "broker.hivemq.com"
#define MQTT_PORT 1883
#define MQTT_TOPIC "clyvo/pet/ambiente"

#define DHT_PIN 15
#define DHT_TYPE DHT22

#define LDR_PIN 34

#define SEND_INTERVAL 5000

WiFiClient espClient;
PubSubClient mqttClient(espClient);
DHT dht(DHT_PIN, DHT_TYPE);

unsigned long lastSendTime = 0;

void connectWiFi() {
  Serial.println("Iniciando conexao WiFi...");
  WiFi.begin(WIFI_SSID, WIFI_PASSWORD);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println();
  Serial.println("WiFi conectado com sucesso.");
  Serial.print("IP: ");
  Serial.println(WiFi.localIP());
}

void connectMQTT() {
  while (!mqttClient.connected()) {
    Serial.println("Tentando conectar ao broker MQTT...");

    String clientId = "clyvo-pet-iot-";
    clientId += String(random(0xffff), HEX);

    if (mqttClient.connect(clientId.c_str())) {
      Serial.println("MQTT conectado com sucesso.");
    } else {
      Serial.print("Falha MQTT. Codigo: ");
      Serial.println(mqttClient.state());
      delay(2000);
    }
  }
}

void publishSensorData() {
  Serial.println();
  Serial.println("Lendo sensores...");

  float temperatura = dht.readTemperature();
  float umidade = dht.readHumidity();
  int luminosidade = analogRead(LDR_PIN);

  Serial.print("Temperatura lida: ");
  Serial.println(temperatura);

  Serial.print("Umidade lida: ");
  Serial.println(umidade);

  Serial.print("Luminosidade lida: ");
  Serial.println(luminosidade);

  if (isnan(temperatura) || isnan(umidade)) {
    Serial.println("Erro: leitura invalida do DHT22.");
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

  Serial.print("Payload gerado: ");
  Serial.println(payload);

  bool publicado = mqttClient.publish(MQTT_TOPIC, payload.c_str());

  if (publicado) {
    Serial.println("Dados publicados no MQTT com sucesso.");
  } else {
    Serial.println("Erro: falha ao publicar no MQTT.");
  }
}

void setup() {
  Serial.begin(115200);
  delay(2000);

  Serial.println("==============================");
  Serial.println("CLYVO PET IOT");
  Serial.println("==============================");

  pinMode(LDR_PIN, INPUT);

  dht.begin();

  connectWiFi();

  mqttClient.setServer(MQTT_SERVER, MQTT_PORT);

  Serial.println("Setup finalizado.");
}

void loop() {
  Serial.println("Loop em execucao...");

  if (!mqttClient.connected()) {
    connectMQTT();
  }

  mqttClient.loop();

  unsigned long currentTime = millis();

  if (currentTime - lastSendTime >= SEND_INTERVAL) {
    publishSensorData();
    lastSendTime = currentTime;
  }

  delay(1000);
}