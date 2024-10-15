# MIDI in Sky Python
一个简易光遇国际服PC端的乐器整活工具

## 注意事项
- 需要Python环境
- Python代码内部有写死琴键键位，使用时请注意自行修改
- 默认键位是我正在使用的 `1234567890-=←\
- 弹奏部分基于 pydirectinput，请先确认是否安装，如果没装，执行 `pip install pydirectinput`

## MIDI2KeyBoard
接收抓取MIDI设备输入，并自动转换为键盘
- MIDI部分基于 rtmidi，请先确认是否安装，如果没装，执行`pip install rtmidi`
- 默认MIDI设备为扫到的第一个设备
- 使用时直接执行py文件即可，如`python MIDI2KeyBoard.py`

