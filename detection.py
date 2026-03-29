import cv2
from ultralytics import YOLO
import pyttsx3
import time

# ------------------ TTS SETUP ------------------
engine = pyttsx3.init()
engine.setProperty('rate', 150)

# ------------------ YOLO MODEL ------------------
model = YOLO("yolov8n.pt")

# ------------------ CAMERA ------------------
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Cannot access webcam")
    exit()

# ------------------ CONTROL ------------------
spoken_objects = set()   # stores already spoken objects
voice_enabled = True     # toggle voice

# ------------------ MAIN LOOP ------------------
while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame, stream=True)

    for r in results:
        for box in r.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            conf = float(box.conf[0])
            cls = int(box.cls[0])
            label = model.names[cls]

            # Draw box
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

            text = f"{label} {conf:.2f}"
            cv2.putText(frame, text, (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

            # ------------------ VOICE (ONLY ONCE) ------------------
            if voice_enabled and conf > 0.6:
                if label not in spoken_objects:
                    engine.stop()
                    engine.say(label)
                    engine.runAndWait()
                    spoken_objects.add(label)

    # Display instructions
    cv2.putText(frame, "Press V: Toggle Voice | R: Reset | ESC: Exit",
                (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 255), 2)

    cv2.imshow("Object Detection + Voice", frame)

    key = cv2.waitKey(1) & 0xFF

    # ------------------ CONTROLS ------------------
    if key == 27:  # ESC
        break
    elif key == ord('v'):  # toggle voice
        voice_enabled = not voice_enabled
        print("Voice:", "ON" if voice_enabled else "OFF")
    elif key == ord('r'):  # reset spoken objects
        spoken_objects.clear()
        print("Reset spoken objects")

# ------------------ CLEANUP ------------------
cap.release()
cv2.destroyAllWindows()