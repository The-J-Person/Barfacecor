import cv2

def detect_face(image):
    """Checks if the image contains exactly one face, returns True if it does.
    False will be returned if no face is found, or if multiple faces have been detected."""
    cascadePath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascadePath)
    faces = faceCascade.detectMultiScale(image)
    if len(faces)==0:
        return True
    return False
        

def take_picture(path):
    cascadePath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascadePath)
    video_capture = cv2.VideoCapture(0)
    ret, frame = video_capture.read()
    video_capture.release()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(path,frame)
    if detect_face(frame):
        cv2.imwrite(path,gray)
        return True
    return False

print(take_picture("./Database/subject16.png"))
