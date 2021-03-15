from MotorModule import Motor
import JoyStickModule as js
from time import sleep

motor = Motor(17, 27, 22, 10, 11, 9)


def main():
    jsVal = js.getJS()
    motor.move(-(jsVal['axis3']),jsVal['axis1'],0.1)

if __name__ == '__main__':

    while True:
        main()