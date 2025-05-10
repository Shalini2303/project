
# Raspberry Pi AI Camera - Real-Time Basket Item Detection

## Overview
This application uses a Raspberry Pi with an AI camera and a YOLOv5 model to detect and identify items dropped into a basket in real time. It sends item events to an MQTT broker.

## Prerequisites
- Raspberry Pi 4 / Zero 2 W with camera support
- Python 3.8+
- Internet access for model loading (optional if using local model)
- MQTT Broker (e.g., Mosquitto)

## Setup Instructions

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the detection script:
```bash
python raspi_camera_infer.py
```

3. Ensure your MQTT broker is running and reachable at the IP defined in the script (`localhost` by default).

## Notes
- Replace YOLOv5 model with a custom trained `.pt` model for accurate item detection.
- Frame capture happens every 0.2 seconds with confidence threshold > 0.5.
- For production, mount the camera over the basket or on shelves and fine-tune the model.
