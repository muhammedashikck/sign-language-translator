import cv2
import mediapipe as mp
import time

BaseOptions = mp.tasks.BaseOptions
HandLandmarker = mp.tasks.vision.HandLandmarker
HandLandmarkerOptions = mp.tasks.vision.HandLandmarkerOptions
RunningMode = mp.tasks.vision.RunningMode

options = HandLandmarkerOptions(
    base_options=BaseOptions(
        model_asset_path="hand_landmarker.task"
    ),
    running_mode=RunningMode.VIDEO,
    num_hands=2
)

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Could not open camera.")
    raise SystemExit

start_time = time.monotonic()

with HandLandmarker.create_from_options(options) as landmarker:
    while True:
        success, frame = cap.read()

        if not success:
            print("Could not read camera.")
            break

        frame = cv2.flip(frame, 1)
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        mp_image = mp.Image(
            image_format=mp.ImageFormat.SRGB,
            data=rgb
        )

        timestamp = int((time.monotonic() - start_time) * 1000)
        result = landmarker.detect_for_video(mp_image, timestamp)

        if result.hand_landmarks:
            height, width, _ = frame.shape

            for hand in result.hand_landmarks:
                points = [
                    (int(p.x * width), int(p.y * height))
                    for p in hand
                ]

                for x, y in points:
                    cv2.circle(frame, (x, y), 5, (0, 255, 0), -1)

                connections = (
                    mp.tasks.vision.HandLandmarksConnections.HAND_CONNECTIONS
                )

                for connection in connections:
                    start = points[connection.start]
                    end = points[connection.end]
                    cv2.line(frame, start, end, (255, 0, 0), 2)

            message = "Hand Detected!"
            color = (0, 255, 0)
        else:
            message = "Show your hand"
            color = (0, 0, 255)

        cv2.putText(
            frame, message, (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2
        )

        cv2.imshow("Hand Detection Test", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

cap.release()
cv2.destroyAllWindows()
