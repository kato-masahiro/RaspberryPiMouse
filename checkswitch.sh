#!/bin/bash
#coding:utf-8

while :
do
    clear
    echo switch0 is ..
    cat /dev/rtswitch0
    echo switch1 is ..
    cat /dev/rtswitch1
    echo switch2 is ..
    cat /dev/rtswitch2
    sleep 0.1
done
