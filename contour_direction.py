from PIL import Image
import numpy as np
# import matplotlib.pyplot as plt
import glob
import time 
import os
contour_directions_feature = np.zeros((400,12))
t=0
for filename in glob.glob(os.path.join('Testing input/', '*.jpg')):
	im = Image.open(filename)
	gs = im.convert('L')
	bw = np.array(gs)
	bw[bw<230] = 0
	bw[bw>=230] = 255
	count = np.zeros(12)
	# window size = 5x5
	for i in range(5,bw.shape[0]-5):
		for j in range(5,bw.shape[1]-5):
			if((not bw[i][j]) and (bw[i][j-1]) and (not bw[i][j+1])): #left edge	
				check=0		
				l= j-5
				for k in range(i,i-6,-1):
					if(not bw[k][l]):
						check=1
						break
				if(check):
					if(k==i):
						if(l>j):
							theta= np.pi/2
						else:
							theta = -np.pi/2
					else:
						theta = np.arctan(float(l-j)/float(k-i))
					if(theta<0):
						theta += np.pi
					theta *= (180)/np.pi
					if(theta!=0.0 and theta!=-0.0):
						count[int(theta)/15]+=1
					continue
				k=i-5
				for l in range(j-5,j+6):
					 if(not bw[k][l]):
						check=1
						break
				if(check):
					if(k==i):
						if(l>j):
							theta= np.pi/2
						else:
							theta = -np.pi/2
					else:
						theta = np.arctan(float(l-j)/float(k-i))
					if(theta<0):
						theta += np.pi
					theta *= (180)/np.pi
					if(theta!=0.0 and theta!=-0.0):
						count[int(theta)/15]+=1
					continue
				l=j+5
				for k in range(i-5,i+1):
					if(not bw[k][l]):
						check=1
						break
				if(check):
					if(k==i):
						if(l>j):
							theta= np.pi/2
						else:
							theta = -np.pi/2
					else:
						theta = np.arctan(float(l-j)/float(k-i))
					if(theta<0):
						theta += np.pi
					theta *= (180)/np.pi
					if(theta!=0.0 and theta!=-0.0):
						count[int(theta)/15]+=1
					continue
					
			elif((not bw[i][j]) and (bw[i][j+1]) and (not bw[i][j-1])): #right edge
				check= 0
				l=j+5
				for k in range(i,i-6,-1):
					if(not bw[k][l]):
						check=1
						break
				if(check):	
					if(k==i):
						if(l>j):
							theta= np.pi/2
						else:
							theta = -np.pi/2
					else:
						theta = np.arctan(float(l-j)/float(k-i))
					if(theta<0):
						theta += np.pi				
					theta *= (180)/np.pi
					if(theta!=0.0 and theta!=-0.0):
						count[int(theta)/15]+=1
					continue
				k=i-5
				for l in range(j+5,j-6,-1):
					if(not bw[k][l]):
						check=1
						break
				if(check):
					if(k==i):
						if(l>j):
							theta= np.pi/2
						else:
							theta = -np.pi/2
					else:
						theta = np.arctan(float(l-j)/float(k-i))
					if(theta<0):
						theta += np.pi
					theta *= (180)/np.pi
					if(theta!=0.0 and theta!=-0.0):
						count[int(theta)/15]+=1
					continue
				l=j-5
				for k in range(i-5,i+1):
					if(not bw[k][l]):
						check=1
						break
				if(check):
					if(k==i):
						if(l>j):
							theta= np.pi/2
						else:
							theta = -np.pi/2
					else:
						theta = np.arctan(float(l-j)/float(k-i))
					if(theta<0):
						theta += np.pi
					theta *= (180)/np.pi
					if(theta!=0.0 and theta!=-0.0):
						count[int(theta)/15]+=1
					continue
	contour_directions_feature[t] = count
	t+=1
	print t
np.save('contour_directions_feature_test.npy',contour_directions_feature)