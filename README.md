## 简介

+	基于[ssf2fcitx](https://github.com/VOID001/ssf2fcitx)工具进行开发，由于ssf2fcitx在Manjaro-i3发行版上有bug(不知其他发行版有没有)，遂有了此仓库

+	ssf2fcitx转换之后的皮肤没有menu.png，且没有BackArrow与ForwardArrow，我在原工具的基础上针对这两项进行了修改


## 使用

+	将下载的搜狗输入法皮肤文件放在此项目同级目录下，然后执行 `./ssf2fcitx.py  xxx.ssf` 即可

+	执行完上条命令之后会得到一个同名文件夹，将文件夹移动到 `~/.config/fcitx/skin/` 目录下(若没有skin目录，自行创建)，然后就可以开心地使用皮肤了


## 截图

![](../images/01.png)

![](../images/02.png)

![](../images/03.png)

![](../images/04.png)

![](../images/05.png)

![](../images/06.png)


## 其它

+	经测试原工具ssf2fcitx转换后，有些皮肤左右会多出很多，这个问题可以通过手动修改转换之后的文件夹内的配置文件：fcitx_skin.conf
