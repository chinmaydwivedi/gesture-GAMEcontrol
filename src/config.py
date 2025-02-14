# Virtual key codes
KEY_CODES = {
    'W': 0x11,  # Gas
    'S': 0x1F,  # Brake
    'A': 0x1E,  # Left
    'D': 0x20   # Right
}

# Hand tracking settings
HAND_TRACKING = {
    'max_num_hands': 1,
    'min_detection_confidence': 0.7,
    'min_tracking_confidence': 0.7
}

# Gesture thresholds
GESTURE_CONFIG = {
    'gas_threshold': 4,     # Number of fingers for gas
    'brake_threshold': 1    # Number of fingers for brake
}

# Camera settings
CAMERA = {
    'width': 640,
    'height': 480,
    'fps': 30
}