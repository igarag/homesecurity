import cv2
import logging
import datetime

logger = logging.getLogger(__name__)

cam = cv2.VideoCapture('/dev/video2')

total = 70
current = 0

ret, frame = cam.read()

tic = datetime.datetime.now()

while True:
    if current >= total:
        ret, frame = cam.read()
        cv2.imshow('frame', frame)
        if (datetime.datetime.now() - tic) >  datetime.timedelta(seconds=1):
            tic = datetime.datetime.now()
        current = 0
    current += 1

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()


