#! /usr/bin/python3

# Copyright(c) 2020 note.jorhelp.cn

# Authored by Jorhelp on: 2020年 02月 17日 星期一 14:50:58 CST

# @desc: 在原有工具的基础上针对i3做一些修复

import os
import sys
from configparser import ConfigParser


#==========================
# 全局变量
#==========================
FILE_NAME = None
DIR_NAME = None


#==========================
# 初始化
#==========================
def init():
    global FILE_NAME, DIR_NAME
    argvs = sys.argv
    if len(argvs) != 2:
        return False
    else:
        FILE_NAME = argvs[1]
        DIR_NAME = FILE_NAME.split('.')[0]
        return True


#==========================
# 调用ssf2skin
#==========================
def ssf_skin():
    try:
        os.system("resources/ssf2skin -i {} -o {}".format(FILE_NAME, DIR_NAME))
        return True
    except Exception as e:
        print(repr(e))
        return False


#==========================
# 移动文件
#==========================
def copy_file():
    if not os.path.exists("resources/menu.png"):
        print("\n  menu.png文件不存在")
        return False
    if not os.path.exists("resources/next.png"):
        print("\n  next.png文件不存在")
        return False
    if not os.path.exists("resources/prev.png"):
        print("\n  prev.png文件不存在")
        return False
    else:
        try:
            os.system("cp resources/menu.png {}/".format(DIR_NAME))
            os.system("cp resources/next.png {}/".format(DIR_NAME))
            os.system("cp resources/prev.png {}/".format(DIR_NAME))
            return True
        except Exception as e:
            print(repr(e))
            return False


#==========================
# 让配置文件保留大小写
#==========================
class myconf(ConfigParser):
    def __init__(self,defaults=None):
        ConfigParser.__init__(self,defaults=None)
    def optionxform(self, optionstr):
        return optionstr

#==========================
# 修改配置文件
#==========================
def conf():
    config_local = myconf()
    config = myconf()
    try:
        config_local.read("resources/change.conf")
        config.read("{}/fcitx_skin.conf".format(DIR_NAME))

        for section in config_local.sections():
            for item in config_local.items(section):
                # 将本地配置文件写入皮肤配置文件
                config.set(section, item[0], item[1])

        bottom = config['SkinInputBar']['MarginBottom']
        top = config['SkinInputBar']['MarginTop']
        left = config['SkinInputBar']['MarginLeft']
        right = config['SkinInputBar']['MarginRight']
        out_put_pos = config['SkinInputBar']['OutputPos']
        config.set('SkinInputBar', 'MarginBottom', str(int(bottom)-7))
        config.set('SkinInputBar', 'MarginLeft', str(int(left)-20))
        config.set('SkinInputBar', 'MarginRight', str(int(right)-20))

        config.set('SkinInputBar', 'BackArrowY', str(int(top)-20))
        config.set('SkinInputBar', 'ForwardArrowY', str(int(top)-20))
        config.set('SkinInputBar', 'BackArrowX',  str(int(right)-20))
        config.set('SkinInputBar', 'ForwardArrowX',  str(int(right)-30))
        config.set('SkinInputBar', 'OutputPos', str(int(out_put_pos)+8))

        with open("{}/fcitx_skin.conf".format(DIR_NAME), 'w+') as f:
            # 下面第二个参数默认会使等号左右有空格，坑死我了
            config.write(f, space_around_delimiters=False)

        return True
    except Exception as e:
        print(repr(e))
        return False



#==========================
# 测试
#==========================
def test():
    global DIR_NAME
    DIR_NAME = "漫画格"
    conf()
    pass


#==========================
# main
#==========================
if __name__ == "__main__":
    #  test()
    if not init():
        print("\n  无效参数 @_@")
    else:
        if not ssf_skin():
            print("\n  无法调用ssf2skin！！")
        else:
            print("\n  解包成功 @_@")
            if not copy_file():
                print("\n  复制文件失败！！")
            else:
                print("\n  复制文件成功 @_@")
                if not conf():
                    print("\n  修改配置文件失败！！")
                else:
                    print("\n  修改配置文件成功 @_@")
