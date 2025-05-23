from pathlib import Path
import cv2

def load_images(paths: list[Path]) -> list:
    res = list(map(read_image, paths))
    return res

def read_image(path: Path):
    img = cv2.imread(str(path))  # BGR image
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return gray