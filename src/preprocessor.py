from pathlib import Path
import cv2

def get_vector_data(paths: list[Path]) -> list:

    '''
    
    '''
    res = []
    for path in paths:
        normal = vectorize(path)
        res.append(normal)
    return []

def vectorize(path: Path):
    img = cv2.imread(str(path))  # BGR image
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)