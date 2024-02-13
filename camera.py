import cv2
from cv2 import VideoCapture
from vlc import MediaPlayer
from moviepy.editor import VideoFileClip

class Camera(object):
    def __init__(self, video_path):
        self.video_path = video_path
        self.video = VideoCapture(self.video_path)
        self.player = MediaPlayer(self.video_path)

    def __del__(self):
        self.video.release()

    def extract_audio(self, output_path='output.mp3'):
        video_clip = VideoFileClip(self.video_path)
        audio_clip = video_clip.audio
        audio_clip.write_audiofile(output_path, codec='mp3', bitrate='192k')
        video_clip.close()

    def get_frame(self):
        success, image = self.video.read()
        if not success:
            self.video.set(cv2.CAP_PROP_POS_FRAMES, 0)
            _, image = self.video.read()
            ret, jpeg = cv2.imencode('.jpg', image)
            if success:
                return jpeg.tobytes(), 'output.mp3'
            else:
                return None, None

    def play(self):
        self.player.play()

    def pause(self):
        self.player.pause()

    def set_volume(self, volume):
        self.player.audio_set_volume(volume)
# import cv2
# import vlc
# from cv2 import VideoCapture
# from vlc import MediaPlayer
# class Camera(object):
#     # def __init__(self, video_path):
#     #     self.video = cv2.VideoCapture(video_path)
#     #     player=vlc.MediaPlayer(video_path)

#     def __init__(self, video_path): 
#         self.video_path = video_path
#         self.video = VideoCapture(self.video_path) 
#         self.player = MediaPlayer(self.video_path) 
#         # self.video_path = video_path
#         print("printed:" + str(self.player))
#         # sound = self.player.video_get_track(1).get_default_channel() 
#         track = self.player.video_get_track(1)  # Get the video track
#         sound = track.get_default_channel()  # Get the default channel
#         sound_data = sound.get_frames() 
#         sound = open('output.mp3', 'w') 
#         sound.write(bytes(sound_data)) 
#         sound.close()

# #     def __del__(self):
# #         self.video.release()

#     # def get_frame(self):
#     #     success, image = self.video.read()
#     #     if not success:
#     #         # If there are no more frames in the video, rewind to the beginning
#     #         self.video.set(cv2.CAP_PROP_POS_FRAMES, 0)
#     #         _, image = self.video.read()
#     #     ret, jpeg = cv2.imencode('.jpg', image)
#     #     return jpeg.tobytes()
    
#     # def get_frame(self): 
#     #     success, image = self.video.read() 
#     #     if not success: # If there are no more frames in the video, go back to the beginning 
#     #         self.video.set(cv2.cap_prop_pos_frames, 0) 
#     #         _, image = self.video.read() 
#     #         ret, jpeg = cv2.imencode('.jpg', image) 
#     #         return jpeg.tobytes(), open('output.mp3', 'rb').
        
        
    

        
# import cv2
# from cv2 import VideoCapture
# from vlc import MediaPlayer
# from moviepy.editor import VideoFileClip

# class Camera(object):
#     def __init__(self, video_path):
#         self.video_path = video_path
#         self.video = VideoCapture(self.video_path)
#         self.player = MediaPlayer(self.video_path)
#         self.extract_audio()

#     def __del__(self):
#         self.video.release()

#     def extract_audio(self, output_path='output.mp3'):
#         video_clip = VideoFileClip(self.video_path)
#         audio_clip = video_clip.audio
#         audio_clip.write_audiofile(output_path, codec='mp3', bitrate='192k')
#         video_clip.close()

#     def get_frame(self):
#         success, image = self.video.read()
#         if not success:
#             self.video.set(cv2.CAP_PROP_POS_FRAMES, 0)
#             _, image = self.video.read()

#         ret, jpeg = cv2.imencode('.jpg', image)
#         return jpeg.tobytes()

# if __name__ == "__main__":
#     # Example usage
#     video_path = 'path/to/your/video.mp4'
#     camera = Camera(video_path)
#     camera.run(debug=True)

# import cv2
# from cv2 import VideoCapture

# class Camera(object):
#     def __init__(self, video_path):
#         self.video_path = video_path
#         self.video = VideoCapture(self.video_path)

#     def __del__(self):
#         self.video.release()

#     def get_frame(self):
#         success, image = self.video.read()
#         if not success:
#             self.video.set(cv2.CAP_PROP_POS_FRAMES, 0)
#             _, image = self.video.read()

#         ret, jpeg = cv2.imencode('.jpg', image)
#         return jpeg.tobytes()
