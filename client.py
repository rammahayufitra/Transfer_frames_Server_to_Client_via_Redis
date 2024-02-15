import redis
import cv2
import base64 
import numpy as np

redis_connection = redis.Redis(host="localhost", port=6379, db=1)

def decode_frame(encoded_frame):
    frame_bytes = base64.b64decode(encoded_frame)
    frame_array = np.frombuffer(frame_bytes, dtype=np.uint8)
    frame = cv2.imdecode(frame_array, cv2.IMREAD_COLOR)
    return frame


while  True:
    get_frame1 = redis_connection.get('frame1')
    if  get_frame1 :
        frame1  = decode_frame(get_frame1)
    else:
        frame1 = np.zeros((640, 480, 3))

    cv2.imshow('Webcam', frame1)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
    