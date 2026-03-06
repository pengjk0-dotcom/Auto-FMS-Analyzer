import numpy as np
from typing import Tuple, Optional, Dict

class AngleCalculator:
    """角度 + 距离计算工具类（已扩展）"""
    @staticmethod
    def calculate_angle(a: Tuple[float, float], b: Tuple[float, float], c: Tuple[float, float]) -> float:
        ba = np.array(a) - np.array(b)
        bc = np.array(c) - np.array(b)
        cosine = np.dot(ba, bc) / (np.linalg.norm(ba) * np.linalg.norm(bc) + 1e-6)
        angle = np.arccos(np.clip(cosine, -1.0, 1.0))
        return np.degrees(angle)

    @staticmethod
    def calculate_distance(p1: Tuple[float, float], p2: Tuple[float, float]) -> float:
        """归一化欧氏距离（用于肩部距离等）"""
        return np.hypot(p1[0] - p2[0], p1[1] - p2[1])

    @staticmethod
    def get_landmark_point(landmarks: Dict[int, Tuple[float, float, float]], idx: int) -> Optional[Tuple[float, float]]:
        if idx not in landmarks:
            return None
        x, y, _ = landmarks[idx]
        return (x, y)
