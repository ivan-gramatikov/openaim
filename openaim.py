import cv2
#cv2.namedWindow("preview")

import gtk.gdk
import numpy as np
import matplotlib.pyplot as plt
import pyautogui as vui

CASCADE_ITEM = "FACE"
faceCascade = cv2.CascadeClassifier("haar.xml")
w = gtk.gdk.get_default_root_window()
sz = w.get_size()
pb = gtk.gdk.Pixbuf(gtk.gdk.COLORSPACE_RGB,False,8,sz[0],sz[1])
pb = pb.get_from_drawable(w,w.get_colormap(),0,0,0,0,sz[0],sz[1])
nx = pb.get_pixels_array()
nx.dtype = np.uint8
color = cv2.cvtColor(nx, cv2.COLOR_RGB2BGR)
gray = cv2.cvtColor(color, cv2.COLOR_BGR2GRAY)
rectangles = faceCascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=10,
			minSize=(75, 75))

for (i, (x, y, w, h)) in enumerate(rectangles):
	# Surround cascade with rectangle
	cv2.rectangle(color, (x, y), (x + w, y + h), (0, 0, 255), 2)
	cv2.putText(color, CASCADE_ITEM + " #{}".format(i + 1), (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.55, (0, 0, 255), 2)
        vui.moveTo(x+120, y+50)


#cv2.startWindowThread()
#cv2.imshow('preview', color)
#cv2.waitKey(5000)

#cv2.destroyAllWindows()

























#mat1 = np.arange(nx, dtype ='uint8')
#print type(mat1)

#yb = np.array(nx)
#cv2.imwrite("face-"+ ".jpg", color)

#cv2.imshow('test', nx)
#cv2.imwrite("face-"+ ".jpg", color)
#cv2.waitKey(5000)
#cv2.imshow('test', gray)
#yb = np.array(nx)
#yk = yb.astype(uint8)
#cv2.imshow('test', mat)
#cv2.waitKey(5000)
