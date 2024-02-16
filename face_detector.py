from facenet_pytorch.models.mtcnn import MTCNN
import cv2
import torch
import numpy as np

device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
mtcnn = MTCNN(keep_all=True, device=device)

def mtcnn_detect(img: np.ndarray) -> np.ndarray:
    boxes, probs = mtcnn.detect(img)
    return boxes, probs

def face_location(boxes, probs):
    if  boxes is not None:
        x =  int(boxes[0][0])
        y =  int(boxes[0][1])
        w =  int(boxes[0][2])
        h =  int(boxes[0][3])
        return x, y, w, h
    else:
        pass
    return  0, 0, 0, 0
    
def boxes_draw(frame, x, y, w, h):
    frame = cv2.rectangle(frame, (x,y), (w, h), (255, 0, 0), 2)
    return frame