import redis
import base64 
import cv2

redis_connection = redis.Redis(host="localhost", port=6379, db=1)

def encode_frame(frame):
    _, buffer = cv2.imencode('.jpg', frame)
    frame_bytes = buffer.tobytes()
    encoded_frame = base64.b64encode(frame_bytes)
    return encoded_frame

def main():
    cap = cv2.VideoCapture("http://192.168.1.64:8080/video")
    if not cap.isOpened():
        print("Tidak bisa membuka kamera.")
        return

    while True:
        ret, frame = cap.read()
        if ret:
            frame =cv2.resize(frame,(640,320))
            encoded_frame = encode_frame(frame)
            redis_connection.set('frame1', encoded_frame, ex=2)
        else:
            cap = cv2.VideoCapture("http://192.168.1.64:8080/video")
       

if __name__ == "__main__":
    main()



