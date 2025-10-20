from youtubesearchpython import VideosSearch, StreamURLFetcher

def searchYoutube(q: str, limit: int) -> list:
	"""
	Searches for media content such as music, tutorials, or general videos using a natural-language query.

	Parameters:
	    q (str): The search query string describing the desired media content.
	    limit (int): The maximum number of results to return. Must be 1 or more.

	Returns:
	    List[Dict[str, Any]]: A list of up to 3 media result dictionaries. Each result includes:
	        - title (str): Title of the media item
	        - link (str): Direct URL for playback
	        - duration (str): Duration of the media (if available)
	        - thumbnails (list): List of thumbnail image URLs
	        - channel (str): Name of the content creator or source
	        - viewCount (str): View count information (if available)
	        - publishedTime (str): Relative publication time
	"""
	search = VideosSearch(q, limit= limit)
	return search.result()["result"]


