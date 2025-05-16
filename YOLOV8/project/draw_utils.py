import cv2

def draw_boxes(frame, results, model):
    """
    Draw bounding boxes and labels on the frame from YOLOv8 results.

    Args:
        frame (np.array): Image frame (BGR)
        results: YOLOv8 inference results
        model: YOLOv8 model instance for class names
    """
    for result in results:
        boxes = result.boxes
        for box in boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            conf = box.conf[0]
            cls = int(box.cls[0])
            label = model.names[cls]

            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            text = f"{label} {conf:.2f}"
            cv2.putText(frame, text, (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    return frame
