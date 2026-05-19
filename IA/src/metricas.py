import time


class BehaviorMetrics:
    def __init__(self):
        self.current_region = "fora_das_regioes"
        self.previous_region = "fora_das_regioes"

        self.status = "SEM MOVIMENTO"

        self.still_start_time = None
        self.still_time = 0

        self.region_times = {
            "agua": 0,
            "racao": 0,
            "cama": 0
        }

        self.region_visits = {
            "agua": 0,
            "racao": 0,
            "cama": 0
        }

        self.movements = 0

        self.last_time = time.time()

        self.was_moving = False
        self.last_movement_count_time = 0
        self.movement_cooldown_seconds = 1.5

    def update(self, motion_detected, region):
        now = time.time()
        delta = now - self.last_time
        self.last_time = now

        if motion_detected:
            self.status = "MOVIMENTO DETECTADO"
            self.current_region = region

            can_count_movement = now - self.last_movement_count_time >= self.movement_cooldown_seconds

            if not self.was_moving and can_count_movement:
                self.movements += 1
                self.last_movement_count_time = now

            self.was_moving = True
            self.still_start_time = None

            if self.current_region != self.previous_region:
                if self.current_region in self.region_visits:
                    self.region_visits[self.current_region] += 1

            self.previous_region = self.current_region

        else:
            self.status = "SEM MOVIMENTO"
            self.was_moving = False

            if self.still_start_time is None:
                self.still_start_time = time.time()

            self.still_time = time.time() - self.still_start_time

        if self.current_region in self.region_times:
            self.region_times[self.current_region] += delta

    def get_alert(self):
        if self.still_time >= 10:
            return "ALERTA: parado por muito tempo"

        return "Status normal"

    def to_dict(self):
        return {
            "regiao_atual": self.current_region,
            "status": self.status,
            "tempo_parado_seg": int(self.still_time),
            "tempo_agua_seg": int(self.region_times["agua"]),
            "tempo_racao_seg": int(self.region_times["racao"]),
            "tempo_cama_seg": int(self.region_times["cama"]),
            "visitas_agua": self.region_visits["agua"],
            "visitas_racao": self.region_visits["racao"],
            "visitas_cama": self.region_visits["cama"],
            "movimentos": self.movements
        }