import os
import cv2
import DataAugument


_min_angel = 60	 # for img_rotation
_max_angel = 60		# for img_rotation
_min_scale = 1.0  # for img_rotation
_max_scale = 1.0  # for img_rotation
_fill_pixel = 255  # for img_shift and img_rotation


# creat files
def creat_files(path, goal_path):
    files = os.listdir(path)
    s = []                          # img code
    for file in files:
        file = file[:-4]
        s.append(file)
    for a in s:
        img = cv2.imread('D:\\test\\img\\%s.jpg' % a)
        os.mkdir('%s\\%s' % (goal_path, a))
        cv2.imwrite('%s\\%s\\%s.jpg' % (goal_path, a, a), img)


# img shift
def imgforshift(path, x_max_shift, y_max_shift, step_size):
    files = os.listdir(path)
    for file in files:
        img = cv2.imread('%s\\%s\\%s.jpg' % (path, file, file))
        for shift in range(-x_max_shift, x_max_shift, step_size):               # range[2] = 平移间隔
            for shift1 in range(-y_max_shift, y_max_shift, step_size):
                img2 = DataAugument.img_shift(img, shift, shift, shift1, shift1, 255)
                cv2.imwrite('%s\\%s\\%s_%d_%d.jpg' % (path, file, file, shift, shift1), img2)


# img rotation
def imgrotation(path, min_angle, max_angle, step_size):
    files = os.listdir(path)
    for file in files:
        img = cv2.imread('%s\\%s\\%s.jpg' % (path, file, file))
        for angle in range(min_angle, max_angle, step_size):
            img1, global_angle, Matrix = DataAugument.img_rotation(img, angle, angle, _min_scale, _max_scale,
                                                                   _fill_pixel)
            cv2.imwrite('%s\\%s\\%s_%d.jpg' % (path, file, file, angle), img1)


# img minishandmaxish
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


