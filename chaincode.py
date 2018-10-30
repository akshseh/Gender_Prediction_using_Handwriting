from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
im = Image.open('0050_4.jpg')
gs = im.convert('L')
bw = np.array(gs)
bw[bw<230] = 0
bw[bw>=230] = 255
check = np.zeros((bw.shape[0],bw.shape[1]))
chain = []
for i in range(bw.shape[0]):
	for j in range(bw.shape[1]):
		if( (not bw[i][j]) and (not check[i][j])):
			check[i][j]=1
			current_i = i
			current_j = j
			loop = True
			while(loop):
				if((current_j<bw.shape[1]-1) and (not bw[current_i][current_j+1]) and (not check[current_i][current_j+1])):
					chain.append(3)
					check[current_i][current_j+1]=1
					current_i = current_i
					current_j = current_j+1
				elif((current_j<bw.shape[1]-1) and (current_i<bw.shape[0]-1) and (not bw[current_i+1][current_j+1]) and (not check[current_i+1][current_j+1])):
					chain.append(4)
					check[current_i+1][current_j+1]=1
					current_i = current_i+1
					current_j = current_j+1
				elif((current_i<bw.shape[0]-1) and (not bw[current_i+1][current_j]) and (not check[current_i+1][current_j])):
					chain.append(5)
					check[current_i+1][current_j]=1
					current_i = current_i+1
					current_j = current_j
				elif((current_j>0) and (current_i<bw.shape[0]-1) and (not bw[current_i+1][current_j-1]) and (not check[current_i+1][current_j-1])):
					chain.append(6)
					check[current_i+1][current_j-1]=1
					current_i = current_i+1
					current_j = current_j-1
				elif((current_j>0) and (not bw[current_i][current_j-1]) and (not check[current_i][current_j-1])):
					chain.append(7)
					check[current_i][current_j-1]=1
					current_i = current_i
					current_j = current_j-1
				elif((current_i>0) and (current_j>0) and (not bw[current_i-1][current_j-1]) and (not check[current_i-1][current_j-1])):
					chain.append(0)
					check[current_i-1][current_j-1]=1
					current_i = current_i-1
					current_j = current_j-1
				elif((current_i>0) and (not bw[current_i-1][current_j]) and (not check[current_i-1][current_j])):
					chain.append(1)
					check[current_i-1][current_j]=1
					current_i = current_i-1
					current_j = current_j
				elif((current_i>0) and (current_j<bw.shape[1]-1) and (not bw[current_i-1][current_j+1]) and (not check[current_i-1][current_j+1])):
					chain.append(2)
					check[current_i-1][current_j+1]=1
					current_i = current_i-1
					current_j = current_j+1
				else:
					loop = False
chain = np.array(chain)
np.save('0050_4.npy',chain)
chain = np.load('0050_4.npy')
count = np.zeros(8)
for i in range(chain.shape[0]):
	count[chain[i]]+=1
for i in range(count.shape[0]):
	count[i]/=chain.shape[0]
print count
plt.plot(np.arange(8),count)
plt.show()
count_ij = np.zeros(64)
for i in range(chain.shape[0]-1):
	count_ij[7*chain[i]+chain[i+1]]+=1
for i in range(count_ij.shape[0]):
	count_ij[i]/=(chain.shape[0]-1)
plt.plot(np.arange(64),count_ij)
plt.show()
# bwimg.save('0050_4_bw.jpg')