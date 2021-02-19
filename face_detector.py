#!python3
#face_detector.py - program to detect face in a image, video or in real-time

# Algorith used = Cascade Classifier Algorithms

import cv2  # importing opencv module

# Loading pretrained data that i've downloaded from opencv github.
trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Taking user input
print("*** Machine Learning Face detector Project ***")
print("Programmer: https://www.github.com/Punit-Choudhary\n")

user_input = input("Type i for image and w for realtime webcam or video:  ")

if user_input == 'i':
    # Choosing an image to test
    img_path = input("Enter file path(with extention i.e. png,jpg):  ")
    img = cv2.imread(img_path)
    
    # Converting image to greyscale
    greyscaled_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detecting faces in image
    face_cordinates = trained_face_data.detectMultiScale(greyscaled_img)
    
    (x, y, w, h) = face_cordinates[0]
    
    for (x, y, w, h) in face_cordinates:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow('Punit Choudhary\'s Project',img)
    cv2.waitKey()

elif user_input == 'w':
    video = input("Enter path of video or press enter for real-time: ")
    print("Hit q or Q to quit!")
    
    if video == '':
        video = 0
    
    webcam = cv2.VideoCapture(video)

    # Iterate over frames forever
    while True:
        # reading the current frame
        successful_frame_read, frame = webcam.read()

        # Converting frame to greyscale
        greyscaled_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        face_cordinates = trained_face_data.detectMultiScale(greyscaled_img)
    
        for (x, y, w, h) in face_cordinates:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)


        cv2.imshow("Punit Choudhary\'s Project", frame)
        key = cv2.waitKey(1)

        if key == 81 or key == 113:
            break

    # Releasing the webcam
    webcam.release()

print("Code completed")