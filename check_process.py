#!/usr/bin/python3
# -*- coding: utf-8 -*-

import psutil
import re
import os
from datetime import datetime, timedelta

rows, columns = os.popen('stty size', 'r').read().split()
os.system('clear')
home_dir = os.environ["HOME"]

def memory_usage_psutil(pid):
    process = psutil.Process(pid)
    mem = process.memory_percent()
    return mem

try:
    print("{:=^100}".format("="))
    print("{:^90}".format("Process Status"))
    print("{:=^100}".format("="))
    file = open(home_dir + "/scripts/.Config", "r")
    for line in file:
        line = line.rstrip()
        pattern = '(.*' + line + '.*)'
        for proc in psutil.process_iter():
            cmdline = str(proc.cmdline())
            proc = str(proc)
            splited_proc = proc.split("=")
            pid = splited_proc[1]
            pid = pid.replace(', name', '')
            mem = (memory_usage_psutil(int(pid)))
            mem = round(mem, 2)
            started = splited_proc[3]
            started = started.replace('\'', '')
            started = started.replace(')', '')
            result = re.match(pattern, cmdline)
            if result:
                print("{:<29}".format("PROCESS: " + line) + "{:<15}".format("PID: " + pid) + "{:<20}".format("MEMORY % : " + str(mem)) + "{:<20}".format(" STARTED: " + started))
except IOError:
    print ("Error: The configuration file does not exist.")
    exit(0)
