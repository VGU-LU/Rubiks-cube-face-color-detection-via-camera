from nis import match
import cv2
import cvzone
import time
import numpy as np
from test_camera import * 
from extract import * 
from face_detector import * 

# original = cv2.imread('test.jpg') 
# copy=original.copy()
# output=original.copy()
# overlay = cv2.imread('grille.png',cv2.IMREAD_UNCHANGED)


# cv2.rectangle(copy,(490,210),(582,302),(0, 255, 255),-1)
# cv2.rectangle(copy,(594,210),(686,302),(0, 255, 255),-1)
# cv2.rectangle(copy,(698,210),(790,302),(0, 255, 255),-1)

# cv2.rectangle(copy,(490,314),(582,406),(0, 255, 255),-1)
# cv2.rectangle(copy,(594,314),(686,406),(0, 255, 255),-1)
# cv2.rectangle(copy,(698,314),(790,406),(0, 255, 255),-1)

# cv2.rectangle(copy,(490,418),(582,510),(0, 255, 255),-1)
# cv2.rectangle(copy,(594,418),(686,510),(0, 255, 255),-1)
# cv2.rectangle(copy,(698,418),(790,510),(0, 255, 255),-1)


# cv2.addWeighted(copy,0.25,output,0.75,0,output)



# cv2.imshow('output',output)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


yellow=[0,255,255]
green=[0,255,0]
white=[255,255,255]
orangee=[0,127.5,255]
red=[0,0,255]
blue=[255,0,0]
def overlay(original,n):
	
	#equations pour généraliser l'overlay sur différents formats d'écran
	y=len(original)
	x=len(original[0])
	cy=int(y/2)
	cx=int(x/2)
	dc=70 #distance entre chaque centre
	lc=22 #demi longueur d'une case
	carre=int((0.5*y-2*12)/3)
	p1=((int(cx-1.5*carre-12),int(cy-1.5*carre-12)),(int(cx-0.5*carre-12),int(cy-0.5*carre-12)))
	p2=((int(cx-0.5*carre),int(cy-1.5*carre-12)),(int(cx+0.5*carre),int(cy-0.5*carre-12)))
	p3=((int(cx+0.5*carre+12),int(cy-1.5*carre-12)),(int(cx+1.5*carre+12),int(cy-0.5*carre-12)))
	p4=((int(cx-1.5*carre-12),int(cy-0.5*carre)),(int(cx-0.5*carre-12),int(cy+0.5*carre)))
	p5=((int(cx-0.5*carre),int(cy-0.5*carre)),(int(cx+0.5*carre),int(cy+0.5*carre)))
	p6=((int(cx+0.5*carre+12),int(cy-0.5*carre)),(int(cx+1.5*carre+12),int(cy+0.5*carre)))
	p7=((int(cx-1.5*carre-12),int(cy+0.5*carre+12)),(int(cx-0.5*carre-12),int(cy+1.5*carre+12)))
	p8=((int(cx-0.5*carre),int(cy+0.5*carre+12)),(int(cx+0.5*carre),int(cy+1.5*carre+12)))
	p9=((int(cx+0.5*carre+12),int(cy+0.5*carre+12)),(int(cx+1.5*carre+12),int(cy+1.5*carre+12)))
	
	
	#carrés centrés sur différents points: c(i) est le centre de la case i
	c1=(cx-dc,cy-dc)
	c2=(cx,cy-dc)
	c3=(cx+dc,cy-dc)
	
	c4=(cx-dc,cy)
	c5=(cx,cy)
	c6=(cx+dc,cy)
	
	c7=(cx-dc,cy+dc)
	c8=(cx,cy+dc)
	c9=(cx+dc,cy+dc)
	
	z1=((c1[0]-lc,c1[1]-lc),(c1[0]+lc,c1[1]+lc))
	z2=((c2[0]-lc,c2[1]-lc),(c2[0]+lc,c2[1]+lc))
	z3=((c3[0]-lc,c3[1]-lc),(c3[0]+lc,c3[1]+lc))
	
	z4=((c4[0]-lc,c4[1]-lc),(c4[0]+lc,c4[1]+lc))
	z5=((c5[0]-lc,c5[1]-lc),(c5[0]+lc,c5[1]+lc))
	z6=((c6[0]-lc,c6[1]-lc),(c6[0]+lc,c6[1]+lc))
	
	z7=((c7[0]-lc,c7[1]-lc),(c7[0]+lc,c7[1]+lc))
	z8=((c8[0]-lc,c8[1]-lc),(c8[0]+lc,c8[1]+lc))
	z9=((c9[0]-lc,c9[1]-lc),(c9[0]+lc,c9[1]+lc))
	
	
	copy=original.copy()
	output=original.copy()	

	color1=quellecouleur(moy_rectangle(original,z1[0],z1[1]))
	color2=quellecouleur(moy_rectangle(original,z2[0],z2[1]))
	color3=quellecouleur(moy_rectangle(original,z3[0],z3[1]))
	
	color4=quellecouleur(moy_rectangle(original,z4[0],z4[1]))
	color5=quellecouleur(moy_rectangle(original,z5[0],z5[1]))
	color6=quellecouleur(moy_rectangle(original,z6[0],z6[1]))
	
	color7=quellecouleur(moy_rectangle(original,z7[0],z7[1]))
	color8=quellecouleur(moy_rectangle(original,z8[0],z8[1]))
	color9=quellecouleur(moy_rectangle(original,z9[0],z9[1]))

	cv2.rectangle(copy,z1[0],z1[1],color1,-1)
	cv2.rectangle(copy,z2[0],z2[1],color2,-1)
	cv2.rectangle(copy,z3[0],z3[1],color3,-1)
	
	cv2.rectangle(copy,z4[0],z4[1],color4,-1)
	cv2.rectangle(copy,z5[0],z5[1],color5,-1)
	cv2.rectangle(copy,z6[0],z6[1],color6,-1)
	
	cv2.rectangle(copy,z7[0],z7[1],color7,-1)
	cv2.rectangle(copy,z8[0],z8[1],color8,-1)
	cv2.rectangle(copy,z9[0],z9[1],color9,-1)

	cv2.addWeighted(copy,0.25,output,0.75,0,output)	
	
	if n==1 or n==5:
		original = cv2.arrowedLine(original, [cx,(1/3)*cy],[cx,(2/3)*cy],[0,0,255], 9, tipLength = 0.5) 
	if n==2 or n==3 or n==4:
		original = cv2.arrowedLine(original, [(1/3)*cx,cy],[(2/3)*cx,cy],[0,0,255], 9, tipLength = 0.5) 

	cv2.imshow('output',output)
	


