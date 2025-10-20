import pyautogui

def type(text: str, speed: float = 0.1):
    """
    This function types the given text on the user's keyboard.

    Use this function when you need to type something on the user's keyboard.

    You can adjust the typing speed to suit your preference:
    - To type slowly, increase the interval between keystrokes.
    - To type quickly, decrease the interval.
    - If you want to type something directly without any delay, set `speed=0` to paste the text instantly.

    Args:
        text (str): The text to be typed.
        speed (float): The interval between each keystroke, in seconds. Default is 0.1 seconds.
                       Set `speed=0` for instant typing (text will be pasted directly).

    Returns:
        dict: A dictionary with a message confirming that the text was typed successfully.

    Example:
        type("Hello, how are you?", speed=0.002)  # For fast typing, around 2 milliseconds per key.
        type("Hello, World!", speed=0)  # For instant typing, text will be pasted directly.
    """
    # If speed is 0, type instantly without any delay
    if speed == 0:
        pyautogui.write(text, interval=0)  # No interval, text is pasted directly
    else:
        pyautogui.write(text, interval=speed)

    return {
        "status": f"Successfully typed: {text}"
    }
