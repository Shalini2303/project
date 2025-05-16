from video_stream import VideoStream
from qrcode_reader import QRCodeScanner
from draw_utils import draw_qr_results
import cv2

def main():
    stream = VideoStream(0)  # default camera
    scanner = QRCodeScanner()

    while True:
        frame = stream.read()
        if frame is None:
            print("Failed to grab frame")
            break

        qr_results = scanner.scan(frame)

        frame = draw_qr_results(frame, qr_results)

        cv2.imshow("Real-time QR Code Scanner", frame)

        # Exit on pressing 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    stream.release()

if __name__ == "__main__":
    main()
