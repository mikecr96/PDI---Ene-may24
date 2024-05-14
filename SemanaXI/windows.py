import cv2 as cv

img = cv.imread("/Users/miguelcamargorojas/Documents/UP/PDI - Ene-may24/images/aero1.jpg")
# img2 = cv.imread("/Users/miguelcamargorojas/Documents/UP/PDI - Ene-may24/images/aero3.jpg")

while True:
    tecla_presionada = cv.waitKey(33)
    cv.imshow("PRUEBA", img)
    # cv.imshow("PRUEBA", img2)
    if tecla_presionada == ord("q"):
        # print("sí")
        break
    elif tecla_presionada == ord("b"):
        img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        binaria = cv.threshold(img_gray, 127, 255, cv.THRESH_BINARY)[1]
        cv.imshow("binarizada", binaria)
    
cv.destroyAllWindows()
