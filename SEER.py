import cv2, time, dlib
import numpy as np
import serial
from gaze_tracking import GazeTracking

ardu = serial.Serial('COM5',115200)

cap = cv2.VideoCapture(0)
gaze = GazeTracking()

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

pts = []
rebt, rebv, heye, reye, leye, lebt, lebv, jaw, veye = '060','60','060','060','060','060','60','060','120'


while(1):

    _, image = cap.read()

    faces = detector(image)

    gaze.refresh(image)
    frame = gaze.annotated_frame()
    
    for face in faces:

        landmarks = predictor(image, face)
 
        for n in range(0, 68):
            
            x = landmarks.part(n).x
            y = landmarks.part(n).y

            pts.append([x,y])

            cv2.circle(image, (x, y), 1, (0, 255, 0), 1)
    
# ------------------------------
    
#right eye
    if len(pts) != 68:
        pass
    else:
        if (pts[41][1] - pts[37][1]) <=6:
            reye = '130'
        elif (pts[46][1] - pts[37][1]) <=8 and (pts[46][1] - pts[37][1]) >=6:
            reye = '125'
        elif (pts[41][1] - pts[37][1]) <=10 and (pts[46][1] - pts[37][1]) >=8:
            reye = '113'
        elif (pts[41][1] - pts[37][1]) <=12 and (pts[46][1] - pts[37][1]) >=10:
            reye = '101'
        elif (pts[41][1] - pts[37][1]) <=16 and (pts[46][1] - pts[37][1]) >=14:
            reye = '089'
        elif (pts[41][1] - pts[37][1]) <=18 and (pts[46][1] - pts[37][1]) >=16:
            reye = '077'
        elif (pts[41][1] - pts[37][1]) <=19 and (pts[46][1] - pts[37][1]) >=18:
            reye = '065'
        elif (pts[41][1] - pts[37][1]) <=20 and (pts[46][1] - pts[37][1]) >=19:
            reye = '052'
        elif (pts[41][1] - pts[37][1]) >=20:
            reye = '040'

#left eye
    if len(pts) != 68:
        pass
    else:
        if (pts[46][1] - pts[44][1]) <=13:
            leye = '030'
        elif (pts[46][1] - pts[44][1]) <=14 and (pts[46][1] - pts[44][1]) >=13:
            leye = '041'
        elif (pts[46][1] - pts[44][1]) <=15 and (pts[46][1] - pts[44][1]) >=14:
            leye = '052'
        elif (pts[46][1] - pts[44][1]) <=16 and (pts[46][1] - pts[44][1]) >=15:
            leye = '063'
        elif (pts[46][1] - pts[44][1]) <=17 and (pts[46][1] - pts[44][1]) >=16:
            leye = '074'
        elif (pts[46][1] - pts[44][1]) <=18 and (pts[46][1] - pts[44][1]) >=17:
            leye = '085'
        elif (pts[46][1] - pts[44][1]) <=19 and (pts[46][1] - pts[44][1]) >=18:
            leye = '096'
        elif (pts[46][1] - pts[44][1]) <=20 and (pts[46][1] - pts[44][1]) >=19:
            leye = '107'
        elif (pts[46][1] - pts[44][1]) >=20:
            leye = '110'
    
#eyesight_ver
    if type(gaze.vertical_ratio()) == float :
        if gaze.vertical_ratio() >= 0.9 :
            veye = '100'
        elif gaze.vertical_ratio() >= 0.8 and gaze.vertical_ratio() < 0.9:
            veye = '108'
        elif gaze.vertical_ratio() >= 0.7 and gaze.vertical_ratio() < 0.8:
            veye = '115'
        elif gaze.vertical_ratio() >= 0.6 and gaze.vertical_ratio() < 0.7:
            veye = '122'
        elif gaze.vertical_ratio() >= 0.5 and gaze.vertical_ratio() < 0.6:
            veye = '129'
        elif gaze.vertical_ratio() >= 0.4 and gaze.vertical_ratio() < 0.5:
            veye = '136'
        elif gaze.vertical_ratio() >= 0.3 and gaze.vertical_ratio() < 0.4:
            veye = '143'
        elif gaze.vertical_ratio() < 0.3 :
            veye = '150'
        else :
            pass

