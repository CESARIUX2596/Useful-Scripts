#!/usr/bin/python3
'''
This script exists because I got a video capture and only one HDMI port in my monitor.
Not recomended for latency sensitive aplications...
To exit the app press ESC on your keyboard
'''

from cv2 import cv2
import sys


def main():
    print('Note: To close the app press the ESC key in your keyboard')
    if len(sys.argv) == 1:
        valid = False
        while(valid == False):
            print('Select your input device:')
            print('[0] Build in Camera\n[1]External Video Capture 1\n[2]External Video Capture 2\n[3]External Video Capture 3\n')
            try:
                selected_device = int(input())
            except:
                print('Select a valid device')

            if selected_device > 0 and selected_device < 4:
                ok = input('You selected {} as your device, is that ok? Yes or No: \n'.format(
                    selected_device))
                if (ok == 'y' or ok == 'yes' or ok == 'Y' or ok == 'YES' or ok == 'Yes'):
                    valid = True
            else:
                print('Selection out of bounds\n')
    else:
        selected_device = int(sys.argv[1])

    # print(selected_device)

    capture = cv2.VideoCapture(selected_device)

    while(True):

        ret, frame = capture.read()

        cv2.imshow('video', frame)

        if cv2.waitKey(1) == 27:
            break

    capture.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
