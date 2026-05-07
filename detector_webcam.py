import cv2
import time

camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("Erro: não foi possível acessar a webcam.")
    exit()

ret, frame_anterior = camera.read()

if not ret:
    print("Erro: não foi possível capturar o primeiro frame.")
    camera.release()
    exit()

frame_anterior = cv2.cvtColor(frame_anterior, cv2.COLOR_BGR2GRAY)
frame_anterior = cv2.GaussianBlur(frame_anterior, (21, 21), 0)

tempo_inicio_parado = None
tempo_total_parado = 0
movimentos_detectados = 0

while True:
    ret, frame_atual = camera.read()

    if not ret:
        print("Erro ao capturar frame.")
        break

    frame_cinza = cv2.cvtColor(frame_atual, cv2.COLOR_BGR2GRAY)
    frame_cinza = cv2.GaussianBlur(frame_cinza, (21, 21), 0)

    diferenca = cv2.absdiff(frame_anterior, frame_cinza)
    limiar = cv2.threshold(diferenca, 25, 255, cv2.THRESH_BINARY)[1]
    limiar = cv2.dilate(limiar, None, iterations=2)

    contornos, _ = cv2.findContours(
        limiar,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    movimento_detectado = False

    for contorno in contornos:
        if cv2.contourArea(contorno) < 1200:
            continue

        movimento_detectado = True

        x, y, w, h = cv2.boundingRect(contorno)
        cv2.rectangle(frame_atual, (x, y), (x + w, y + h), (0, 255, 0), 2)

    if movimento_detectado:
        movimentos_detectados += 1
        tempo_inicio_parado = None
        status = "MOVIMENTO DETECTADO"
    else:
        if tempo_inicio_parado is None:
            tempo_inicio_parado = time.time()

        tempo_total_parado = int(time.time() - tempo_inicio_parado)
        status = "SEM MOVIMENTO"

    if tempo_total_parado >= 10:
        alerta = "ALERTA: comportamento parado por muito tempo"
    else:
        alerta = "Status normal"

    cv2.putText(frame_atual, f"Status: {status}", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
    cv2.putText(frame_atual, f"Tempo parado: {tempo_total_parado}s", (20, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 255), 2)
    cv2.putText(frame_atual, f"Movimentos: {movimentos_detectados}", (20, 120), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 0), 2)
    cv2.putText(frame_atual, alerta, (20, 160), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

    cv2.imshow("Clyvo Pet Monitor - Webcam", frame_atual)

    frame_anterior = frame_cinza

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()