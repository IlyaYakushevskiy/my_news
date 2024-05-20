import requests
from bs4 import BeautifulSoup
import json
from get_urls import get_recent_urls

# URL list



def prepare_sink(days):
    urls = get_recent_urls(days)
    # Perform web scraping
    def scrape(url):
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find article title
        title_tag = soup.find('h1')
        if title_tag:
            title = title_tag.get_text()
        else:
            title = "No title found"
        
    # Find the meta tag with the specified property
        meta_tag = soup.find('meta', property='article:published_time')

        # Extract the content attribute value if the tag is found
        if meta_tag:
            datetime_string = meta_tag['content']
            publication_date = datetime_string.split("T")[0]
        else:
            publication_date = "No published time found"
        
        # Create article data dictionary
        article_data = {
            "title": title,
            "url": url,
            #"summary": summary,
            "publication_date": publication_date
            # Add more article data as needed
        }

        # Append article data to data_sink
        data_sink["articles"].append(article_data)


    # Initialize or load the data_sink dictionary from JSON
    try:
        with open('data_sink.json', 'r') as f:
            data_sink = json.load(f)
    except FileNotFoundError:
        data_sink = {"articles": []}

    # Iterate over the list of URLs and call scrape function for each URL
    for url in urls:
        print(f"Scraping blog for URL: {url}")
        scrape(url)
        print()  # Add a newline for better readability between URLs

    # Write the updated data_sink to a JSON file
    with open('data_sink.json', 'w') as f:
        json.dump(data_sink, f, indent=4)

    print("Article(s) added to data_sink and saved to 'data_sink.json'")