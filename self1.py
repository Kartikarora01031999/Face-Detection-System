import cv2
import numpy
import argparse

ag=argparse.ArgumentParser()
ag.add_argument("-i","--image",required=True,help="path to the image")
ag.add_argument("-c","--confidence",type=float,default=0.5,help="minimum proboblity for detection")
args=vars(ag.parse_args())

print("[info] loading  model .....")
net=cv2.dnn.readNetFromCaffe("deploy.prototxt.txt","res10_300x300_ssd_iter_140000.caffemodel")
image=cv2.imread(args["image"])
(h,w)=image.shape[:2]
blob=cv2.dnn.blobFromImage(image,1.0,(300,300),(172,23,45))
#print(blob)
k=net.setInput(blob)
detections=net.forward()

print(detections.shape[2])