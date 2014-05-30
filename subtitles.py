#!/usr/bin/python

import sys
import logging
from random import randint
import re
import time

show_lines = 10


logging.basicConfig(level=logging.INFO)

if len(sys.argv)!= 3 :
   print "usage: subtitles.py <file_ru> <file_eng>"
   exit()

file_ru = open(sys.argv[1]);
file_en = open(sys.argv[2]);


r_size = 0;
for line in file_ru:
  r_size+=1

logging.debug("r_size=%s"%r_size)

offset = randint(1,r_size)

logging.debug("offset=%s"%offset)

i = 0
time_code_not_found = True
file_ru.seek(0)

for line in file_ru:
  if (i>=offset) & (i<offset+show_lines):
    print '%s'%(line.rstrip())
    if time_code_not_found:
        sObj = re.search( r'(\d+\:\d+\:\d+),', line, re.M|re.I)
        if sObj:
            logging.debug("time=%s"%sObj.group(1))
            time_code_not_found = False
            time_code_s = sObj.group(1)

  i+=1

time_code = time.strptime(time_code_s,"%H:%M:%S")

time_code_not_found = True
for line in file_en:
    if time_code_not_found:
        sObj = re.search( r'(\d+\:\d+\:\d+),', line, re.M|re.I)
        if sObj:
            time_code_s = sObj.group(1)
            time_code_en = time.strptime(time_code_s,"%H:%M:%S")
            if time_code == time_code_en:
               logging.debug(time_code)
               logging.debug(time_code_en)
               time_code_not_found = False
               wait = raw_input("Press ENTER for english...")
               print "==================================="
               print line
               for i in range(10):
                   print next(file_en).rstrip()

    




