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


