import numpy as np
import cv2 as cv
import sys

#resim açar
#img = cv.imread("C:\Program Files (x86)\deneme.jpg")
("""while True: 
    cv.imshow("resim",img)
    if cv.waitKey(0) == ord("q"):
        break

cv.destroyAllWindows()""")
#ek    
("""black = np.zeros((500,500,3),np.uint8)
    white = np.ones((500,500,3),np.uint8)*255

    black_kesik=black[0:200,0:500]
    white_kesik=white[0:200,0:200]

    white[0:200,0:500] = black_kesik""")
#  
("""while True:

    for i in  range (0,200):
        black[i] = [0]

    cv.imshow("Resim", img)
    cv.imshow("resim", black)
    k = cv.waitKey(0)
    if k == ord("s"):
        break
    
cv.destroyAllWindows()
""")

#video yansıtma
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

#video kaydetme
("""vid = cv.VideoCapture(0)
fourcc = cv.VideoWriter_fourcc(*"XVID")
out = cv.VideoWriter("output.avi", fourcc, 20.0, (640,480))

while vid.isOpened():
    ret , frame = vid.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    
    out.write(frame)
    cv.imshow("goruntu",frame)
    if cv.waitKey(1) == ord("q"):
        break
vid.release()
out.release()
cv.destroyAllWindows()""")


#video üzerinde piksel değiştirme
("""video = cv.VideoCapture(0)
black=np.zeros((200,640,3),np.uint8)
white=np.ones((100,640,3),np.uint8)*255
while True:
    ret , frame = video.read()
    frame[0:200,0:640]=black
    frame[380:480,0:640]=white
    if cv.waitKey(1) == ord("q"):
        break 
    cv.imshow("video", frame)

video.release()
cv.destroyAllWindows()""")

resim = cv.imread("C:\Program Files (x86)\ptesla.jpg",0)
plaka = cv.imread("C:\Program Files (x86)\plaka.jpg",0)
h,w=plaka.shape

methods=['cv.TM_CCOEFF', 'cv.TM_CCOEFF_NORMED', 'cv.TM_CCORR',
 'cv.TM_CCORR_NORMED', 'cv.TM_SQDIFF', 'cv.TM_SQDIFF_NORMED']

for meth in methods:
    resim2= resim.copy()
    method = eval(meth)

    sonuc = cv.matchTemplate(resim2,plaka, method)
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(sonuc)
 
    if method in [cv.TM_SQDIFF, cv.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc

    bottom_right = (top_left[0] + w, top_left[1] + h)
    cv.rectangle(resim2, top_left ,bottom_right, 0, 3 )
    cv.imshow(  "resim", resim2)
    cv.waitKey(0)
    cv.destroyAllWindows()












