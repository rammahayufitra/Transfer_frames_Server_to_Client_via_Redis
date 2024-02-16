import redis
import cv2
import base64 
import numpy as np
from face_detector import boxes_draw

redis_connection = redis.Redis(host="localhost", port=6379, db=1)

def decode_frame(encoded_frame):
    frame_bytes = base64.b64decode(encoded_frame)
    frame_array = np.frombuffer(frame_bytes, dtype=np.uint8)
    frame = cv2.imdecode(frame_array, cv2.IMREAD_COLOR)
    return frame

while  True:
    frame_redis = redis_connection.get('frame_redis')
    if  frame_redis :
        frame  = decode_frame(frame_redis)
        face_location = eval(redis_connection.get('faces_location'))
        x = face_location['x']
        y = face_location['y']
        w = face_location['w']
        h = face_location['h']
        frame = boxes_draw(frame, x, y, w, h)
    else:
        frame = np.zeros((640, 480, 3))

    # cv2.imshow('Webcam', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
    