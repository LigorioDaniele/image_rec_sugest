import os
import cv2
from hconcat_resize import *

processati = ['primo']
def mostra_suggeriti(name,folder_suggeriti):
    suggeriti = []
    if name!= processati[-1]:
        for filename in os.listdir(folder_suggeriti+'\\'+name):
            img_path=os.path.join(folder_suggeriti+'\\'+name,filename)
            if img_path is not None:
                img_letta=cv2.imread(img_path)
                suggeriti.append(img_letta)
                img_h_resize = hconcat_resize(suggeriti)
             # salvo l'immagine finale con tutti i preferiti
             #cv2.imwrite('C:\\Users\\ga1danligori\\Pictures\\Camera Roll\\input\\hconcat_resize.jpg', img_h_resize) 
                cv2.imshow('image',img_h_resize)
                processati.append(name)
                print(processati)