from nis import match
import cv2
import cvzone
import time
import numpy as np
from test_camera import * 
from extract import * 
from face_detector import * 
from getcolor import *
def moy_rectangle(img,m1,m2):
	#renvoie la couleur moyenne d'un rectangle entre les cordonnées m1,m2
	case=[]
	for a in range (m1[1],m2[1]):
		casex=[]
		for b in range (m1[0],m2[0]):
			casex.append(img[a][b])	
		case.append(casex)
	return getcolor(case)
