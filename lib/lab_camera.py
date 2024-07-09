import cv2
from picamera2 import Picamera2, Preview
import os
from dotenv import load_dotenv

# # .envファイルの読み込み
load_dotenv()

# Picamera
camera = Picamera2()
camera.configure(camera.create_preview_configuration(main={
    "format": 'XRGB8888',
    "size": (1920, 1080)
}))
# camera.start_preview( Preview.QTGL, width = 200, height = 300 )
camera.start()
# camera.set_controls({'AfMode': controls.AfModeEnum.Continuous})


image = camera.capture_array()


channels = 1 if len(image.shape) == 2 else image.shape[2]
if channels == 1:
    image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
if channels == 4:
    image = cv2.cvtColor(image, cv2.COLOR_BGRA2BGR)

flipped_image = cv2.flip(image, 0)

# jpg
cv2.imwrite(os.getenv('IMG_PATH'), flipped_image)