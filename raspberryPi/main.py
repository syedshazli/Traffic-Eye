from FunctionLibrary import *
import cv2
import time
from predict_positions import predict_positions, create_lines
from alarm import overlap, soundAlarm
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(2, GPIO.OUT)


tracker=EuclideanDistTracker()
PTime=0
obj_det=cv2.createBackgroundSubtractorMOG2(history=100,varThreshold=100)

WebcamIsUsing=True
if WebcamIsUsing: 
    cap=cv2.VideoCapture(0)
else:
    cap=cv2.VideoCapture("crash.mp4")

positions = []
while True:
    _,img=cap.read()

    h,w,_,=img.shape
    print(f"{w = } {h = }")
    roi=img[0: 1080,0: 1900]
    mask=obj_det.apply(roi)
    _,mask=cv2.threshold(mask,254,255,cv2.THRESH_BINARY)
    cont,_=cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    det=[]
    for cnt in cont:
        area=cv2.contourArea(cnt)
        if area>300:
            #cv2.drawContours(roi,[cnt],-1,(0,255,0),2)
            x,y,w,h=cv2.boundingRect(cnt)
            det.append([x,y,w,h])
    
    CTime=time.time()
    fps=1/(CTime-PTime)
    PTime=CTime
    
    boxes_ids=tracker.update(det)
    positions.append(boxes_ids)
    for box in boxes_ids:
        print(1)
        x,y,w,h,id=box
        SpeedEstimatorTool=SpeedEstimator([x,y],fps)
        speed=SpeedEstimatorTool.estimateSpeed()

        if len(positions) >= 6:
            lines = create_lines(positions[-6], positions[-1])
            for line in lines:
                cv2.line(roi, line[0], line[1], (0, 255, 0), 5)
        
            for i in range(len(lines)):
                for j in range(len(lines)):
                    if i == j or not overlap(lines[i][0], lines[i][1], lines[j][0], lines[j][1]):
                        continue
                    GPIO.output(2, GPIO.HIGH)
                    time.sleep(1)
                    GPIO.output(2, GPIO.LOW)
                   


        # if len(positions) >= 10:
        #     pts = predict_positions(positions[-10], positions[-1])
        #     # print(pts)
        #     if pts is not None:
        #         # print(pts)
        #         for pt in pts:
        #             cv2.circle(roi, (pt[0],pt[1]), 5, (0, 255, 0), -1)


        cv2.putText(roi,str(id)+": "+str(speed)+"Km/h",(x,y-15),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),1)
        cv2.rectangle(roi,(x,y),(x+w,y+h),(0,0,255),3)


        
    

    #cv2.imshow("mask",mask)
    #cv2.imshow("roi",roi)
    #cv2.imshow("img",img)

    key=cv2.waitKey(30)
    if key==113: #113=Q
        break
