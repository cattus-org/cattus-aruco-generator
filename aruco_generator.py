import cv2
import numpy as np

class ArucoGenerator:
    def __init__(self):
        self.aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_ARUCO_ORIGINAL)

    def generate_single_marker(self, marker_id: int, size: int, margin_size: int, border_bits: int) -> np.ndarray:
        marker_image = cv2.aruco.generateImageMarker(self.aruco_dict, marker_id, size, borderBits=border_bits)
        if margin_size > 0:
            marker_image = cv2.copyMakeBorder(marker_image, margin_size, margin_size, margin_size, margin_size, cv2.BORDER_CONSTANT, value=255)
        return marker_image

    def generate_marker_row(self, marker_id: int, count: int, size: int, margin_size: int, border_bits: int) -> np.ndarray:
        markers = []
        for _ in range(count):
            marker = self.generate_single_marker(marker_id, size, margin_size, border_bits)
            markers.append(marker)

        row_image = np.hstack(markers)

        return row_image
