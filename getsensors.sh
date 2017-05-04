#!/bin/bash
#coding:utf-8
while :
do
    clear
    echo sensors val is ...
    cat /dev/rtlightsensor0
    sleep 0.2
done
