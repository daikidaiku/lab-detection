import os
import glob

def get_latest_file(folder_path):
    # 指定されたフォルダ内のlab_{timestamp}.txtファイルを取得
    files = glob.glob(os.path.join(folder_path, 'lab_*.txt'))
    if not files:
        return None
    
    # 最新のファイルを選択
    latest_file = max(files, key=os.path.getctime)
    return latest_file

def count_zero_first_column(file_path):
    count = 0
    with open(file_path, 'r') as file:
        for line in file:
            columns = line.strip().split()
            if columns and columns[0] == '0':
                count += 1
    return count

# フォルダのパスを指定
folder_path = os.getenv('LABEL_BACKUP')

# 最新のファイルを取得
latest_file = get_latest_file(folder_path)
# print(latest_file)
if latest_file:
    # 1列目が0の行の数をカウント
    zero_count = count_zero_first_column(latest_file)
    print(f"{zero_count} people are in the lab")
else:
    print("No lab_{timestamp}.txt files found in the specified folder.")
