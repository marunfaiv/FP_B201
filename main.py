from distutils.log import debug
import weakref
from cv2 import calibrateCamera
from flask import Flask, render_template, Response
import cv2 as cv
import os

# init flask app
app = Flask(__name__)

if os.environ.get('WERKZEUG_RUN_MAIN') or Flask.debug is False:
    cam = cv.VideoCapture(0)
    cap = cv.VideoCapture('/home/arya/Videos/video.mp4')
'''
for ip camera use - rtsp://username:password@ip_address:554/user=username_password='password'_channel=channel_number_stream=0.sdp' 
for local webcam use cv2.VideoCapture(0)
'''

def generate_frames():
    while True:
        success, frame = cap.read()
        if not success:
            break
        else:
            ret, buffer = cv.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace;boundary=frame')

if __name__ == "__main__":
    app.run(debug=True)