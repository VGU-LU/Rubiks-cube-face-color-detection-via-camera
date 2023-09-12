from nis import match
import cv2
import cvzone
import time
import numpy as np
from test_camera import * 
from extract import * 
from face_detector import * 
tolerance=35

yellow=[0,255,255]
green=[0,255,0]
white=[255,255,255]
orangee=[0,127.5,255]
red=[0,0,255]
blue=[255,0,0]

jaune=[39.406666666666666, 175.75222222222223, 145.17444444444445]

vert=[50.69416666666667, 135.09027777777777, 13.4775]
blanc=[135.3488888888889, 122.89555555555556, 119.8488888888889]
orange=[18.603055555555557, 71.1825, 169.90305555555557]

rouge=[71.95916666666666, 31.00138888888889, 165.07805555555555]
bleu=[135.72861111111112, 79.62416666666667, 34.3875]

paletteideale=[white,green,orangee,blue,red,yellow]
palette=[blanc,vert,orange,bleu,rouge,jaune]
stringpalette=['W','V','O','B','R','Y']

#booleen si l'image a une couleur précise: comparateur par couleur moyenne
def iscolor(imgcolor):
	for i in range (len(palette)):
		compteur=0
		for j in range (3):
			if abs(imgcolor[j]-palette[i][j])<=tolerance:
				compteur+=1
		if compteur==3:
			return 1
	return 0
	
#renvoie la couleur de l'image correspondante à partir de la couleur moyenne

def quellecouleur(imgcolor):
	for i in range (len(palette)):
	
		compteur=0
		for j in range (3):
			if abs(imgcolor[j]-palette[i][j])<=tolerance:
				compteur+=1
		if compteur==3:
			return paletteideale[i]
		# if i ==5:
			# o=abs(imgcolor[2]-2*imgcolor[1]-palette[4][2]+2*palette[4][1])
			# r=abs(imgcolor[2]-2*imgcolor[1]-palette[5][2]+2*palette[5][1])
			# if r>o:
				# return paletteideale[i]
	return (0,0,0)
			
#renvoie le nom de la couleur de l'image correspondante à partir de la couleur moyenne
def quellecouleurstring(imgcolor):
	for i in range (len(palette)):
		compteur=0
		for j in range (3):
			if abs(imgcolor[j]-palette[i][j])<=tolerance:
				compteur+=1
		if compteur==3:
			return stringpalette[i]

def prise():
	face=[]
	face.append(quellecouleur(moy_rectangle(original,z1[0],z1[1])))
	face.append(quellecouleur(moy_rectangle(original,z2[0],z2[1])))
	face.append(quellecouleur(moy_rectangle(original,z3[0],z3[1])))
	face.append(quellecouleur(moy_rectangle(original,z4[0],z4[1])))
	face.append(quellecouleur(moy_rectangle(original,z5[0],z5[1])))
	face.append(quellecouleur(moy_rectangle(original,z6[0],z6[1])))
	face.append(quellecouleur(moy_rectangle(original,z7[0],z7[1])))
	face.append(quellecouleur(moy_rectangle(original,z8[0],z8[1])))
	face.append(quellecouleur(moy_rectangle(original,z9[0],z9[1])))
	return face

#renvoie en string la couleur idéale reçue en bgrq
def couleurstring(couleurideale):
	for i in range(len(paletteideale)):
		if paletteideale[i]==couleurideale:
			return stringpalette[i]


def quellecouleurbis(imgcolor):
	#jaune
	if imgcolor[1]>110 and imgcolor[2]>=110 and	imgcolor[0]<(1/2)*imgcolor[1]:
		return paletteideale[0]
	#vert
	if imgcolor[1]>1.6*imgcolor[0] and imgcolor[1]>1.6*imgcolor[2]:
		return paletteideale[1]
	#blanc	
	if imgcolor[0]>110 and imgcolor[1]>110 and imgcolor[0]>110:
		return paletteideale[2]
	if imgcolor[2]>1.6*imgcolor[0]:
		
		#orange
		if abs(imgcolor[2]-2*imgcolor[1])<25:
			return paletteideale[3]
		#rouge
		if imgcolor[2]>3*imgcolor[1]:
			return paletteideale[4]
	#bleu
	if imgcolor[0]>1.6*imgcolor[1] and imgcolor[0]>1.6*imgcolor[2]:
		return paletteideale[5]
	
# def quellecouleur(imgcolor):
	# for i in range (len(palette)):
		# compteur=0
		# if not (i==3 or i==4):
			
			# for j in range (3):
				# if abs(imgcolor[j]-palette[i][j])<=tolerance:
					# compteur+=1
		
			# if compteur==3:
				# return paletteideale[i]
		
		# if i== 3:
			# o=abs(palette[3][2]-2*palette[3][1])
			# r=abs(palette[4][2]-2*palette[4][1])
			# if o<r:
				# return paletteideale[3]
		# if i== 4:
			# o=abs(palette[3][2]-2*palette[3][1])
			# r=abs(palette[4][2]-2*palette[4][1])
			# if r>o:
				# return paletteideale[4]
	# return([255,255,255])
	
def verify(patron):
	liste=[0,0,0,0,0,0]

	for i in range(len(patron)):
		for j in range(len(patron[1])):
			if patron[i][j]=='blanc':
				liste[0]+=1
			if patron[i][j]=='vert':
				liste[1]+=1
			if patron[i][j]=='orange':
				liste[2]+=1
			if patron[i][j]=='bleu':
				liste[3]+=1
			if patron[i][j]=='rouge':
				liste[4]+=1
			if patron[i][j]=='jaune':
				liste[5]+=1
	for i in range(len(liste)):
		if liste[i]!=6:
			return 0
	return 1
			

