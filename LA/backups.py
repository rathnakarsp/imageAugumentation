# img minishandmaxish
def imgMerge(path, nx, ny):
    img = cv2.imread('00.jpg')
    files = os.listdir(path)
    if float(nx) < 1.0 and float(ny) < 1.0:
        for file in files:
            img1 = cv2.imread('%s\\%s\\%s.jpg' % (path, file, file))
            width = int(948*nx)
            height = int(700*ny)
            x = int((948 - width)/2)
            y = int((700 - height)/2)
            rect = (x, y, width, height)  # x, y, width, height
            out = DataAugument.Merge(img, img1, rect)
            cv2.imwrite('%s\\%s\\%s_%s_%s.jpg' % (path, file, file, nx, ny), out)
    else:
        for file in files:
            img = cv2.imread('%s\\%s\\%s.jpg' % (path, file, file))
            width = int(948*nx)
            height = int(700*ny)
            out = cv2.resize(img, (width, height), interpolation=cv2.INTER_NEAREST)
            cv2.imwrite('%s\\%s\\%s_%d_%d.jpg' % (path, file, file, width, height), out)


