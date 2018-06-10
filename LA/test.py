import os,sys
import cv2
import creat

path = 'D:\\test\\img'              # img_path
goal_path = 'D:\\test\\1'           # files_path


L = [0.6, 0.8, 1, 1.2, 1.4]                     # for image zoom
s = [0.8, 0.9, 1.0, 1.1, 1.2]
creat.creat_files(path, goal_path)

creat.imgforshift(goal_path, 300, 150, 50)      # x_max:300 y_max:150

creat.imgrotation(goal_path, 0, 35, 5)          # angle_min: 0  angle_max :30

creat.imgrotation(goal_path, 330, 365, 5)       # angle_min: -30  angle_max :0

for i in L:
    creat.imgMerge(goal_path, i, i)             # img_zoom


for x in s:
    for y in s:
        creat.imgMerge(goal_path, x, y)



