import os
import time
import picamera

class Camera:
    def __init__(self, train_instance, data_dir):
        self.train_instance = train_instance
        self.data_dir = data_dir
        self.label = None
        self.camera = picamera.PiCamera()
        self.camera.resolution = (640, 480)
        self.camera.framerate = 80
        self.image_id = 0
        self.done = False
        if not os.path.exists(self.data_dir + self.train_instance):
            os.mkdir(os.path.join(self.data_dir + self.train_instance))


    def record(self):
        print("recording...")
        label = self.label
        if label is not None:
            image_name = "image-"+ label + "-" + str(self.image_id) + ".jpg"

            file_name = self.data_dir + self.train_instance + "/" + image_name

            self.camera.capture(file_name,use_video_port=True)
            self.image_id +=1


    def set_label(self, label):
        self.label = label

    def done(self):
        self.done = True
