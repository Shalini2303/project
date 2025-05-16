from qreader import QRReader

class QRCodeScanner:
    def __init__(self):
        self.qr = QRReader()

    def scan(self, frame):
        results = self.qr.detect(frame)
        # results is a list of decoded QR codes or empty if none
        return results
