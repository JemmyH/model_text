# _*_ coding:utf-8 _*_
import shutil
import os
"""
最最重要的是这两个方法：copy和move
"""

def shutil_test():
    if not os.path.exists("F:\\tianjintest\\"):
        os.mkdir("F:\\tianjintest\\")
    print(shutil.copy("F:\\image\\www.5857.com\\清纯\\白裙气质女神海边低胸写真高清手机壁纸\\001.jpg", "F:\\tianjintest\\tianjin.jpg"))
    if not os.path.exists("F:\\movetest\\"):
        os.mkdir("F:\\movetest\\")
    old_path = "F:\\tianjintest\\tianjin.jpg"
    shutil.move("F:\\tianjintest\\tianjin.jpg", "F:\\movetest\\{0}".format(old_path[-1:13]))


if __name__ == '__main__':
    shutil_test()
