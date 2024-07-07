import cv2
from deepface import DeepFace

reference_img_path = 'my_face.jpg'

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# open webcam 
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

print("Press 'q' to quit.")

max_attempts = 100  # max attempts to recognize the face
attempts = 0
recognized = False
verify_count = 0
verify_threshold = 3  # number of consecutive verifications needed
distance_threshold = 0.4  # distance threshold for DeepFace verification

def perform_login():
    global recognized
    recognized = True
    print("Face recognized. Logging in...")
    #TODO: implement login logic

    cap.release()
    cv2.destroyAllWindows()

def prompt_password_login():
    print(f"Face not recognized after {max_attempts} attempts. Switching to password login...")
    # TODO:implement password login
    
while True:
    # capture frame-by-frame
    ret, frame = cap.read()

    if not ret:
        print("Error: Failed to capture image")
        break

    # grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # detect faces
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    #TODO: add anti-spoofing and enhanced security
    face_recognized = False
    for (x, y, w, h) in faces:
        face_region = frame[y:y+h, x:x+w]

        try:
            result = DeepFace.verify(face_region, reference_img_path)

            if result["verified"] and result["distance"] < distance_threshold:
                verify_count += 1
                print(f"Face recognized {verify_count}/{verify_threshold} times")
                if verify_count >= verify_threshold:
                    face_recognized = True
                    break  
            else:
                verify_count = 0
        except Exception as e:
            print(f"Error: {e}")

        # draw a rectangle around the face (optional)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

        if face_recognized:
            break

    # display the resulting frame (optional)
    cv2.imshow('Video', frame)

    if not face_recognized:
        attempts += 1
        if attempts >= max_attempts:
            prompt_password_login()
            break

    if face_recognized:
        perform_login()
        break

    # can exit loop too
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
