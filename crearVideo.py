import cv2
import os

path = 'Images/'

images = []

for file in os.listdir(path):
    name, extend = os.path.splitext(file)

    if extend in ['.jpg', '.jpeg', '.png', '.gif', '.jfif']:
        file_name = path + file
        images.append(file_name)

count = len(images)

frame = cv2.imread(images[0])
height, width, channels = frame.shape
sizes = (width,height)

out = cv2.VideoWriter('project.mp4',cv2.VideoWriter_fourcc(*'DIVX'), 5, sizes)

for i in range(0, count-1):
    frame = cv2.imread(images[i])
    out.write(frame)

out.release()
print('Terminamos')
