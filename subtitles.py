#!/usr/bin/python

import sys
import logging
from random import randint
import re
import time

show_lines = 10


logging.basicConfig(level=logging.DEBUG)

if len(sys.argv)!= 3 :
   print "usage: subtitles.py <file_ru> <file_eng>"
   exit()

file_ru = open(sys.argv[1]);


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





