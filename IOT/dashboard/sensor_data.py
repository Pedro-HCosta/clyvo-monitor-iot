class SensorData:
    def __init__(self):
        self.temperature = None
        self.humidity = None
        self.luminosity = None
        self.last_update = None
        self.history = []

    def update(self, temperature, humidity, luminosity):
        self.temperature = temperature
        self.humidity = humidity
        self.luminosity = luminosity
        self.last_update = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        self.history.append({
            "timestamp": self.last_update,
            "temperatura": temperature,
            "umidade": humidity,
            "luminosidade": luminosity
        })

        if len(self.history) > 100:
            self.history.pop(0)

    def to_dict(self):
        return {
            "temperatura": self.temperature,
            "umidade": self.humidity,
            "luminosidade": self.luminosity,
            "ultima_atualizacao": self.last_update
        }

    def get_status(self):
        alerts = []

        if self.temperature is not None:
            if self.temperature >= 30:
                alerts.append("Temperatura elevada")
            elif self.temperature <= 15:
                alerts.append("Temperatura baixa")

        if self.humidity is not None:
            if self.humidity >= 75:
                alerts.append("Umidade elevada")
            elif self.humidity <= 30:
                alerts.append("Umidade baixa")

        if self.luminosity is not None:
            if self.luminosity <= 500:
                alerts.append("Ambiente escuro")
            elif self.luminosity >= 3500:
                alerts.append("Luminosidade intensa")

        if not alerts:
            return "Ambiente dentro do padrão"

        return " | ".join(alerts)