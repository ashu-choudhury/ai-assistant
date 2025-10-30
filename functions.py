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

from user_keyboard import type
from music_function import playMusic, changeMusic, pauseMusic,setMusicVolume, stopMusic,resumeMusic
from tts import changeVolume
from terminal import shel
from search import searchGoogle
from timer import setTimer
from mouse import mouse
from gettts import change_voice
from youtube_search import searchYoutube
from date_time import get_formatted_time

FUNCTIONS=[
	playMusic,
	changeMusic,
	pauseMusic,
	setMusicVolume,
	stopMusic,
	changeVolume,
	shel,
	searchGoogle,
	setTimer,resumeMusic,
	mouse,
	type,
	change_voice,
	searchYoutube,
	get_formatted_time
]
