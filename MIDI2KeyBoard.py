import rtmidi
import pydirectinput

midiin = rtmidi.MidiIn()

基准音高=5

键位 = [
     "`",
    "1",
     "2",
    "3",
    "4",
     "5",
    "6",
    "7",
     "8",
    "9",
    "0",
     "-",
     "=",
    "backspace",
     "\\",
]

    # 计算音阶信息
key_number_to_note = {
    0: 'C', 1: 'C#', 2: 'D', 3: 'D#', 4: 'E', 5: 'F',
    6: 'F#', 7: 'G', 8: 'G#', 9: 'A', 10: 'A#', 11: 'B'
}
白键映射 = {
    0: 0, 1: -1, 2: 1, 3:  -1, 4: 2,
    5: 3,6: -1, 7: 4, 8: -1, 9: 5, 10: -1, 11: 6,
    12: 7,13: -1,14: 8,15: -1,16: 9,
    17: 10,18: -1,19: 11,20: -1,21: 12,22: -1,23: 13,
    24: 14
}
当前零位=12*(基准音高+1)


pydirectinput.PAUSE = 0.00001
pydirectinput.FAILSAFE = False
def KeyName(note):
    return f"{key_number_to_note[note % 12]}{note // 12 - 1}"

import threading

def midi_callback(message):
    threading.Thread(target=KeyEvent, args=(message,)).start()
 
def KeyEvent(message):
    KeyNote=message[0][1]-当前零位

    if KeyNote>=0 and KeyNote <25 and 白键映射[KeyNote]>-1:
        if message[0][0]==148:
                print(f"按下琴键 {KeyName(message[0][1])}\n触发键位 {键位[白键映射[KeyNote]]}\n--------")
                pydirectinput.keyDown(键位[白键映射[KeyNote]])
        elif message[0][0]==132:
                print(f"抬起琴键 {KeyName(message[0][1])}\n释放键位 {键位[白键映射[KeyNote]]}\n--------")
                pydirectinput.keyUp(键位[白键映射[KeyNote]])

    # print("--------")


# 打印所有可用的MIDI输入端口
print("Available MIDI input ports/扫描可用设备:")
ports = range(midiin.get_port_count())
if ports:
    for i in ports:
        print(midiin.get_port_name(i))
    print("--------")
else:
    print("No MIDI input ports found. Exiting...")
    print("未能找到MIDI设备，退出程序...")
    exit()
# 选择第一个可用的MIDI输入端口
print("Attempting to set backend to rtmidi...")
print("尝试激活 rtmidi 监听")
midiin.open_port(0)
print(f"Listening / 开始监听 {midiin.get_port_name(0)}...")
print(f"current key StartAt:{KeyName(当前零位)}")
print(f"当前键盘零位:{KeyName(当前零位)}")
try:
    while True:
        m = midiin.get_message() # some timeout in ms
        if m:
            KeyEvent(m)
except KeyboardInterrupt:
    print("Exiting...")
    print("手动退出...")
