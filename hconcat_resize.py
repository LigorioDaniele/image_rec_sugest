import cv2

def hconcat_resize(img_list, interpolation = cv2.INTER_CUBIC): 
    h_min = min(img.shape[0]  
                for img in img_list)   
    # ridimensionamento immagine 
    im_list_resize = [cv2.resize(img, (int(150), int(200)), interpolation = interpolation)
    for img in img_list] 
    # return dell'immagine finale
    return cv2.hconcat(im_list_resize) 