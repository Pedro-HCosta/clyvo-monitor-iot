import cv2
import time

from camera import Camera
from config import CAMERA_INDEX, MIN_CONTOUR_AREA, CSV_INTERVAL_SECONDS, DATA_FILE_PATH, WINDOW_NAME, REGIONS
from motion_detector import MotionDetector
from region_detector import RegionDetector
from metrics import BehaviorMetrics
from csv_logger import CSVLogger


def draw_regions(frame):
    for name, region in REGIONS.items():
        x = region["x"]
        y = region["y"]
        w = region["w"]
        h = region["h"]

        cv2.rectangle(
            frame,
            (x, y),
            (x + w, y + h),
            (255, 0, 0),
            2
        )

        cv2.putText(
            frame,
            name.upper(),
            (x, y - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (255, 0, 0),
            2
        )


def draw_motion(frame, motion_data):
    if motion_data is None:
        return

    x = motion_data["x"]
    y = motion_data["y"]
    w = motion_data["w"]
    h = motion_data["h"]
    center_x = motion_data["center_x"]
    center_y = motion_data["center_y"]

    cv2.rectangle(
        frame,
        (x, y),
        (x + w, y + h),
        (0, 255, 0),
        2
    )

    cv2.circle(
        frame,
        (center_x, center_y),
        5,
        (0, 255, 255),
        -1
    )


def draw_info(frame, metrics):
    data = metrics.to_dict()
    alert = metrics.get_alert()

    cv2.putText(
        frame,
        f"Status: {data['status']}",
        (20, 35),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (0, 255, 0),
        2
    )

    cv2.putText(
        frame,
        f"Regiao: {data['regiao_atual']}",
        (20, 70),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (0, 255, 255),
        2
    )

    cv2.putText(
        frame,
        f"Parado: {data['tempo_parado_seg']}s",
        (20, 105),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (0, 255, 255),
        2
    )

    cv2.putText(
        frame,
        f"Movimentos: {data['movimentos']}",
        (20, 140),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (255, 255, 0),
        2
    )

    cv2.putText(
        frame,
        alert,
        (20, 175),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (0, 0, 255),
        2
    )


def main():
    camera = Camera(CAMERA_INDEX)
    motion_detector = MotionDetector(MIN_CONTOUR_AREA)
    region_detector = RegionDetector(REGIONS)
    metrics = BehaviorMetrics()
    csv_logger = CSVLogger(DATA_FILE_PATH)

    first_frame = camera.read()
    motion_detector.initialize(first_frame)

    last_csv_save = time.time()

    while True:
        frame = camera.read()

        motion_data, _ = motion_detector.detect(frame)

        if motion_data is not None:
            region = region_detector.detect_region(
                motion_data["center_x"],
                motion_data["center_y"]
            )
            metrics.update(True, region)
        else:
            metrics.update(False, metrics.current_region)

        draw_regions(frame)
        draw_motion(frame, motion_data)
        draw_info(frame, metrics)

        if time.time() - last_csv_save >= CSV_INTERVAL_SECONDS:
            csv_logger.save(metrics.to_dict())
            last_csv_save = time.time()

        cv2.imshow(WINDOW_NAME, frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    camera.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()