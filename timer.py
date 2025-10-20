import time
from tts import speak
import threading

class Timer:
	def setNewTimer(self, TIMER, NAME, content):
		time.sleep(TIMER*60)
		string=f"""
dear user your timer: {NAME}
is completed
timer for :{content}
it is a reminder automatic message do not reply this
"""
		speak(string)
	


def setTimer(Time: int, Name: str, Content: str):

    """
    This function sets a timer for a specified duration and triggers a reminder once the timer completes.

    It allows you to schedule a reminder with a custom name and content that will be announced when the timer expires.
Do not force user to provide every detail is there a just provide name and timer you should automatically create content for this if you can make any grammar issue yeah something wrong you should edit the name everything do not force user to provide a name do not force user to provide anything you should automatically do everything
    Args:
        Time (int): The duration of the timer in minutes, representing how long the timer will run before triggering the reminder.
        Name (str): The name or title of the timer, used to identify it (e.g., "Test Timer").
        Content (str): The content or message associated with the timer, which will be announced when the timer expires (e.g., "Time to take a break!").

    Returns:
        dict: A dictionary containing:
            - "status": A message indicating the timer has been set.
            - "name": The name of the timer.
            - "content": The content/message associated with the timer.
            - "message": A success message confirming the timer has been set.
    
    This function will set the timer and immediately return. Once the timer expires, the specified reminder will be announced.
    """
    # Create a Timer instance and start the timer in a separate thread
    timer = Timer()
    timerThread = threading.Thread(target=timer.setNewTimer, args=(Time, Name, Content,))
    timerThread.start()

    return {
        "status": f"Timer set for {Time} minutes.",
        "name": Name,
        "content": Content,
        "message": "Timer set successfully for user."
    }
