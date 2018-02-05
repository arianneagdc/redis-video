import numpy as np
import cv2
import time
import simplejson as json
import redis
import sys
#import json
import pickle

r=redis.Redis(host='35.194.148.35', port=6379, db=0)
abs1=r.get('fam')
frameString1= pickle.loads(abs1)
mat1=np.array(frameString1)
mat1=np.uint8(mat1)
fh,fw,xa=mat1.shape
print(mat1)
out = cv2.VideoWriter('outpy1.avi',cv2.VideoWriter_fourcc('M','P','4','2'), 10, (fw,fh))

count=0
while(True):
    time1=time.clock()
    #frameString=pickle.loads(r.get('red_frame_%d' %count))
    frameString=pickle.loads(r.lpop('red_frame'))
    print(type(frameString))
    time1e=time.clock()
   
    time2=time.clock()
    mat=np.array(frameString)
    time2e=time.clock()
   
    time3=time.clock()
    mat=np.uint8(mat)
    time3e=time.clock()
    
    count=count+1
    print((frameString))
    print("time for pickle: ", time1e-time1)
    print("time for np array conv: ", time2e-time2 )
    print("time for uint8 conv: ", time3e-time3)
    print("time for 1 frame: ", time3e-time1)
    out.write(mat)  
    cv2.imshow('frame',mat)

    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cv2.waitKey(0)
cv2.destroyAllWindows() 


