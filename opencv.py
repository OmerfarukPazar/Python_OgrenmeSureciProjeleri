import numpy as np
import cv2 as cv
import sys

("""img = cv.imread("C:\Program Files (x86)\whatsapp.jpeg")
if img is None:
    sys.exit("Could not read the image.")

cv.imshow("Resim", img)
k = cv.waitKey()
if k == ord("s"):
    cv.imwrite("C:\Program Files (x86)\whatsapp.jpeg", img)
""")

("""vid = cv.VideoCapture(0)
if not vid.isOpened():
    print("kamera açılamadı")
    exit()
while True:
    ret , frame = vid.read()
    if not ret:
        print("kameradan kare alınamıyor")
        break
    renk = cv.cvtColor(frame,cv.COLOR_BGRA2GRAY)
    cv.imshow("frame" , renk)
    if cv.waitKey(1) == ord("q"):
        break
vid.release()
cv.destroyAllWindows()""")

vid = cv.VideoCapture(0)
fourcc = cv.VideoCapture.fourcc(*"XVID")
out = cv.VideoWriter("output.avi", fourcc, 20.0, (640,480))

while vid.isOpened():
    ret , frame = vid.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    frame = cv.flip(frame,0)
    out.write(frame)
    cv.imshow("görüntü",frame)
    if cv.waitKey(1) == ord("q"):
        break
vid.release()
out.release()
cv.destroyAllWindows()


















