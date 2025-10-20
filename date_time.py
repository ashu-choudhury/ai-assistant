from datetime import datetime


def get_formatted_time():
	"""
	Returns the current date and time in a spoken-style, human-friendly format.

	This function generates a full natural language description of the current
	date and time, useful for speaking out loud or displaying in assistants.

	Example output:
		"2025, 1st of July, Tuesday, 4.22 PM, and 22 seconds"

	Returns:
		str: The current date and time as a formatted string.
	"""
	now = datetime.now()

	# Date parts
	year = now.year
	day = now.day
	weekday = now.strftime("%A")
	month = now.strftime("%B")

	# Determine suffix
	if 11 <= day <= 13:
		suffix = "th"
	else:
		suffix = {1: "st", 2: "nd", 3: "rd"}.get(day % 10, "th")

	day_with_suffix = f"{day}{suffix}"

	# Time parts
	hour_min = now.strftime("%-I.%M %p") if hasattr(now, 'strftime') else now.strftime("%I.%M %p").lstrip("0")
	seconds = now.second

	return f"{year}, {day_with_suffix} of {month}, {weekday}, {hour_min}, and {seconds} seconds"
