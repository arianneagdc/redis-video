import shutil
import tempfile
import time
import numpy as np
import cv2
import os, sys
import redis
import json

r=redis.Redis(host='130.211.248.50',port=6379,db=0)

#cap = cv2.VideoCapture('countdown.mp4')
cap = cv2.VideoCapture("rtsp://admin:@192.168.1.193/h264Preview_01_main")
if (cap.isOpened() == False): 
  print("Unable to read camera feed")
#frame_width = int(cap.get(3))
#frame_height = int(cap.get(4))
ret, frame = cap.read()
time2=time.clock()
frame_height,frame_width,x = frame.shape
time2end=time.clock()
print("time 1: ", time2, time2end)
print(frame)
print(frame.shape)
count=0
out = cv2.VideoWriter('outpy.avi',cv2.VideoWriter_fourcc('M','P','4','2'), 10, (frame_width,frame_height))
adc1=r.set('fam', json.dumps(frame.tolist()))
while(True):
  tim3=time.clock()
  ret, frame = cap.read()
  if ret == True: 
    print(frame)
    tim1=time.clock()
    lo1= json.dumps(frame.tolist())
    tim1end=time.clock()

    time1p=time.clock()
    lo=r.lset('red_frame', count, lo1)
    time1pend=time.clock()
    
    cv2.imshow('frame',frame)
    print(frame.dtype)
    count=count+1
    print("time json: ", tim1, tim1end)
    print("time lset: ", time1p, time1pend)

    tim3end=time.clock()
    print("Total time per frame: ", tim3, tim3end)
    

    if cv2.waitKey(1) & 0xFF == ord('q'):
      break
  else:
    break 