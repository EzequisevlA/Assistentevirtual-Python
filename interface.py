from time import sleep
import cv2
import pandas
import numpy
import openpyxl
from multiprocessing import Process
import omxp
#def janeladeinteracao(): 
#    cap = cv2.VideoCapture('video (4).mp4')  
#    while cap.isOpened():
#
#        ret, im =cap.read()
#        if ret == False:
#            break
#        cv2.imshow('imagem', im)
#        if cv2.waitKey(1) ==27:
#            break
#        sleep(1/30)
#janeladeinteracao()


#class video(object):
#    def __init__(self, path):
#        self.path = path
#    def play(self):
#        from os import startfile
#        startfile(self.path)
#class Movie_MP4(video):
#    type="MP4"
#movie = Movie_MP4(r"C:\\Users\\qui12\\.vscode\\estudos\\estudos\\treino\\ia\\video (4).mp4")
#movie.play()
omxplayer -o local --loop /home/pi/video.mp4 --orientation 270