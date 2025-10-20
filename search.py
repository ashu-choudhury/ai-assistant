from googlesearch import search
import requests
from bs4 import BeautifulSoup

def searchGoogle(q: str) -> dict:
    #play("run_function.mp3")
    """
    A tool for retrieving real-time information from Google.

    This function is designed to fetch real-time data directly from Google. 
    Use this function whenever real-world, live information is needed, such as:
    - Current time and date.
    - Weather updates.
    - Latest news or events.
    - Sports scores.
    - Any other real-time data.

    **Key Notes:**
    - Do not ask the user what they want to search. Automatically determine and provide 
      the relevant real-time information based on the query or context.
    - This function is essential for any scenario requiring live data retrieval.

    **Parameters:**
        q (str): The search term or query to retrieve information from Google.

    **Returns:**
        dict: A dictionary containing:
            - "result" (str): The extracted text content if successful.
            - "error" (str): An error message if any issue occurs.

    **Examples:**
    - Fetch current weather: `searchGoogle("current weather in New York")`
    - Get the current time: `searchGoogle("current time in Tokyo")`
    - Retrieve breaking news: `searchGoogle("latest news today")`
    """
    print(q)
    try:
        text = list(search(q, num_results=1))
        print(text[0])
        html = requests.get(text[0])
        body=BeautifulSoup(html.text, 'html.parser')
        htmlText=""
        for tag in body.select('footer, nav, .language-list, .unwanted-class'):
            tag.decompose()
        if body.find('main'):  # Check for <main> tag
            htmlText = body.find('main').get_text(strip=True)
        elif body.find('article'):  # Check for <article> tag
            htmlText = body.find('article').get_text(strip=True)
        elif body.find('div', {'id': 'content'}):  # Check for a common content div
            htmlText = body.find('div', {'id': 'content'}).get_text(strip=True)
        else:  # Default to the body text if no specific section is found
            htmlText = body.get_text(strip=True)
        return {
            "result": htmlText,
            "error": None
        }
    except requests.RequestException as e:
        print(e)
        return {
            "result": None,
            "error": str(e)
        }