#eyesight_hor
    if type(gaze.vertical_ratio()) == float :
        if gaze.horizontal_ratio() >= 0.9 :
            heye = '180'
        elif gaze.horizontal_ratio() >= 0.8 and gaze.horizontal_ratio() < 0.9:
            heye = '160'
        elif gaze.horizontal_ratio() >= 0.7 and gaze.horizontal_ratio() < 0.8:
            heye = '140'
        elif gaze.horizontal_ratio() >= 0.6 and gaze.horizontal_ratio() < 0.7:
            heye = '120'
        elif gaze.horizontal_ratio() >= 0.5 and gaze.horizontal_ratio() < 0.6:
            heye = '100'
        elif gaze.horizontal_ratio() >= 0.4 and gaze.horizontal_ratio() < 0.5:
            heye = '080'
        elif gaze.horizontal_ratio() >= 0.3 and gaze.horizontal_ratio() < 0.4:
            heye = '060'
        elif gaze.horizontal_ratio() >= 0.2 and gaze.horizontal_ratio() < 0.3:
            heye = '040'
        elif gaze.horizontal_ratio() >= 0.1 and gaze.horizontal_ratio() < 0.2:
            heye = '020'
        elif gaze.horizontal_ratio() < 0.1:
            heye = '000'
        else :
            pass
    
#jaw
    if len(pts) != 68:
        pass
    else:
        if (pts[66][1] - pts[62][1]) <= 10:
            jaw = '110'
        elif (pts[66][1] - pts[62][1]) <= 20 and (pts[66][1] - pts[62][1]) > 10 :
            jaw = '090'
        elif (pts[66][1] - pts[62][1]) <= 30 and (pts[66][1] - pts[62][1]) > 20 :
            jaw = '083'
        elif (pts[66][1] - pts[62][1]) <= 40 and (pts[66][1] - pts[62][1]) > 30 :
            jaw = '076'
        elif (pts[66][1] - pts[62][1]) <= 50 and (pts[66][1] - pts[62][1]) > 40 :
            jaw = '069'
        elif (pts[66][1] - pts[62][1]) <= 60 and (pts[66][1] - pts[62][1]) > 50 :
            jaw = '062'
        elif (pts[66][1] - pts[62][1]) > 60 :
            jaw = '050'

#right eyebrow turn
    if len(pts) != 68:
        pass
    else:
        if (pts[27][1] - pts[19][1]) == 49:
            rebt = '000'
        elif (pts[27][1] - pts[19][1]) == 50:
            rebt = '010'
        elif (pts[27][1] - pts[19][1]) == 51:
            rebt = '020'
        elif (pts[27][1] - pts[19][1]) == 52:
            rebt = '030'
        elif (pts[27][1] - pts[19][1]) == 53:
            rebt = '040'
        elif (pts[27][1] - pts[19][1]) == 54:
            rebt = '050'
        elif (pts[27][1] - pts[19][1]) == 55:
            rebt = '060'
        elif (pts[27][1] - pts[19][1]) == 56:
            rebt = '070'
        elif (pts[27][1] - pts[19][1]) == 57:
            rebt = '080'
        elif (pts[27][1] - pts[19][1]) == 58:
            rebt = '090'
        elif (pts[27][1] - pts[19][1]) == 59:
            rebt = '100'
        elif (pts[27][1] - pts[19][1]) == 60:
            rebt = '110'
        elif (pts[27][1] - pts[19][1]) == 61:
            rebt = '120' 
        elif (pts[27][1] - pts[19][1]) == 62:
            rebt = '130'
        elif (pts[27][1] - pts[19][1]) == 63:
            rebt = '140' 
        elif (pts[27][1] - pts[19][1]) == 64:
            rebt = '150' 
        elif (pts[27][1] - pts[19][1]) == 65:
            rebt = '160' 
        elif (pts[27][1] - pts[19][1]) == 66:
            rebt = '170'
        elif (pts[27][1] - pts[19][1]) >  67:
            rebt = '180'

