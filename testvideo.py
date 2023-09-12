from nis import match
import cv2
import cvzone
import time
import numpy as np
from test_camera import * 
from extract import * 
from face_detector import * 
import socket
import pickle
from flask import Flask
#utilisation de Flask pour créer un serveur et garder les valeurs de calibration des couleurs précédentes:
# app = Flask('rubiks_cube_calibration')

# try:
    # with open('counter.txt', 'r') as f:
        # blanc =int(f.read())
        # vert=int(f.read())
        # rouge=int(f.read())
        # orange=int(f.read())
        # bleu=int(f.read())
        # blanc=int(f.read())
        
# sys.exit()

#l'argument de videocapture est un entier choisissant le n° de périphérique utilise

numero=0
nface=0
Patron=[[],[],[],[],[],[]]
cap = cv2.VideoCapture(0)
ret, frame = cap.read()
mode=1
#equations pour généraliser l'overlay sur différents formats d'écran
y=len(frame)
x=len(frame[0])
cy=int(y/2)
cx=int(x/2)
dc=80 #distance entre chaque centre
lc=18 #demi longueur d'une case
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


while(True):
	ret, frame = cap.read()
	
		
	copy=frame.copy()
	output=frame.copy()	
	
	#detection de couleur premiere technique
		
	color1=quellecouleur(moy_rectangle(frame,z1[0],z1[1]))
	color2=quellecouleur(moy_rectangle(frame,z2[0],z2[1]))
	color3=quellecouleur(moy_rectangle(frame,z3[0],z3[1]))
	
	color4=quellecouleur(moy_rectangle(frame,z4[0],z4[1]))
	color5=quellecouleur(moy_rectangle(frame,z5[0],z5[1]))
	color6=quellecouleur(moy_rectangle(frame,z6[0],z6[1]))
	
	color7=quellecouleur(moy_rectangle(frame,z7[0],z7[1]))
	color8=quellecouleur(moy_rectangle(frame,z8[0],z8[1]))
	color9=quellecouleur(moy_rectangle(frame,z9[0],z9[1]))	
	
	#detection des couleurs nouvelle technique
	
	# color1=quellecouleurbis(moy_rectangle(frame,z1[0],z1[1]))
	# color2=quellecouleurbis(moy_rectangle(frame,z2[0],z2[1]))
	# color3=quellecouleurbis(moy_rectangle(frame,z3[0],z3[1]))
	
	# color4=quellecouleurbis(moy_rectangle(frame,z4[0],z4[1]))
	# color5=quellecouleurbis(moy_rectangle(frame,z5[0],z5[1]))
	# color6=quellecouleurbis(moy_rectangle(frame,z6[0],z6[1]))
	
	# color7=quellecouleurbis(moy_rectangle(frame,z7[0],z7[1]))
	# color8=quellecouleurbis(moy_rectangle(frame,z8[0],z8[1]))
	# color9=quellecouleurbis(moy_rectangle(frame,z9[0],z9[1]))	


	
