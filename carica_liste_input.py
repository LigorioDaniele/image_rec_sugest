import os
import face_recognition
def carica_liste_input(folder_riferimenti,known_face_encodings,known_face_names):
    for filename in os.listdir(folder_riferimenti):
        img_path=os.path.join(folder_riferimenti,filename)
        if img_path is not None:
            caricamento=face_recognition.load_image_file(img_path)
            codifica=face_recognition.face_encodings(caricamento)[0]
            known_face_encodings.append(codifica)
            known_face_names.append(filename.rsplit( ".", 1 )[ 0 ])