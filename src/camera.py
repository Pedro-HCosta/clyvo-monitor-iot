import cv2


class Camera:
    def __init__(self, camera_index):
        self.camera = cv2.VideoCapture(camera_index)

        if not self.camera.isOpened():
            raise RuntimeError("Erro: não foi possível acessar a webcam.")

    def read(self):
        ret, frame = self.camera.read()

        if not ret:
            raise RuntimeError("Erro: não foi possível capturar o frame.")

        return frame

    def release(self):
        self.camera.release()