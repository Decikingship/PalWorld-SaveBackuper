# PalWorld-SaveBackuper
这个项目用于自动备份PalWorld的存档,每15分钟备份一次
## 使用方法
###  方法一:使用exe文件
直接下载并使用该文件,这个程序会被WindowsDefender判定为病毒,如果不放心请直接使用源代码:

https://github.com/Decikingship/PalWorld-SaveBackuper/releases/tag/Windows
###  方法二:使用源代码
1. 安装Python3.x(如已安装请跳过): https://www.python.org/downloads/
2. 安装git(如已安装请跳过): https://git-scm.com/downloads
3. 克隆本项目: `git clone https://github.com/Decikingship/PalWorld-SaveBackuper.git`
4. 使用cmd进入项目目录。
5. cmd执行安装依赖: `pip install -r requirements.txt`
6. 运行本项目: `python backuper.py`
7. 输入你的存档路径(比如`C:\Users\Administrator\Desktop\steamcmd\steamapps\common\PalServer\Pal\Saved\SaveGames\0`)并回车,这也是默认的存档路径。

## License
本项目基于Apache-2.0协议开源,可以随意修改。
