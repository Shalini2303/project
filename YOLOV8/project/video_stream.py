import cv2

def open_camera(source=0):
    """Open video source. Default is webcam 0."""
    cap = cv2.VideoCapture(source)
    if not cap.isOpened():
        raise RuntimeError(f"Cannot open video source {source}")
    return cap

def release_camera(cap):
    """Release video capture."""
    cap.release()
    cv2.destroyAllWindows()
