# # # from flask import Flask, render_template, Response
# # # from camera import Camera

# # # app = Flask(__name__)

# # # @app.route('/')
# # # def index():
# # #     return render_template('index.html')

# # # # def generate(camera):
# # # #     while True:
# # # #         frame = camera.get_frame()
# # # #         yield (b'--frame\r\n'
# # # #                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

# # # # def generate(camera):
# # # #     while True:
# # # #         frame, audio = camera.get_frame()
# # # #         yield (b'--frame\r\n'
# # # #                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n'
# # # #                b'--frame\r\n'
# # # #                b'Content-Type: audio/mp3\r\n\r\n' + audio.read() + b'\r\n\r\n')

# # # def generate(camera):
# # #     while True:
# # #         frame, audio_path = camera.get_frame()
        
# # #         if frame is not None:
# # #             yield (b'--frame\r\n'
# # #                    b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

# # #             if audio_path is not None:
# # #                 with open(audio_path, 'rb') as audio_file:
# # #                     yield (b'--frame\r\n'
# # #                            b'Content-Type: audio/mp3\r\n\r\n' + audio_file.read() + b'\r\n\r\n')

        
# # # @app.route('/video_feed')
# # # def video_feed():
# # #     return Response(generate(Camera("C:/Users/DELL/Desktop/Livesitter/production_id_4624594 (1080p).mp4")), mimetype='video/mp4')

# # # if __name__ == '__main__':
# # #     app.run(debug=True)

# # from flask import Flask, render_template, Response
# # from camera import Camera

# # app = Flask(__name__)

# # @app.route('/')
# # def index():
# #     return render_template('index.html')

# # def generate(camera):
# #     while True:
# #         frame = camera.get_frame()
# #         yield (b'--frame\r\n'
# #                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

# # @app.route('/video_feed')
# # def video_feed():
# #     return Response(generate(Camera("C:/Users/DELL/Desktop/Livesitter/production_id_4624594 (1080p).mp4")),
# #                     mimetype='multipart/x-mixed-replace; boundary=frame')

# # if __name__ == '__main__':
# #     app.run(debug=True, port=5000)

# from flask import Flask, render_template, Response, send_file
# from camera import Camera

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('index.html')

# def generate(camera):
#     while True:
#         frame = camera.get_frame()
#         yield (b'--frame\r\n'
#                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
        
# @app.route('/video_feed')
# def video_feed():
#     video_path = "static/videos/production_id_4624594 (1080p).mp4"
#     return Response(generate(Camera(video_path)),
#                     mimetype='multipart/x-mixed-replace; boundary=frame')

# print(app.url_map)

# if __name__ == '__main__':
#     app.run(debug=True, port=5000)

from flask import Flask, render_template, Response
import cv2
from flask_cors import CORS

app = Flask(__name__)
CORS(app) 
# CORS(app, resources={'/video_feed': {"origins": " http://localhost:5173/"}})
# CORS(app, resources={r'/video_feed': {"origins": "http://localhost:5173/"}})


# Replace this with your actual RTSP URL
RTSP_URL = "static/video.mp4"

@app.route('/')
def index():
    return render_template('index.html')

def generate_frames():
    cap = cv2.VideoCapture(RTSP_URL)

    while True:
        success, frame = cap.read()

        if not success:
            break

        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

    cap.release()

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=True)
