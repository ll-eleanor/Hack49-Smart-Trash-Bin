# imports
import cv2
import os
import controller as cnt
import supervision as sv
from ultralytics import YOLO

# import custom trained yolov8 dataset
model = YOLO('best.pt')

# webcam labelling
bounding_box_annotator = sv.BoundingBoxAnnotator()
label_annotator = sv.LabelAnnotator()

# setting video source to webcam
cap = cv2.VideoCapture(0)

# displaying error message if webcam access fails
if not cap.isOpened():
    print("Unable to read camera feed")

# detecting objects until esc key is clicked
while True:

    # capturing frame
    ret, frame = cap.read()

    if not ret:
        break

    # storing frame data
    results = model(frame)[0]
    detections = sv.Detections.from_ultralytics(results)

    # labelling objects on webcam display
    annotated_image = bounding_box_annotator.annotate(scene=frame, detections=detections)
    annotated_image = label_annotator.annotate(scene=annotated_image, detections=detections)
    cv2.imshow('Webcam', annotated_image)

    # storing detected objects in variable
    class_names = detections.data['class_name']

    # running object names through arduino controller code 
    for x in class_names:
        cnt.motor(x)
        break

    # setting exit button to escape key
    k = cv2.waitKey(1)
    if k%256 == 27:
        print("Escape hit, closing...")
        break

# closing video stream
cap.release()
cv2.destroyAllWindows