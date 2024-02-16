import redis
import base64 
import cv2

from face_detector import mtcnn_detect, face_location,  boxes_draw

redis_connection = redis.Redis(host="localhost", port=6379, db=1)

def encode_frame(frame):
    _, buffer = cv2.imencode('.jpg', frame)
    frame_bytes = buffer.tobytes()
    encoded_frame = base64.b64encode(frame_bytes)
    return encoded_frame

def main():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("can not access camera.")
        return

    while True:
        ret, frame = cap.read()
        encoded_frame = encode_frame(frame)
        #set data with expired time 2 second
        redis_connection.set('frame_redis', encoded_frame, ex=2)
        if ret:
            boxes, probs = mtcnn_detect(frame)
            x, y, w, h = face_location(boxes, probs)
            redis_connection.set('faces_location', str({'x':x, 'y':y, 'w':w, 'h':h}), ex=2)
        else:
            cap = cv2.VideoCapture(0)
       

if __name__ == "__main__":
    main()



