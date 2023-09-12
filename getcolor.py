from nis import match
import cv2
import cvzone
import time
import numpy as np
from test_camera import * 
from extract import * 
from face_detector import * 
from parse import parse
from parse import compile
#renvoie la couleur moyenne de l'image
def getcolor(image):
	schema=[]
	B=0
	G=0
	R=0
	for k in range (len(image[0])):
		for l in range(len(image)):
			#methode par moyennage
			B+=image[l][k][0]
			G+=image[l][k][1]
			R+=image[l][k][2]
	B=B/(len(image)*len(image[0]))
	G=G/(len(image)*len(image[0]))
	R=R/(len(image)*len(image[0]))
	schema.append(B)
	schema.append(G)
	schema.append(R)
	return(schema)
