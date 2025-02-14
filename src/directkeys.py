from pynput.keyboard import Key, Controller

# Initialize keyboard controller
keyboard = Controller()

# Key mappings (using simple characters instead of virtual key codes)
W = 'w'  # Forward/Gas
A = 'a'  # Left
S = 's'  # Backward/Brake
D = 'd'  # Right

def PressKey(key):
    """
    Simulates a key press
    Args:
        key: The key to be pressed (e.g., 'w', 'a', 's', 'd')
    """
    keyboard.press(key)

def ReleaseKey(key):
    """
    Simulates a key release
    Args:
        key: The key to be released (e.g., 'w', 'a', 's', 'd')
    """
    keyboard.release(key)

# Optional: Test function to verify key simulation
def test_keys():
    """
    Test function to verify key simulation is working
    """
    import time
    print("Testing key simulation...")
    print("Pressing 'w' for 1 second...")
    PressKey(W)
    time.sleep(1)
    ReleaseKey(W)
    print("Test complete!")

if __name__ == "__main__":
    # Uncomment to test the key simulation
    # test_keys()
    pass