import requests
from bs4 import BeautifulSoup

def scrape_music_list():
    """
    Scrapes a list of music tracks from Free Music Archive's main page.
    
    Returns:
        list: A list of music track names found on the page.
    """
    url = "https://freemusicarchive.org/genre/Random"  # FMA's genre page

    # Send GET request to the webpage
    response = requests.get(url)
    
    if response.status_code != 200:
        return {"error": "Failed to retrieve data from FMA"}
    
    # Parse the HTML page with BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find all the track names in the page
    track_names = []
    
    for track_item in soup.find_all('a', class_='track-title'):
        track_names.append(track_item.get_text(strip=True))

    # Return the list of track names
    return track_names

# Example usage
music_list = scrape_music_list()
if isinstance(music_list, list):
    print("List of Music Tracks:")
    for track in music_list:
        print(track)
else:
    print(music_list["error"])
