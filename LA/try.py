import os
import cv2
import random
import numpy as np
import DataAugument

goal_path = 'D:\\test\\11'


def imgMerge(path, nx, ny):
    img = cv2.imread('00.jpg')
    files = os.listdir(path)
    if float(nx) < 1.0:
        if float(ny) < 1.0:
            for file in files:
                img1 = cv2.imread('%s\\%s\\%s.jpg' % (path, file, file))
                width = int(948*nx)
                height = int(700*ny)
                x = int((948 - width)/2)
                y = int((700 - height)/2)
                rect = (x, y, width, height)  # x, y, width, height
                out0 = DataAugument.Merge(img, img1, rect)
                cv2.imwrite('%s\\%s\\%s_%s_%s.jpg' % (path, file, file, nx, ny), out0)
        else:
            for file in files:
                img1 = cv2.imread('%s\\%s\\%s.jpg' % (path, file, file))
                out1 = img1[170:530, 325:625]
                width = int(360*nx)
                height = int(300*ny)
                x = int((948 - width)/2)
                y = int((700 - height)/2)
                img3 = cv2.resize(out1, (width, height), interpolation=cv2.INTER_NEAREST)
                rect = (x, y, width, height)  # x, y, width, height
                out2 = DataAugument.Merge(img, img3, rect)
                cv2.imwrite('%s\\%s\\%s_%s_%s.jpg' % (path, file, file, nx, ny), out2)
    else:
        if ny > 1:
            for file in files:
                img1 = cv2.imread('%s\\%s\\%s.jpg' % (path, file, file))
                out1 = img1[170:530, 325:625]
                width = int(360*nx)
                height = int(300*ny)
                x = int((948 - width)/2)
                y = int((700 - height)/2)
                img3 = cv2.resize(out1, (width, height), interpolation=cv2.INTER_NEAREST)
                rect = (x, y, width, height)  # x, y, width, height
                out2 = DataAugument.Merge(img, img3, rect)
                cv2.imwrite('%s\\%s\\%s_%s_%s.jpg' % (path, file, file, nx, ny), out2)
        else:
            for file in files:
                img1 = cv2.imread('%s\\%s\\%s.jpg' % (path, file, file))
                out1 = img1[170:530, 325:625]
                width = int(360*nx)
                height = int(300*ny)
                x = int((948 - width)/2)
                y = int((700 - height)/2)
                img3 = cv2.resize(out1, (width, height), interpolation=cv2.INTER_NEAREST)
                rect = (x, y, width, height)  # x, y, width, height
                out2 = DataAugument.Merge(img, img3, rect)
                cv2.imwrite('%s\\%s\\%s_%s_%s.jpg' % (path, file, file, nx, ny), out2)


L = [0.6, 0.8, 1, 1.2, 1.4]
for i in L:
    for x in L:
        imgMerge(goal_path, i, x)

