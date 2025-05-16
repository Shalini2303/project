from ultralytics import YOLO

def load_model(model_path='yolov8n.pt'):
    """Load and return YOLOv8 model."""
    model = YOLO(model_path)
    return model

def run_inference(model, frame):
    """Run inference on a single frame."""
    results = model(frame)
    return results
