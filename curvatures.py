from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
im = Image.open('0050_4.jpg')
gs = im.convert('L')
bw = np.array(gs)
bw[bw<230] = 0
bw[bw>=230] = 255
convert = {}
indices = []
k=0
for i in range(-25,26):
	convert[i/25.0]=k
	indices.append(i/25.0)
	k+=1
indices = np.array(indices)
curves = []
for i in range(2,bw.shape[0]-2):
	for j in range(2,bw.shape[1]-2):
		if (not bw[i][j]):
			n1=0
			n2=0
			for k in range(i-2,i+3):
				for l in range(j-2,j+3):
					if(bw[k][l]):
						n1+=1
					else:
						n2+=1
			curves.append((n1-n2)/25.0)
count = np.zeros(indices.shape[0])
for i in curves:
	count[convert[i]]+=1
for i in range(count.shape[0]):
	count[i]/=len(curves)
plt.plot(indices,count)
plt.show()

