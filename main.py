from distutils.log import debug
import weakref
from cv2 import calibrateCamera
from flask import Flask, render_template, Response
import cv2 as cv
import os
# from yolov5 import detect
# import subprocess
import rospy
from sensor_msgs.msg import Image
from std_msgs.msg import String
from cv_bridge import CvBridge
from threading import Thread

# init flask app
app = Flask(__name__)
img = None
count_ = None
br = CvBridge()

# if os.environ.get('WERKZEUG_RUN_MAIN') or Flask.debug is False:
#     cam = cv.VideoCapture(0)
#     cap = cv.VideoCapture('/home/arya/Videos/video.mp4')
'''
for ip camera use - rtsp://username:password@ip_address:554/user=username_password='password'_channel=channel_number_stream=0.sdp' 
for local webcam use cv2.VideoCapture(0)
'''

def string_callback(msg):
    global count_
    count_ = msg.data
    # print('Collected counted people')
    # print(msg.data)
    # return render_template('index.html', string_variable=str(msg.data))

def callback(msg):
    global img
    # print('img received')
    img = br.imgmsg_to_cv2(msg)

rospy.Subscriber("/Camera_Detection", Image, callback, queue_size=1)
rospy.Subscriber("/People_Count", String, string_callback, queue_size=10)

def generate_frames():
    while True:
        # success, frame = cam.read()
        # if not success:
        #     break
        # else:
        if img is not None:
            ret, buffer = cv.imencode('.jpg', img)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result

@app.route('/')
def index():
    global count_
    return render_template('index.html', string_variables="Counted Person:" + str(count_))

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace;boundary=frame')

if __name__ == "__main__":
    rospy.init_node('yuagsfyasfygusafgyuaas')
    app.run(debug=True)