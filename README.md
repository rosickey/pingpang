# pingpang 弹球算法竞赛
![avatar](https://github.com/rosickey/pingpang/blob/master/images/ping.gif)
## *竞赛规则*
### 比赛规则
修改ball.py 文件中pad_ai(pad_pos, ball_pos)函数，编写控制球拍移动的算法，得分高者为胜
:warning: **只能**修改pad_ai函数，入口参数pad_pos、ball_pos，出口参数-1、0、1不可修改，可添加全局变量，但全局变量只限定在pad_ai函数中使用

### 提交作品
竞赛者将修改的程序在github中进行提交，或者发送代码附件到001@cosx.xyz

### 有疑问？
有安装问题或者调试问题可在issues中提问，或者发送邮件到001@cosx.xyz
![avatar](https://github.com/rosickey/pingpang/blob/master/images/ans.png)



## *安装说明*
### Windows操作系统

1.首先，推荐安装Python2.7.10 **不建议使用Python3**<a href="https://www.python.org/ftp/python/2.7.10/python-2.7.10.msi" target="_blank">点击下载python-2.7.10.msi</a>

:warning: **整个安装和调试过程不要有中文路径**
:warning: **不要**安装在中文路径，在安装过程中，请**勾选**将Python加入到系统环境变量里
![avatar](https://github.com/rosickey/pingpang/blob/master/images/install.png)

2.Python安装结束后，打开系统命令行（开始-运行-输入CMD），输入
```bash
	python
```
如果进入Python环境，表明Python安装成功，输入exit()可退出。
否则，请检查自己的系统变量path中是否有Python的安装路径，重新安装

![avatar](https://github.com/rosickey/pingpang/blob/master/images/testok.png)


3.安装成功后，重新打开系统命令行（开始-运行-输入CMD），输入
```bash
	pip install --upgrade pip
```
:warning: **此步安装最后出现错误提示，没关系**

![avatar](https://github.com/rosickey/pingpang/blob/master/images/pip.png)

4.继续输入
```bash
    pip install simpleguitk
```
![avatar](https://github.com/rosickey/pingpang/blob/master/images/simpleguitk.png)


### OSX\Linux操作系统

:warning: OSX\Linu已经安装有Python环境

1.打开命令行bash，输入
```bash
	pip install --upgrade pip
	pip install simpleguitk
```

## *快速开始*

### Windows

下载源代码ball.py, 假如存放在电脑c:\ball.py

打开系统命令行（开始-运行-输入CMD），输入
```bash
     python c:\ball.py
```
![avatar](https://github.com/rosickey/pingpang/blob/master/images/run.png)

修改源代码，可右键点击ball.py,使用IDLE打开编辑，也可使用其他代码编辑器

### OSX\Linux

假如源代码ball.py 存放在/Users/home，打开命令行，输入
```bash
     python /Users/home/ball.py
```
