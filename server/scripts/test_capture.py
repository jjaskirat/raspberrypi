# import cv2
# import urllib.request
# import numpy as np

# stream = urllib.request.urlopen('http://localhost:8080/stream.mjpg')
# bytes = b''
# while True:
#     bytes += stream.read(1024)
#     a = bytes.find(b'\xff\xd8')
#     b = bytes.find(b'\xff\xd9')
#     if a != -1 and b != -1:
#         jpg = bytes[a:b+2]
#         bytes = bytes[b+2:]
#         i = cv2.imdecode(np.frombuffer(jpg, dtype=np.uint8), cv2.IMREAD_COLOR)
#         cv2.imshow('i', i)
#         if cv2.waitKey(1) == 27:
#             exit(0)   


import cv2
import warnings
warnings.filterwarnings('ignore')    

cap = cv2.VideoCapture("http://localhost:8080/stream.mjpg")

while True:

    ret, frame = cap.read()
    cv2.imshow('video', frame)

    k = cv2.waitKey(30) & 0xff
    if k == 27:  # press 'ESC' to quit
        break
