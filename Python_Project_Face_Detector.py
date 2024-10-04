# Importing the OpenCV library
import cv2 

# Loading the Haar Cascade Classifier for face detection
face_cap = cv2.CascadeClassifier("C:/Users/nitro/AppData/Local/Programs/Python/Python312/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml")

# Opening the default camera (index 0)
video_cap = cv2.VideoCapture(0)

# Infinite loop to continously capture frames and per form face detection
while True :
  
  # Reading a frame from the video capture
  ret , video_data = video_cap.read()
  
  # Converting the frame to grayscale for better face detection
  col = cv2.cvtColor(video_data,cv2.COLOR_BGR2GRAY)
  
  # Detecting faces in the greyscale frame
  faces = face_cap.detectMultiScale(
    col,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30),
    flags=cv2.CASCADE_SCALE_IMAGE
  )
  
  # Drawing rectangles around detected faces
  for (x,y,w,h) in faces:
    cv2.rectangle(video_data,(x,y),(x+w,y+h),(0,255,0),2)
    
    # Displayind the processed frame with rectangles around faces
  cv2.imshow("video_live",video_data)
  
  # Checking for user input to exit the program (press 'a' key)
  if cv2.waitKey(10) == ord("a"):
    break
  
  # Releasing the video capture resources
video_cap.release() 

  # Destroying OpenCV windows
cv2.destroyAllWindows()