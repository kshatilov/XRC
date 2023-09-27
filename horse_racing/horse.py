from random import randint
import cv2

 
def horserun(videoparam, callback):
  videoPath = videoparam
  cap = cv2.VideoCapture(videoPath)
  _, frame = cap.read()

  bboxes = []
  colors = [0, 128, 255, 0, 128, 255]
  bboxes = [(352, 240, 105, 173), (885, 265, 99, 186), (723, 234, 130, 182), (654, 246, 108, 154), (548, 230, 116, 185), (476, 255, 82, 140)] 

  multiTracker = cv2.legacy.MultiTracker_create()
  for bbox in bboxes:
    multiTracker.add(cv2.legacy.TrackerCSRT_create(), frame, bbox)

  frameno = 0
  while cap.isOpened():
      _, frame = cap.read()
      frameno += 1
      list = []
      _, boxes = multiTracker.update(frame)

      for i, newbox in enumerate(boxes):
          p1 = (int(newbox[0]), int(newbox[1]))
          p2 = (int(newbox[0] + newbox[2]), int(newbox[1] + newbox[3]))
          cv2.rectangle(frame, p1, p2, colors[i], 2, 1)
          cv2.putText(frame, str(i), p1, cv2.FONT_HERSHEY_SIMPLEX, 1, colors[i], 2)
          temp2 = p1[0]
          tempno = (frameno + 0.1*(600-temp2))/376
          if tempno > 1:
              tempno = 1
          list.insert(len(list), tempno)
    
      cv2.imshow('MultiTracker', frame)
      callback(list)
      if cv2.waitKey(1) & 0xFF == 27:  # Esc pressed
          break
      
  return 0    
