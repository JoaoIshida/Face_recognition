# Face Recognition and Login System

I created this face recognition and login system to deepen my understanding of computer vision. Using Python with [OpenCV](https://pypi.org/project/deepface/) and [DeepFace](https://pypi.org/project/opencv-python/) libraries to create a simple face recognition and login system using your webcam. It verifies whether the detected face matches a reference image (`my_face.jpg`) and allows login upon successful recognition.

This project demonstrates how modern computer vision techniques can enhance security on computers without pre-installed face recognition software. Through this experience, I learned about face detection, data preprocessing, and ensuring accurate recognition, paving the way for future exploration and applications in computer vision.

## Libraries Used

### OpenCV (cv2)

OpenCV (Open Source Computer Vision Library) is used for real-time computer vision tasks such as face detection and video capture.

- **cv2.VideoCapture(0)**: Opens the default webcam for video capture.
- **cv2.CascadeClassifier**: Initializes the face detection classifier using Haar cascades.
- **cv2.cvtColor**: Converts the color of frames from BGR to grayscale for face detection.
- **cv2.rectangle**: Draws rectangles around detected faces on the video frame.
- **cv2.imshow**, **cv2.waitKey**, **cv2.destroyAllWindows**: Display and manage video frames and windows.

### DeepFace

DeepFace is a lightweight face recognition and facial attribute analysis library for Python.

- **DeepFace.verify**: Performs face verification against a reference image (`my_face.jpg`).
- **result["verified"]**: Checks if the detected face is verified against the reference image.
- **result["distance"]**: Measures the similarity distance between faces.

## Reference Image (`my_face.jpg`)

The `my_face.jpg` file located in the same directory as the script serves as the reference image for face verification. It can be of any size and shape
, however, ensure this image contains a clear and representative picture of your face for accurate recognition.

## Script Overview

The script performs the following steps:

1. **Initialization**

   - Opens the webcam (`cv2.VideoCapture(0)`).
   - Initializes the face detection classifier (`cv2.CascadeClassifier`).
   - Defines maximum login attempts (`max_attempts`) and initializes attempt counters.

2. **Face Detection and Recognition Loop**

   - Captures frames from the webcam and converts them to grayscale.
   - Detects faces in the grayscale frame using the cascade classifier.
   - For each detected face, crops the face region and attempts to verify it against `my_face.jpg` using DeepFace.
   - Implements a retry mechanism (`max_attempts`) to ensure robust face recognition.
   - Draws rectangles around detected faces and displays the video frame (`cv2.imshow`)- this part is for feedback only and will be removed in a real use scenario .

3. **Login Handling**

   - If the face is recognized (`result["verified"]` is `True` and `result["distance"]` is less than `distance_threshold`), performs the login action (`perform_login()`).
   - If face recognition fails after `max_attempts`, prompts for password login (`prompt_password_login()`).

4. **User Interaction**

   - Press 'q' to quit the application (`cv2.waitKey`).

5. **Cleanup**
   - Releases the webcam (`cap.release()`) and closes all OpenCV windows (`cv2.destroyAllWindows()`).

## What I've Learned

Through this project, I've gained practical experience in:

- Implementing real-time face detection and recognition using OpenCV and DeepFace.
- Handling webcam video capture and processing frames for face detection.
- Integrating external libraries (`cv2` and `DeepFace`) to build a functional application.
- Managing user interaction and error handling in real-time applications.

## Why This Project is Cool

This project combines cutting-edge technologies like computer vision and deep learning to create a biometric login system. It's cool because:

- It uses your webcam to authenticate users based on facial recognition.
- It demonstrates the power of Python libraries for AI and computer vision applications.
- It provides a hands-on experience in building a security system using accessible tools.

## Future Implementations

Future enhancements and implementations for this project could include:

- **Password Phase**: Integrate a password login phase as a fallback option if face recognition fails.
- **Embedding to Machines without GUI**: Implement the script to run on machines using bash scripts or headless configurations.
- **Enhanced Security Features**: Add features like anti-spoofing detection to improve security against photo or video-based attacks.
- **User Management**: Develop a user management system to handle multiple users and permissions.
- **Learn More**: Learn more of Deepface capabilities and other projects to use it.
