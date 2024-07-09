import os
import shutil
from datetime import datetime
import os
from dotenv import load_dotenv

# .envファイルの読み込み
load_dotenv()

# 移動するファイルのパス
file_path = os.getenv('LABEL_OUT')

# 移動先のディレクトリパス
backup_dir = os.getenv('LABEL_BACKUP')
if os.path.exists(file_path):
    # 現在のタイムスタンプを取得し、ファイル名に使用
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    backup_file_name = f'lab_{timestamp}.txt'

    # 移動先のファイルパス
    backup_file_path = os.path.join(backup_dir, backup_file_name)

    # 移動先のディレクトリが存在しない場合は作成
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)

    # ファイルを移動
    shutil.move(file_path, backup_file_path)

    print(f"ファイルを {backup_file_path} に移動しました。") 
else:
    print(f"{file_path} が存在しません。")