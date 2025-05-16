import cv2
from yolov8_inference import YOLOv8Detector
from video_stream import VideoStream
from draw_utils import draw_detections

def main():
    # Initialize modules
    video_stream = VideoStream(0)
    detector = YOLOv8Detector('yolov8n.pt')
    
    while True:
        frame = video_stream.read_frame()
        if frame is None:
            print("Failed to grab frame")
            break
        
        results = detector.detect(frame)
        
        # Draw detections on the frame
        draw_detections(frame, results, detector.model.names)
        
        # Show output window
        cv2.imshow('YOLOv8 Real-Time Detection', frame)
        
        # Quit with 'q' key
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    # Cleanup
    video_stream.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()

