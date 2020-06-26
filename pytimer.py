#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
#  Copyright 2020 devv <devv@devv>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
import os, sys, time, tfont
def printUsage(): #Help screen
    print('Usage: pytimer.py [h](hours) [m](minutes) [s](seconds)\nExamples:\n'+
          'ts.py 1h30m30s\nts.py 10m30s\nts.py 45s')
    exit()
def cls(): #Clear console
    os.system('cls' if os.name=='nt' else 'clear')
def parseTime(args, DIGITS, line, sec): #Parsing args  
    for char in args:                   
        if char in DIGITS or char in 'hms':
            line += (char if char in DIGITS else char+',')
        else:
            printUsage()
    hms=line[:-1].split(',')
    try:                                #and getting seconds value from args
        for i in hms:
            if 'h' in i:
                sec+=int(str(i)[:-1])*3600
            elif 'm' in i:
                sec+=int(str(i)[:-1])*60
            elif 's' in i:
                sec+=int(str(i)[:-1])
            else:
                printUsage()
    except ValueError:
        printUsage()
    return(sec)
def getSplitTime(seconds): #Reformat seconds to h,m,s
    H=seconds//3600
    M=(seconds%3600)//60
    S=seconds-H*3600-M*60
    HMS=[H,M,S]
    return(HMS)
def DisplayTimer(HMS): #Drawing countdown
    row=0
    digits=(('0'+str(HMS[0]))[-2:]+':'+('0'+str(HMS[1]))[-2:]+':'+
            ('0'+str(HMS[2]))[-2:])
    print(' '*int((os.get_terminal_size().columns - 14) / 2)+'Ctrl+С to stop')
    print('\n' * int((os.get_terminal_size().lines - 6)/2))
    while row < 5:
        line=''
        column = 0
        while column < len(digits):
            digit = Digits[digits[column]]
            line = line + digit[row]+' '
            column += 1
        print(' '*int((os.get_terminal_size().columns - len(line)) / 2)+line)
        row += 1
#main
DIGITS = '0123456789'
Digits = tfont.DefaultFont
if len(sys.argv) != 2:
    printUsage()
args=sys.argv[1]
seconds = parseTime(args, DIGITS,'',0)
cls()
try: #countdown loop
    while seconds>0:
        HMS = getSplitTime(seconds)
        DisplayTimer(HMS)
        seconds-=1
        time.sleep(1)
        cls()
except KeyboardInterrupt:
    print('\n'+' '*int((os.get_terminal_size().columns - 17) / 2)+
          'Countdown stopped')
    exit()
