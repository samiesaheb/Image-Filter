import numpy as np

def pad(img, method='zero'):


  image = img.copy()
  padded = np.zeros((img.shape[0]+2,img.shape[1]+2))

  if method == 'zero':
    for i in range(1, padded.shape[0]-1):
      for k in range(1, padded.shape[1]-1):
        padded[i,k] = image[i-1,k-1]
          
  if method == 'replication':
    for i in range(len(padded)+1):
      if i == 0:
        padded[0,0] = image[0,0]
        padded[i,padded.shape[1]-1] = image[i,image.shape[1]-1]
        padded[padded.shape[0]-1,i] = image[image.shape[0]-1,i]
      if i == padded.shape[0]:
        padded[padded.shape[0]-1,padded.shape[1]-1] = image[image.shape[0]-1,image.shape[1]-1]
      for i in range(1, padded.shape[0]-1):
        
        padded[i,0] = image[i-1,0]
        padded[i,padded.shape[1]-1] = image[i-1,image.shape[1]-1]
        for k in range(1, padded.shape[1]-1):
          padded[0,k] = image[0,k-1]
          padded[i,k] = image[i-1,k-1]
          padded[padded.shape[0]-1,k] = padded[image.shape[0],k]
    
  return padded

def myImageFilter(image, filter):

  image = pad(image,method='replication')

  def rotate180(filter):
    length = len(filter)
    out = np.zeros(shape=(length,length))
    for i in range(length):
      for j in range(length):
        out[i, length-1-j] = filter[length-1-i, j]
    return out

  filter = rotate180(filter)

  filtered = np.zeros(shape=(image.shape[0]-2,image.shape[1]-2))

  for i in range(filtered.shape[0]):
      for j in range(filtered.shape[1]):
        leni = i+len(filter)
        lenj = j+len(filter)
        filtered[i,j] = np.sum(image[i:leni,j:lenj]*filter)
  return filtered