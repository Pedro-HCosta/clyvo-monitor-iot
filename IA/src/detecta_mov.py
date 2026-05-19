import cv2


class MotionDetector:
    def __init__(self, min_contour_area):
        self.min_contour_area = min_contour_area
        self.previous_frame = None

    def prepare_frame(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (21, 21), 0)
        return gray

    def initialize(self, frame):
        self.previous_frame = self.prepare_frame(frame)

    def detect(self, frame):
        current_frame = self.prepare_frame(frame)

        if self.previous_frame is None:
            self.previous_frame = current_frame
            return None

        difference = cv2.absdiff(self.previous_frame, current_frame)
        threshold = cv2.threshold(difference, 25, 255, cv2.THRESH_BINARY)[1]
        threshold = cv2.dilate(threshold, None, iterations=2)

        contours, _ = cv2.findContours(
            threshold,
            cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_SIMPLE
        )

        largest_contour = None
        largest_area = 0

        for contour in contours:
            area = cv2.contourArea(contour)

            if area < self.min_contour_area:
                continue

            if area > largest_area:
                largest_area = area
                largest_contour = contour

        self.previous_frame = current_frame

        if largest_contour is None:
            return None

        x, y, w, h = cv2.boundingRect(largest_contour)

        return {
            "x": x,
            "y": y,
            "w": w,
            "h": h,
            "center_x": x + w // 2,
            "center_y": y + h // 2,
            "area": largest_area
        }