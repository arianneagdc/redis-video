import shutil
import tempfile
import time
import numpy as np
import cv2
import os, sys
import redis
import simplejson as json

r=redis.Redis(host='35.189.168.118',port=6379,db=0)

cap = cv2.VideoCapture('countdown.mp4')
if (cap.isOpened() == False): 
  print("Unable to read camera feed")
#frame_width = int(cap.get(3))
#frame_height = int(cap.get(4))
ret, frame = cap.read()
frame_height,frame_width,x = frame.shape
print(frame)
print(frame.shape)

out = cv2.VideoWriter('outpy.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 10, (frame_width,frame_height))
adc1=r.set('fam', json.dumps(frame.tolist()))
while(True):
  ret, frame = cap.read()
  if ret == True: 
    print(frame)
    lo=r.rpush('red_frame',*frame)
    print(type(lo))
    print(lo)
    out.write(frame)  
    cv2.imshow('frame',frame)
    print(frame.dtype)
    #f1=json.dumps(frame.tolist())

    if cv2.waitKey(1) & 0xFF == ord('q'):
      break
  else:
    break 