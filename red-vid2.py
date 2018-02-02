import numpy as np
import cv2
import time
import simplejson as json
import redis
import sys

r=redis.Redis(host='130.211.248.50', port=6379, db=0)
abs1=r.get('fam')
frameString1= json.loads(abs1)
mat1=np.array(frameString1)
mat1=np.uint8(mat1)
fh,fw,xa=mat1.shape

out = cv2.VideoWriter('outpy1.avi',cv2.VideoWriter_fourcc('M','P','4','2'), 10, (fw,fh))



while(True):
    frameString=json.loads((r.lpop('red_frame')))
    mat=np.array(frameString)
    mat=np.uint8(mat)
    print((frameString))
    out.write(mat)  
    cv2.imshow('frame',mat)

    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cv2.waitKey(0)


