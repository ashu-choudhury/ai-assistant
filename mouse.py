# Copyright 2025 Ashu Choudhury
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import pyautogui


def mouse(x: int, y: int, doubleClick: bool, button: int):
	"""
	Function to perform mouse actions (move and click) at specific screen coordinates.

	Parameters:
	- x (int): The horizontal position on the screen to move the mouse to.
	- y (int): The vertical position on the screen to move the mouse to.
	- doubleClick (bool): If True, double-click. If False, single-click.
	- button (int): Mouse button to click (1 for left, 2 for middle, 3 for right).

	As the AI, you will call this function to automate mouse actions. You should first
	analyze the user's screenshot to find the position of the element to click. Then,
	use this function to move the mouse to that position and perform the click action.

	This function returns a dictionary with detailed information about the mouse action,
	including:
	- The coordinates where the mouse was moved.
	- The type of click performed (single or double).
	- The mouse button that was used (left, middle, or right).
	- The user’s screen context, such as the location and action performed.
	"""

	# Move the mouse to the specified position (x, y)
	pyautogui.moveTo(x, y)

	# Perform the click action based on the button parameter
	if button == 1:  # Left button
		if doubleClick:
			pyautogui.doubleClick()
			action_type = 'double-click'
		else:
			pyautogui.click()
			action_type = 'single-click'
		button_name = 'left'
	elif button == 2:  # Middle button
		if doubleClick:
			pyautogui.doubleClick(button=2)
			action_type = 'double-click'
		else:
			pyautogui.click(button=2)
			action_type = 'single-click'
		button_name = 'middle'
	elif button == 3:  # Right button
		if doubleClick:
			pyautogui.doubleClick(button=3)
			action_type = 'double-click'
		else:
			pyautogui.click(button=3)
			action_type = 'single-click'
		button_name = 'right'

	# Create a dictionary with detailed information about the action
	action_info = {
		'screen_info': {
			'user_screen': 'User is sharing the screen for interaction',  # Reference to user screen sharing context
			'action_performed': f'{action_type} using {button_name} button'
		},
		'mouse_position': {
			'x': x,
			'y': y,
			'description': f'Mouse moved to position ({x}, {y}) on the screen'
		},
		'click_action': {
			'doubleClick': doubleClick,
			'button_used': button_name,
			'action_type': action_type,
			'description': f'{action_type.capitalize()} action performed with the {button_name} button'
		}
	}

	# Return the action info dictionary
	return action_info
