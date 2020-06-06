import cv2

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
output = cv2.VideoWriter('output.avi',fourcc,20.0,(640,480))
while (cap.isOpened()):
    ret , frame = cap.read()

    output.write(frame)
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    cap.get(cv2.CAP_PROP_FRAME_WIDTH) #obtiene el ancho del video  Width of the frames in the video stream
    cap.get(cv2.CAP_PROP_FRAME_HEIGHT)#obtiene el alto del video    Height of the frames in the video stream.
    cv2.imshow('frame',gray) #para que se muestre en color blanco y negro si se quiere ver normal quitar el gray y usar directamente el frame
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        pass
    pass
cap.release()
output.release()
cv2.destroyAllWindows()