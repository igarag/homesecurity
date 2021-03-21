import datetime
import logging

import cv2
from flask import Flask, Response, render_template, url_for

app = Flask(__name__)
logger = logging.getLogger(__name__)

camera = cv2.VideoCapture(0)

def get_camera_from_os():
    devices = 4
    for device in range(devices):
        camera = cv2.VideoCapture(f'/dev/video{device}')
        
        if camera != None:
            logging.info(f'Camera {device} selected.')
            break
        else:
            logger.error('No camera found')
    return camera

def gen_frames():  
    while True:
        success, frame = camera.read()
        if not success:
            logger.error('No camera found.')
            break
        else:
            logger.info('Sending frames')
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')



if __name__ == '__main__':

    app.run(debug=True,
            host='0.0.0.0',
            port=8000,
            threaded=True,
            use_reloader=False)

    camera.release()
