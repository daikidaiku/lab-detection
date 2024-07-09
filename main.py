# main.py
import os
import subprocess
from dotenv import load_dotenv

# .envファイルの読み込み
load_dotenv()

def main():
    root_dir = current_dir = os.path.dirname(__file__)
    
    take_photo_path = os.path.join(root_dir, "lib", "lab_camera.py")
    take_photo = subprocess.run(["python3", take_photo_path], capture_output=True, text=True)

    detect_path = os.path.join(root_dir, "yolov5", "detect.py")
    python_path = os.path.join(root_dir, "yolov5", "env", "bin", "python")
    detect = subprocess.run([python_path, detect_path , "--source", os.getenv('IMG_PATH'), "--exist-ok", "--save-txt"], capture_output=True, text=True)

    move_image_path = os.path.join(root_dir, "lib", "move_imgs.py")
    move_image = subprocess.run(["python3", move_image_path], capture_output=True, text=True)

    mobe_label_path = os.path.join(root_dir, "lib", "move_labels.py")
    move_label = subprocess.run(["python3", mobe_label_path], capture_output=True, text=True)

    upload_path = os.path.join(os.getenv('PYWORKS_PATH'),"upload-lab-photo","main.py")
    upload_image = subprocess.run(["python3", upload_path], capture_output=True, text=True)

    print(upload_image.stdout)
    print(upload_image.stderr)

if __name__ == "__main__":
    main()