from bs4 import BeautifulSoup
import requests

# This Python script was designed to participate in a competition organized by kitesurf shop Icarus
# The goal was to find a eastern egg hidden on their website
# I used the packages requests and BeautifulSoup to iterate over the webpages till I found a link including the word easter
# When the search is finished I had the page where the egg was hidden and the landing page where to fill in contacts to participate in the game

links = ["https://www.icarus.eu"]
idx = 0

while idx < len(links) and idx < 1000:
    url = links[idx]
    print(f"Idx: {idx}, url: {url}")
    try:
        response = requests.get(url)
        if response.status_code == 200:
            html_content = response.content
            soup = BeautifulSoup(html_content, 'html.parser')
            soup_links = soup.find_all('a')
            for link in soup_links:
                if links[idx] + link.get('href') in links:
                    pass
                else:
                    if link.get('href').find("easter") != -1:
                        print(f"Found a link with easter {links[idx]+link.get('href')}")
                        idx = 1000 + 1
                    else:
                        links.append(links[idx]+link.get('href'))
            idx+=1
        else:
            idx+=1
    except:
        print(f"{url} did not work")
        idx+=1