#!/bin/bash
pkill -9 -f bot.py
pkillexitstatus=$?

if [ $pkillexitstatus -eq 0 ]; then
    echo "pkill: one or more processes killed"
elif [ $pkillexitstatus -eq 1]; then
    echo "pkill: no processes killed"
elif [ $pkillexitstatus -eq 2]; then
    echo "pkill: syntax error in the command line"
elif [ $pkillexitstatus -eq 3]; then
    echo "pkill: fatal error"
else
    echo "pkill: UNEXPECTED $pkillexitstatus"
fi