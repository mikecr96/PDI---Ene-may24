import cv2 as cv

cap = cv.VideoCapture(0)
cap.set(cv.CAP_PROP_FRAME_WIDTH, 100)
cap.set(cv.CAP_PROP_FRAME_HEIGHT, 100)
cv.namedWindow("frame", cv.WINDOW_AUTOSIZE)
# cv.moveWindow("frame", )

isgray = False

while cap.isOpened():
    
    ret, frame = cap.read()
    
    # frame = cv.threshold(frame, 180, 255, cv.THRESH_BINARY)[1]
    if isgray:
        frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    cv.imshow("frame", frame)

    tecla = cv.waitKey(33)
    if tecla == 27: # Tecla ESC
        break
    elif tecla == ord("g"):
        isgray = not isgray

cap.release()
cv.destroyAllWindows()