#right eyebrow vertical
    if len(pts) != 68:
        pass
    else:
        if (pts[27][1] - pts[21][1]) <= 31:
            rebv = '060'
        elif (pts[27][1] - pts[21][1]) <= 33 and (pts[27][1] - pts[21][1]) > 31 :
            rebv = '065'
        elif (pts[27][1] - pts[21][1]) <= 35 and (pts[27][1] - pts[21][1]) > 33 :
            rebv = '070'
        elif (pts[27][1] - pts[21][1]) <= 38 and (pts[27][1] - pts[21][1]) > 35 :
            rebv = '075'
        elif (pts[27][1] - pts[21][1]) <= 41 and (pts[27][1] - pts[21][1]) > 38 :
            rebv = '080'
        elif (pts[27][1] - pts[21][1]) <= 45 and (pts[27][1] - pts[21][1]) > 41 :
            rebv = '085'
        elif (pts[27][1] - pts[21][1]) > 45 :
            rebv = '090'

#left eyebrow turn
    if len(pts) != 68:
        pass
    else:
        if (pts[27][1] - pts[24][1]) == 49:
            lebt = '000'
        elif (pts[27][1] - pts[24][1]) == 50:
            lebt = '010'
        elif (pts[27][1] - pts[24][1]) == 51:
            lebt = '020'
        elif (pts[27][1] - pts[24][1]) == 52:
            lebt = '030'
        elif (pts[27][1] - pts[24][1]) == 53:
            lebt = '040'
        elif (pts[27][1] - pts[24][1]) == 54:
            lebt = '050'
        elif (pts[27][1] - pts[24][1]) == 55:
            lebt = '060'
        elif (pts[27][1] - pts[24][1]) == 56:
            lebt = '070'
        elif (pts[27][1] - pts[24][1]) == 57:
            lebt = '080'
        elif (pts[27][1] - pts[24][1]) == 58:
            lebt = '090'
        elif (pts[27][1] - pts[24][1]) == 59:
            lebt = '100'
        elif (pts[27][1] - pts[24][1]) == 60:
            lebt = '110'
        elif (pts[27][1] - pts[24][1]) == 61:
            lebt = '120' 
        elif (pts[27][1] - pts[24][1]) == 62:
            lebt = '130'
        elif (pts[27][1] - pts[24][1]) == 63:
            lebt = '140' 
        elif (pts[27][1] - pts[24][1]) == 64:
            lebt = '150' 
        elif (pts[27][1] - pts[24][1]) == 65:
            lebt = '160' 
        elif (pts[27][1] - pts[24][1]) == 66:
            lebt = '170'
        elif (pts[27][1] - pts[24][1]) >  67:
            lebt = '180'

#left eyebrow vertical
    if len(pts) != 68:
        pass
    else:
        if (pts[27][1] - pts[22][1]) <= 42:
            lebv = '080'
        elif (pts[27][1] - pts[22][1]) <= 44 and (pts[27][1] - pts[22][1]) > 42 :
            lebv = '075'
        elif (pts[27][1] - pts[22][1]) <= 47 and (pts[27][1] - pts[22][1]) > 44 :
            lebv = '070'
        elif (pts[27][1] - pts[22][1]) <= 50 and (pts[27][1] - pts[22][1]) > 47 :
            lebv = '065'
        elif (pts[27][1] - pts[22][1]) <= 54 and (pts[27][1] - pts[22][1]) > 50 :
            lebv = '060'
        elif (pts[27][1] - pts[22][1]) <= 58 and (pts[27][1] - pts[22][1]) > 54 :
            lebv = '055'
        elif (pts[27][1] - pts[22][1]) > 58 :
            lebv = '050'

#define
    rst = 'a' + rebt + ',' + rebv+ ',' + heye+ ',' + reye+ ',' + leye+ ',' + lebt+ ',' + lebv+ ',' + jaw+ ',' + veye + 'a'

    if len(pts) != 68 :
        pass
    else :
        pts.clear()
        rst = rst.encode('utf-8')
        #print(rst)
        #print(ardu.readline())
        ardu.write(rst)

    cv2.imshow('image', image)
    
    if cv2.waitKey(1) == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()
