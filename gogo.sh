#!/bin/bash
#coding:utf-8
echo 1 > /dev/rtmotoren0 #通電

echo -200 > /dev/rtmotor_raw_l0
echo 200 > /dev/rtmotor_raw_r0
sleep 1

echo 200 > /dev/rtmotor_raw_l0
echo -200 > /dev/rtmotor_raw_r0
sleep 2

echo 400 > /dev/rtmotor_raw_l0
echo 400 > /dev/rtmotor_raw_r0
sleep 1

echo 0 > /dev/rtmotor_raw_l0
echo 0 > /dev/rtmotor_raw_r0

echo 0 > /dev/rtmotoren0
