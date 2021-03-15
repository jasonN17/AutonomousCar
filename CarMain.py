from MotorModule import Motor
from LaneDetectionModule import getLaneCurve
import WebcamModule as webcam
import cv2
import utlis
import JoyStickModule as js
from time import sleep
##################################################
motor = Motor(17, 27, 22, 10, 11, 9)
##################################################



def main():

    if js.getJS('x') == 1:
        img = webcam.getImg()
        initialTrackBarVals = [90,110, 0, 240]
        utlis.initializeTrackbars(initialTrackBarVals)

        curveVal= getLaneCurve(img,2)
        sen = 1.5  # SENSITIVITY
        maxVAl= 0.3 # MAX SPEED
        #Normalization
        if curveVal>maxVAl:curveVal = maxVAl
        if curveVal<-maxVAl: curveVal =-maxVAl
        #print(curveVal)

        if curveVal>0:

            if curveVal<0.05: curveVal=0
        else:
            if curveVal>-0.05: curveVal=0
        motor.move(0.28,curveVal*sen,0.05)
        cv2.waitKey(1)
    else:
        cv2.destroyAllWindows()
        jsVal = js.getJS()
        motor.move(-(jsVal['axis3']),jsVal['axis1'],0.1)


if __name__ == '__main__':
    while True:
        main()