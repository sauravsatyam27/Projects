import cv2

print("\n🔍 Checking camera access...\n")

for i in range(5):
    cap = cv2.VideoCapture(i, cv2.CAP_DSHOW)   # force DirectShow
    print(f"Testing index {i} -> Opened: {cap.isOpened()}")
    if cap.isOpened():
        ret, frame = cap.read()
        print("Read frame:", ret)
    cap.release()
