class RegionDetector:
    def __init__(self, regions):
        self.regions = regions

    def detect_region(self, center_x, center_y):
        for name, region in self.regions.items():
            inside_x = region["x"] <= center_x <= region["x"] + region["w"]
            inside_y = region["y"] <= center_y <= region["y"] + region["h"]

            if inside_x and inside_y:
                return name

        return "fora_das_regioes"