#appuyer sur c pour changer de mode:
#mode impair: fonctionnement normal
#mode secondaire:calibration

	if cv2.waitKey(1)==ord('c'):
		mode=mode+1
		ncalibration=0
		print("mode numéro:")
		print(mode%2)
		numero=0

	
	if mode%2==1:
	
		cv2.rectangle(copy,z1[0],z1[1],color1,-1)
		cv2.rectangle(copy,z2[0],z2[1],color2,-1)
		cv2.rectangle(copy,z3[0],z3[1],color3,-1)
		
		cv2.rectangle(copy,z4[0],z4[1],color4,-1)
		cv2.rectangle(copy,z5[0],z5[1],color5,-1)
		cv2.rectangle(copy,z6[0],z6[1],color6,-1)
		
		cv2.rectangle(copy,z7[0],z7[1],color7,-1)
		cv2.rectangle(copy,z8[0],z8[1],color8,-1)
		cv2.rectangle(copy,z9[0],z9[1],color9,-1)
		# cv2.putText(output,'press c to change mode',(10,2*cy-90),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255), 2, cv2.LINE_AA)
		# cv2.putText(output,'press p to save colors',(10,2*cy-60),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255), 2, cv2.LINE_AA)
		# cv2.putText(output,'press q to exit',(10,2*cy-30),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255), 2, cv2.LINE_AA)
		# cv2.putText(output,'mode:main',(10,30),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255), 2, cv2.LINE_AA)
		cv2.addWeighted(copy,0.25,output,0.75,0,output)	
		output=cv2.flip(output,1)
		cv2.putText(output,'press c to change mode',(10,2*cy-90),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255), 2, cv2.LINE_AA)
		cv2.putText(output,'press p to save colors',(10,2*cy-60),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255), 2, cv2.LINE_AA)
		cv2.putText(output,'press q to exit',(10,2*cy-30),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255), 2, cv2.LINE_AA)
		cv2.putText(output,'mode:main',(10,30),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255), 2, cv2.LINE_AA)		
		
		if numero==1 :
			
			output = cv2.arrowedLine(output, [int(cx),int((1/3*cy))],[int(cx),int((4/3)*cy)],[0,0,255], 9, tipLength = 0.5) 
			cv2.imshow('output',output)

	
			# Attendre 2 secondes
			#time.sleep(2)
			numero=numero+1
			
		if numero==3 or numero==5 or numero==7 or numero==9:
			output = cv2.arrowedLine(output, [int((1/3)*cx),int(cy)],[int((4/3)*cx),int(cy)],[0,0,255], 9, tipLength = 0.5) 
			cv2.imshow('output',output)

	
			#time.sleep(2)
			numero=numero+1
			
		if numero==11 :
			output = cv2.arrowedLine(output, [int(cx),int((1/3*cy))],[int(cx),int((4/3)*cy)],[0,0,255], 9, tipLength = 0.5) 
			cv2.imshow('output',output)

			# Attendre 2 secondes
			#time.sleep(2)
			
			
		else:

			cv2.imshow('output',output)
		
	
	
		#taper sur 'p' pour faire une prendre les données de la face
		if cv2.waitKey(1)== ord('p'):
			numero=(numero+1)%10
			print(nface)
			Patron[nface].append(couleurstring(color1))
			Patron[nface].append(couleurstring(color2))
			Patron[nface].append(couleurstring(color3))
			
			Patron[nface].append(couleurstring(color4))
			# Patron[nface].append(couleurstring(color5))
			Patron[nface].append(stringpalette[nface])
			Patron[nface].append(couleurstring(color6))
			
			Patron[nface].append(couleurstring(color7))
			Patron[nface].append(couleurstring(color8))
			Patron[nface].append(couleurstring(color9))
			
			
			
			print(Patron[nface])
			print("la face n° %d a été prise" % (nface+1))
			
			if nface==5:
				if verify(Patron)==1:
					
						# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
							# s.bind(('10.0.2.15', 1234))
							# s.listen()
							# conn, addr = s.accept()
						# with conn:
							# data = pickle.dumps(Patron)
							# conn.sendall(data)
					result=[]
					for sublist in Patron:
						result.append("".join(sublist))
					
				
					print(result)

				if verify(Patron)==0:
	
					print('erreur: une face a été prise 2 fois/erreur de détection')
				Patron=[[],[],[],[],[],[]]
			nface=(nface+1)%6
			

		

#taper sur 'q' pour quitter l'interface
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
		
#taper sur c pour calibrer
	if mode%2==0:
		if ncalibration<6:

			cv2.rectangle(copy,(cx-20,cy-20),(cx+20,cy+20),paletteideale[ncalibration],-1)

			
			cv2.addWeighted(copy,0.25,output,0.75,0,output)	
			output=cv2.flip(output,1)
			cv2.putText(output,'mode:calibration',(10,30),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255), 2, cv2.LINE_AA)
			cv2.putText(output,stringpalette[ncalibration],(cx+100,cy-150),cv2.FONT_HERSHEY_SIMPLEX,1, paletteideale[ncalibration], 2, cv2.LINE_AA)
			cv2.putText(output,'color to calibrate:',(cx-200,cy-150),cv2.FONT_HERSHEY_SIMPLEX,1, paletteideale[ncalibration], 2, cv2.LINE_AA)
			cv2.imshow('output',output)



		if cv2.waitKey(1)==ord('*'):
			if ncalibration<6:
				print('color %s calibrated'% stringpalette[ncalibration])
				palette[ncalibration]=moy_rectangle(frame,(cx-20,cy-20),(cx+20,cy+20))
				print(palette[ncalibration])
			ncalibration+=1
			
			
		if ncalibration>=6:
			
			cv2.addWeighted(copy,0.25,output,0.75,0,output)	
			output=cv2.flip(output,1)
			cv2.putText(output,'Calibration done!',(cx-185,cy-200),cv2.FONT_HERSHEY_SIMPLEX,1, paletteideale[2], 2, cv2.LINE_AA)
			cv2.imshow('output',output)
			
			
		# if cv2.waitKey(1)==ord('o'):
			
			# if cv2.waitKey(1)==ord('d'):
				
			# if cv2.waitKey(1)==ord('c'):
			
# @app.route('/set_config', methods=['POST'])

# # récupération de la configuration depuis la requête POST
# config = request.json
# # mise à jour de la configuration dans l'application Flask
# app.config.update(config)

				
# with open('calibration.txt', 'w') as f:

		# f.write(f'{blanc}: {blanc}\n')
		# f.write(f'{bleu}: {bleu}\n')
		# f.write(f'{vert}: {vert}\n')
		# f.write(f'{jaune}: {jaune}\n')
		# f.write(f'{rouge}: {rouge}\n')
		# f.write(f'{orange}: {orange}\n')
		
		
		
	   

cap.release()
cv2.destroyAllWindows()
