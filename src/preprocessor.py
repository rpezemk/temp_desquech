from pathlib import Path
import cv2
import numpy as np
from shapely.geometry import LineString
import src.log as log


import src.line_operations as line_operations

def load_images(paths: list[Path]) -> list:
    res = list(map(lambda p: (p, read_image(p)), paths))
    return res


def read_image(path: Path):
    img = cv2.imread(str(path))  # BGR image
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 50, 150, apertureSize=3)
    log.nice(path)
    print(path)
    lines = cv2.HoughLinesP(edges, 
                       rho=1, 
                       theta=np.pi/180, 
                       threshold=34)
    lines = [line_operations.to_shapely(l[0]) for l in lines]
    lines = line_operations.merge_lines(lines)
    log.nice("lines", lines)
    return lines

