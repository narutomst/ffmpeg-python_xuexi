# ffmpeg的第一个例子
# 直接在powershell中用pip install ffmpeg-python安装ffmpeg-python包，则安装在了
# C:\Users\naruto\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages
# 这在Pycharm中没办法识别到，import ffmpeg总会出现报错【找不到模块'ffmpeg'】

# 所以，要在Pycharm中安装所需要的第三方包
# 这是在File->Settings->Project:->Project Interpreter->Project Interpreter选择框
# ->选择Python 3.7 C:\ProgramData\Anaconda3\python.exe（即conda中的base环境）->Package列表->右侧的＋
# ->Available Packages，（该页面列出了https://mirrors.aliyun.com/pypi/simple/下的所有第三方包）
# ->下方搜索框中输入“ffmpeg-python”->从搜索结果中选择“ffmpeg-python”->Install Packages
# 即在当前的base环境中安装了ffmpeg-python包，安装位置为C:\ProgramData\Anaconda3\pkgs
# 这时运行import ffmpeg没有报错，第一个将视频画面水平翻转输出的例子也成功了

import ffmpeg

inPath = r"C:\LEL\LEL-Downloader\Download\中国大学\Python语言程序设计_北京理工大学\{1}--课程" \
         r"\{1}--【第0周】课程导学\{1}--0.1课程基本情况\[1.1.1]--开课彩蛋新开始新征程.mp4"
# 路径名称前加r，表示raw string，即保持字符原始值的意思
stream = ffmpeg.input(inPath)
stream = ffmpeg.hflip(stream)
stream = ffmpeg.output(stream, "output2.mp4")
ffmpeg.run(stream)
