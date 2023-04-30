# 获取MOOC的2倍速课程音频文件
# 首先检索出所有的*.mp4文件，文件的地址类似
# "C:\LEL\LEL-Downloader\Download\中国大学\Python语言程序设计_北京理工大学\{1}--课程\{1}--【第0周】课程导学\{1}--0.1课程基本情况\[1.1.1]--开课彩蛋新开始新征程.mp4"
# 将文件地址放进一个list中，
# 然后用循环对每个mp4文件进行视频音频2倍速处理，
# 最后提取出音频2倍速文件

import ffmpeg
import os

# 固定的地址
# disk_name = ['C:\\','D:\\', 'E:\\', 'F:\\', 'G:\\']
# fixedPath = r'LEL\LEL-Downloader\Download\中国大学\Python语言程序设计_北京理工大学\{1}--课程'
disk_name = ['C:\\', 'D:\\', 'E:\\', 'F:\\', 'G:\\']  # 盘符
intermediate_path = r'LEL\LEL-Downloader\Download\中国大学\Python语言程序设计_北京理工大学\{1}--课程'  # 中间路径名称
week_name = [] # 周名称，如'{1}--【第0周】课程导学'
lesson_name = [] # 课名称，如'{1}--0.1课程基本情况'
section_name = [] # 节名称，如'[1.1.1]--开课彩蛋新开始新征程.mp4'
mp4_file_name = ['[1.1.1]--开课彩蛋新开始新征程.mp4', 'PaviaU']
# 1.搜索哪个盘中有'LEL\LEL-Downloader\Download\中国大学\Python语言程序设计_北京理工大学\{1}--课程'这个路径
for item in disk_name:
    test_path = os.path.join(item, intermediate_path)
    if os.path.exists(test_path):   #
        for fname in mat_file_name:
            full_path = os.path.join(test_path, fname + '.mat')   # 2.确认该文件夹中有所指定的mat数据文件
            if os.path.isfile(full_path):
                image_file = full_path
            full_path2 = os.path.join(test_path, fname + '_gt.mat')
            if os.path.isfile(full_path2):
                label_file = full_path2
                break
    else:
        continue
    break
# 通过遍历查找出某个文件夹内所有的子文件和指定后缀的所有文件


def get_files(path=r"C:\LEL", rule=".mp4"):
    all = []
    # os.walk是获取所有的目录
    for fpath, dirs, fs in os.walk(path):
        for f in fs:
            filename = os.path.join(fpath, f)  # 路径拼接
            # 判断是否以"rule"结尾，自定义规则
            if filename.endswith(rule):
                all.append(filename)
    return all


if __name__ == "__main__":
    fileNameList = get_files(path=fixedPath, rule=".mp4")
    for fileName in fileNameList:
        print(fileName)
        stream = ffmpeg.input(filename=fileName)
        # 对每个视频音频2倍速处理

        # 提取音频2倍速文件
        # 保存音频文件

    # 重命名音频文件，即将“{1}--【第0周】课程导学”修改为“{01}--【第0周】课程导学”
    fileList = os.listdir(fixedPath)
    fileListOut = []
    for item in fileList:
        if item[2] == "}":
            path1 = os.path.join(fixedPath, item)   # 路径拼接
            fileNameList = get_files(path=path1, rule=".m4a")   # 音频文件的格式为m4a
            # 重命名每个音频文件
            item1 = item[0] + "{:02d}".format(eval(item[1])) + item[2:]  # 从第3个字符一直取到结尾
            fileListOut.append(item1)   # 生成新文件名用于保存输出的音频文件







