import face_recognition
import cv2
import numpy as np
import configparser
from carica_liste_input import *
from import_img import *
from mostra_suggeriti import *

config = configparser.ConfigParser()
config.readfp(open(r'config.txt'))
folder_riferimenti = config.get('Ambiente_test', 'folder_riferimenti')
folder_suggeriti = config.get('Ambiente_test', 'folder_suggeriti')
process_this_frame = config.get('Ambiente_test', 'process_this_frame')
known_face_encodings = [] #lista delle immagini di riferimento 
known_face_names = [] #lista dei nomi riferiti alle immagini di riferimento
face_locations = []
face_encodings = []
face_names = []

video_capture = cv2.VideoCapture(0,cv2.CAP_DSHOW)
carica_liste_input(folder_riferimenti,known_face_encodings,known_face_names)
while True:
    
    ret, frame = video_capture.read()

 # ridimensiona il del video di 1/4 per lavorare più velocemente
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    # Converte da colori BGR in RGB
    rgb_small_frame = small_frame[:, :, ::-1]
    if process_this_frame:
        # cerca i volti nel video
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
        face_names = []
        for face_encoding in face_encodings:
            # controlla se il volto corrisponde a qualcuno di quelli nella lista
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"
            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]
            face_names.append(name)
    process_this_frame = not process_this_frame
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        top *= 3
        right *= 5
        bottom *= 5
        left *= 3
        # Disegna un quadrato intorno alla faccia
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        # Inserisce del testo
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        fontColor= (255,255,255)
        lineType= 2
        fontScale=1
        bottomLeftCornerOfText =(10,50)
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
        mostra_suggeriti(name,folder_suggeriti)

    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
video_capture.release()
cv2.destroyAllWindows()