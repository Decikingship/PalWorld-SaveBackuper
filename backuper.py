import shutil
import time
import os
from datetime import datetime

# 源文件夹路径
source_folder = ''
while source_folder == '':
    source_folder = input(r'输入存档所在文件夹路径,比如C:\Users\Administrator\Desktop\steamcmd\steamapps\common\PalServer\Pal\Saved\SaveGames\0: ').replace('"', '').strip()
    if source_folder == '':
        source_folder = r'C:\Users\Administrator\Desktop\steamcmd\steamapps\common\PalServer\Pal\Saved\SaveGames\0'

# 备份文件夹的基础路径
backup_base_folder = r'C:\Backups'

# 无限循环，程序将持续运行
while True:
    # 检查备份基础文件夹是否存在，如果不存在，则创建它
    if not os.path.exists(backup_base_folder):
        os.makedirs(backup_base_folder)
        print(f'备份文件夹{backup_base_folder}已创建.')

    # 获取当前时间，并格式化为年月日时分秒
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    # 创建备份文件夹的路径
    backup_folder = os.path.join(backup_base_folder, f'Backup_{timestamp}')

    try:
        # 使用shutil.copytree来复制整个文件夹
        shutil.copytree(source_folder, backup_folder)
        print(f'成功于{backup_folder}完成备份')
    except Exception as e:
        # 如果发生任何错误，打印错误信息
        print(f'备份错误: {e}')

    time.sleep(900)
