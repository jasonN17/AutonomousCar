import cv2
from time import sleep
cap = cv2.VideoCapture(0)
sleep(0.05)

def getImg(display= False,size=[480,240]):
    _, img = cap.read()
    img = cv2.resize(img,(size[0],size[1]))
    if display:
        cv2.imshow('IMG',img)
    return img

if __name__ == '__main__':
    while True:
        img = getImg(True)
        cv2.waitKey(0)
    cap.release()
    cv2.destroyAllWindows()