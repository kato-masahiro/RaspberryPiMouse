#coding:utf-8

import commands
import pfoe

mouse = pfoe.Robot(sensor=4,choice=4) # 0:待機 1:前進 2:右旋回 3:左旋回

def getsensors():
    """
    センサ値を取得
    整数のリストを返す
    """
    sen_val = "[" + commands.getoutput("cat /dev/rtlightsensor0 | tr ' ' ',' " )+ "]"
    sen_val = eval(sen_val)
    return sen_val

def go_ahead():
    """
    前に壁が現れるまで前進
    """
    gain = 1.0
    commands.getoutput("echo 1 > /dev/rtmotoren0")
    while True:
        sen = getsensors()
        if sum(sen) <= 8000:
            commands.getoutput("echo 400 > /dev/rtmotor_raw_l0")
            commands.getoutput("echo 400 > /dev/rtmotor_raw_r0")
        elif sum(sen) > 8000:
            commands.getoutput("echo 0 > /dev/rtmotor_raw_l0")
            commands.getoutput("echo 0 > /dev/rtmotor_raw_r0")
            commands.getoutput("echo 0 > /dev/rtmotoren0")
            break

def turn_right():
    """
    90度右旋回して停止
    """
    commands.getoutput("echo 1 > /dev/rtmotoren0")
    commands.getoutput("echo 200 > /dev/rtmotor_raw_l0")
    commands.getoutput("echo -200 > /dev/rtmotor_raw_r0")
    commands.getoutput("sleep 1.3")
    commands.getoutput("echo 0 > /dev/rtmotor_raw_l0")
    commands.getoutput("echo 0 > /dev/rtmotor_raw_r0")
    commands.getoutput("echo 0 > /dev/rtmotoren0")

def turn_left():
    """
    90度右旋回して停止
    """
    commands.getoutput("echo 1 > /dev/rtmotoren0")
    commands.getoutput("echo -200 > /dev/rtmotor_raw_l0")
    commands.getoutput("echo 200 > /dev/rtmotor_raw_r0")
    commands.getoutput("sleep 1.3")
    commands.getoutput("echo 0 > /dev/rtmotor_raw_l0")
    commands.getoutput("echo 0 > /dev/rtmotor_raw_r0")
    commands.getoutput("echo 0 > /dev/rtmotoren0")

def get_switch():
    """
    スイッチが押されるのを待つ
    押されたら何番の州一致が押されたかを返す
    """

def load_files():
    """
    ファイル存在している場合に読み込む
    """
def write_result():
    """
    今回の試行結果を書き込む
    """

if __name__ == '__main__':
    load_files()

    go_ahead()
    commands.getoutput("sleep 0.5")
    turn_left()
    commands.getoutput("sleep 0.5")
    go_ahead()
