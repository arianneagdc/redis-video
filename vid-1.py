import shutil
import tempfile
import time
import numpy as np
import cv2
import os, sys
import redis
import simplejson as json

r=redis.Redis(host='130.211.248.50',port=6379,db=0) #change depending on the ip address

#cap = cv2.VideoCapture('countdown.mp4')
cap = cv2.VideoCapture("rtsp://admin:@192.168.1.193/h264Preview_01_main")
if (cap.isOpened() == False): 
  print("Unable to read camera feed")
#frame_width = int(cap.get(3))
#frame_height = int(cap.get(4))
ret, frame = cap.read()
frame_height,frame_width,x = frame.shape
print(frame)
print(frame.shape)
count=0
out = cv2.VideoWriter('outpy.avi',cv2.VideoWriter_fourcc('M','P','4','2'), 10, (frame_width,frame_height))
adc1=r.set('fam', json.dumps(frame.tolist()))
while(True):
  ret, frame = cap.read()
  if ret == True: 
    print(frame)
    lo=r.lset('red_frame', count, json.dumps(frame.tolist()))
    print(type(lo))
    print(lo)
    out.write(frame)  
    cv2.imshow('frame',frame)
    print(frame.dtype)
    count=count+1
    #f1=json.dumps(frame.tolist())

    if cv2.waitKey(1) & 0xFF == ord('q'):
      break
  else:
    break 
