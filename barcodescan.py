import cv2
from pyzbar import pyzbar

def decode(frame):
    decoded_objects = pyzbar.decode(frame)
    for obj in decoded_objects:
        # Draw bounding box
        (x, y, w, h) = obj.rect
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Put text
        barcode_data = obj.data.decode('utf-8')
        barcode_type = obj.type
        text = f'{barcode_data} ({barcode_type})'
        cv2.putText(frame, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

        print(f'Decoded: {barcode_data}, Type: {barcode_type}')

    return frame

def main():
    cap = cv2.VideoCapture(0)
    print("Starting barcode/QR code scanner. Press 'q' to quit.")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = decode(frame)
        cv2.imshow('Barcode/QR Code Scanner', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
