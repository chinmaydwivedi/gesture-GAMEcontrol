import cv2
import mediapipe as mp
import time
from directkeys import PressKey, ReleaseKey, W, A, S, D
import sys
import subprocess
from pynput.keyboard import Key

def check_camera_permissions():
    try:
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            print("\nCamera access denied. Please grant camera permissions.")
            subprocess.run(['open', 'x-apple.systempreferences:com.apple.preference.security?Privacy_Camera'])
            sys.exit(1)
        cap.release()
    except Exception as e:
        print(f"Error checking camera permissions: {e}")
        sys.exit(1)

def initialize_camera():
    for i in range(3):
        cap = cv2.VideoCapture(0)
        if cap.isOpened():
            cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
            cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
            cap.set(cv2.CAP_PROP_FPS, 30)
            return cap
        print(f"Attempt {i+1}: Failed to open camera. Retrying...")
        time.sleep(1)
    return None

def count_fingers(hand_landmarks):
    finger_tips = [8, 12, 16, 20]
    thumb_tip = 4
    raised_fingers = 0
    
    if hand_landmarks[thumb_tip].x < hand_landmarks[thumb_tip - 1].x:
        raised_fingers += 1
    
    for tip in finger_tips:
        if hand_landmarks[tip].y < hand_landmarks[tip - 2].y:
            raised_fingers += 1
    
    return raised_fingers

def main():
    check_camera_permissions()
    
    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands(max_num_hands=2, min_detection_confidence=0.7, min_tracking_confidence=0.7)
    mp_draw = mp.solutions.drawing_utils
    
    cap = initialize_camera()
    if cap is None:
        print("Failed to initialize camera.")
        sys.exit(1)
    
    prev_time = 0
    
    try:
        while True:
            success, img = cap.read()
            if not success:
                print("Failed to grab frame, retrying...")
                time.sleep(0.1)
                continue
            
            img = cv2.flip(img, 1)
            rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            results = hands.process(rgb_img)
            
            total_fingers = 0
            
            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    mp_draw.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                    fingers = count_fingers(hand_landmarks.landmark)
                    total_fingers += fingers
                
                if total_fingers == 0:
                    PressKey(Key.space)
                else:
                    ReleaseKey(Key.space)
                
                if (total_fingers == 2 or total_fingers == 1):
                    PressKey(W)
                else:
                    ReleaseKey(W)   
                if total_fingers == 3:
                    PressKey(A)
                else:
                    ReleaseKey(A)
                
                if total_fingers == 5:
                    PressKey(S)
                else:
                    ReleaseKey(S)
                
                if total_fingers == 4:
                    PressKey(D)
                else:
                    ReleaseKey(D)
                                                                  
            
            current_time = time.time()
            fps = 1 / (current_time - prev_time)
            prev_time = current_time
            cv2.putText(img, f"FPS: {int(fps)}", (400, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
            
            cv2.imshow("Hand Tracking", img)
            
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    
    except KeyboardInterrupt:
        print("\nProgram terminated by user")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
