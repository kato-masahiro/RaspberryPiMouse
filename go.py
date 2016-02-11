#coding:utf-8

import random
import commands
import os.path
import pfoe

def get_sensors():
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
        sen = get_sensors()
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
    commands.getoutput("sleep 1.0")
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
    commands.getoutput("sleep 1.0")
    commands.getoutput("echo 0 > /dev/rtmotor_raw_l0")
    commands.getoutput("echo 0 > /dev/rtmotor_raw_r0")
    commands.getoutput("echo 0 > /dev/rtmotoren0")

def get_switch():
    """
    スイッチが押されるのを待つ
    押されたら何番のスイッチが押されたかを返す
    """
    commands.getoutput("echo 400 > /dev/rtbuzzer0")
    commands.getoutput("sleep 0.5")
    commands.getoutput("echo 0 > /dev/rtbuzzer0")
    while True:
        sw1 = commands.getoutput("cat /dev/rtswitch2")
        sw2 = commands.getoutput("cat /dev/rtswitch1")
        sw3 = commands.getoutput("cat /dev/rtswitch0")
        if sw1 == "0":
            return 1
        elif sw2 == "0":
            return 2
        elif sw3 == "0":
            return 3

if __name__ == '__main__':
    mouse = pfoe.Robot(sensor=4,choice=4) # 0:待機 1:前進 2:右旋回 3:左旋回
    mouse.read() #ファイルを読み込み

    for i in range(50):
        print i+1,"番目のチャレンジ"

        get_switch()

        #最初の前進
        sensor=get_sensors()
        mouse.decision_making(sensor)
        mouse.action = 1
        go_ahead()
        commands.getoutput("sleep 0.5")
        mouse.set_reward(0.0)

        #交差点での意思決定
        sensor=get_sensors()
        mouse.decision_making(sensor)
        if mouse.action == 0 or mouse.action == 1:
            mouse.action = random.randint(2,3)
        if mouse.action == 2:
            turn_right()
        elif mouse.action == 3:
            turn_left()
        commands.getoutput("sleep 0.5")
        mouse.set_reward(0.0)

        #最後の前進
        sensor=get_sensors()
        mouse.decision_making(sensor)
        mouse.action = 1
        go_ahead()
        commands.getoutput("sleep0.5")
        mouse.set_reward(0.0)

        #停止・報酬を与える
        sensor=get_sensors()
        mouse.decision_making(sensor)
        mouse.action = 0
        s = get_switch()
        if s == 1: #成功
            mouse.set_reward(1.0)
            commands.getoutput("echo OK >> log")
            print "OK"
        elif s == 2: #失敗
            commands.getoutput("echo NG >> log")
            mouse.set_reward(-1.0)
            print "NG"
        elif s == 3:
            exit(1)

        mouse.write()
