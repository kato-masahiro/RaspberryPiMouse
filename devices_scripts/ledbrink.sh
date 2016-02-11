#!/bin/bash
#coding:utf-8

while :
do
    echo 1 > /dev/rtled0 # 一番右
    echo 1 > /dev/rtled1
    echo 1 > /dev/rtled2
    echo 1 > /dev/rtled3

    sleep 1

    echo 0 > /dev/rtled0
    echo 0 > /dev/rtled1
    echo 0 > /dev/rtled2
    echo 0 > /dev/rtled3

    sleep 1
done 
