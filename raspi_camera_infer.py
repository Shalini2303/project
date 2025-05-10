import cv2
import torch
import json
import time
from datetime import datetime
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
# Load YOLOv5 model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)  # Replace with your custom model

# Video capture setup
cap = cv2.VideoCapture(0)

# MQTT configuration
MQTT_BROKER = "localhost"
MQTT_TOPIC = "store/basket/events"

print("Starting item detection... Press Ctrl+C to stop.")

try:
    while True:
        ret, frame = cap.read()
        if not ret:
            continue

        results = model(frame)

        # Parse results
        for *box, conf, cls in results.xyxy[0]:
            label = model.names[int(cls)]
            confidence = float(conf)
            if confidence > 0.5:
                item_event = {
                    "item": label,
                    "confidence": round(confidence, 2),
                    "timestamp": datetime.utcnow().isoformat()
                }
                payload = json.dumps(item_event)
                publish.single(MQTT_TOPIC, payload, hostname=MQTT_BROKER)
                print("Published:", payload)

        time.sleep(0.2)

except KeyboardInterrupt:
    print("Stopping detection.")
finally:
    cap.release()
