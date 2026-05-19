import time
import pandas as pd
import streamlit as st

from sensor_data import SensorData
from mqtt_client import MQTTClient

MQTT_BROKER = "broker.hivemq.com"
MQTT_PORT = 1883
MQTT_TOPIC = "clyvo/pet/ambiente"

st.set_page_config(
    page_title="Clyvo Pet Monitor - IoT",
    page_icon="🐾",
    layout="wide"
)

if "sensor_data" not in st.session_state:
    st.session_state.sensor_data = SensorData()

if "mqtt_started" not in st.session_state:
    mqtt_client = MQTTClient(
        MQTT_BROKER,
        MQTT_PORT,
        MQTT_TOPIC,
        st.session_state.sensor_data
    )

    mqtt_client.start()

    st.session_state.mqtt_client = mqtt_client
    st.session_state.mqtt_started = True

st.title("Clyvo Pet Monitor - Dashboard IoT")

st.write("Monitoramento ambiental com ESP32, DHT11, LDR e MQTT.")

data = st.session_state.sensor_data.to_dict()
status = st.session_state.sensor_data.get_status()

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Temperatura",
        f"{data['temperatura']} °C" if data["temperatura"] is not None else "Aguardando"
    )

with col2:
    st.metric(
        "Umidade",
        f"{data['umidade']} %" if data["umidade"] is not None else "Aguardando"
    )

with col3:
    st.metric(
        "Luminosidade",
        data["luminosidade"] if data["luminosidade"] is not None else "Aguardando"
    )

st.subheader("Status ambiental")
st.info(status)

st.subheader("Última atualização")
st.write(data["ultima_atualizacao"] if data["ultima_atualizacao"] else "Nenhum dado recebido ainda.")

history = st.session_state.sensor_data.history

if history:
    df = pd.DataFrame(history)

    st.subheader("Histórico de leituras")
    st.dataframe(df, use_container_width=True)

    st.subheader("Gráfico de temperatura")
    st.line_chart(df.set_index("timestamp")["temperatura"])

    st.subheader("Gráfico de umidade")
    st.line_chart(df.set_index("timestamp")["umidade"])

    st.subheader("Gráfico de luminosidade")
    st.line_chart(df.set_index("timestamp")["luminosidade"])
else:
    st.warning("Aguardando dados do ESP32 via MQTT...")

time.sleep(2)
st.rerun()