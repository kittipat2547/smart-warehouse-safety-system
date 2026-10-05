import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("ไม่สามารถเปิดกล้องได้")
    raise SystemExit

print("เปิดกล้องสำเร็จ")
print("กด Q เพื่อออก")

while True:
    ret, frame = cap.read()

    if not ret:
        print("อ่านภาพไม่ได้")
        break

    cv2.imshow("Camera Test", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
