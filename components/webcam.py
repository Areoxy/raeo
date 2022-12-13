import cv2

def take_photo():
    # Öffnen Sie die Webcam
    cap = cv2.VideoCapture(0)

    # Lesen Sie das nächste Frame von der Webcam
    ret, frame = cap.read()

    # Speichern Sie das Bild in der Datei "webcam.png"
    cv2.imwrite("webcam.png", frame)

    # Schließen Sie die Webcam
    cap.release()

