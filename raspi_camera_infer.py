import cv2
import torch
import json
import time
from datetime import datetime, timezone
import paho.mqtt.publish as publish

# Load YOLOv5 model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)  # You can change to a custom model if needed

# Video capture setup
cap = cv2.VideoCapture(0)

# MQTT configuration
MQTT_BROKER = "localhost"
MQTT_TOPIC = "store/basket/events"

print("Starting item detection... Press Ctrl+C or 'q' to stop.")

try:
    while True:
        ret, frame = cap.read()
        if not ret:
            continue

        # Run inference
        results = model(frame)

        # Parse and handle detection results
        for *box, conf, cls in results.xyxy[0]:
            label = model.names[int(cls)]
            confidence = float(conf)
            if confidence > 0.5:
                # Prepare payload
                item_event = {
                    "item": label,
                    "confidence": round(confidence, 2),
                    "timestamp": datetime.now(timezone.utc).isoformat()
                }
                payload = json.dumps(item_event)

                # Publish MQTT message
                publish.single(MQTT_TOPIC, payload, hostname=MQTT_BROKER)
                print("Published:", payload)

                # Draw box and label on frame
                x1, y1, x2, y2 = map(int, box)
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(frame, f"{label} {confidence:.2f}", (x1, y1 - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

        # Display the frame
        cv2.imshow("YOLOv5 Detection", frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        time.sleep(0.2)

except KeyboardInterrupt:
    print("Stopping detection.")

finally:
    cap.release()
    cv2.destroyAllWindows()
