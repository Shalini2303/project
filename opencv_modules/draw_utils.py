import cv2

def draw_qr_results(frame, qr_results):
    for result in qr_results:
        pts = result.points
        # Draw polygon around QR code
        pts = pts.astype(int).reshape((-1, 1, 2))
        cv2.polylines(frame, [pts], True, (0, 255, 0), 2)

        # Put decoded text above the QR code
        text = result.data.decode('utf-8') if isinstance(result.data, bytes) else str(result.data)
        x, y = pts[0][0]
        cv2.putText(frame, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX,
                    0.6, (0, 255, 0), 2)

    return frame
