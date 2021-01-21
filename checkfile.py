import time
from pathlib import Path
import shutil

# 格式化当前时间
#date = time.strftime('%Y %m %d',time.localtime())
Date_origin_file = '2021 01 21'
Date_csv = '2021-1-21'

# 设置工作路径
workdir = '/Users/dengshiqi/Desktop/'
origin_file_Path = Path(workdir+Date_origin_file + '/')
csv_file_Path = Path(workdir+'csv/' + Date_csv + '-')

# 检查文件夹下是否存在下机文件
if origin_file_Path.is_dir():
    shutil.copytree(workdir+Date_origin_file,workdir + 'test/' + Date_origin_file)
    print('下机数据已拷贝！')
    for num in range(1, 4):
        csv_file = str(csv_file_Path) + str(num) + '.csv'
        csv_file_Path_test=Path(csv_file)
        local_csv_file_Path = workdir + 'test/csv/' + Date_csv + '-' + str(num) + '.csv'
        if csv_file_Path_test.is_file():
            shutil.copy(csv_file,local_csv_file_Path)
            print('加样顺序已准备就绪')
        else:
            pass
else:
    print("当前数据还未下机，请耐心等候！")
