filetypes = ['*.ras', '*.xwd', '*.bmp', '*.jpe', '*.jpg', '*.jpeg',
             '*.xpm', '*.ief', '*.pbm', '*.tif', '*.gif', '*.ppm',
             '*.xbm', '*.tiff', '*.rgb', '*.pgm', '*.png', '*.pnm']


def location_correct(location):
    fl = False
    for i in filetypes:
        print(location[-(len(i)-1):])
        if location[-(len(i)-1):] == i[1::]:
            fl = True
    return fl


print(location_correct('main.jpeg'))