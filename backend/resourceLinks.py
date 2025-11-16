import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# Step 1: Fetch the page
url = "https://sacd.sdsu.edu/cps/our-services-and-programs/counseling-individual"
response = requests.get(url)
response.raise_for_status()

# Step 2: Parse with BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")

# Step 3: Extract elements
title = soup.title.string if soup.title else ""

# collect all anchor hrefs and filter by the path fragments
anchors = soup.find_all('a', href=True)
serviceLinks = [a['href'] for a in anchors if '/cps/our-services-and-programs' in a['href']]
therapyLinks = [a['href'] for a in anchors if '/cps/talk-with-a-therapist' in a['href']]
selfLinks = [a['href'] for a in anchors if '/cps/self-care' in a['href']]

all_links_found = serviceLinks + therapyLinks + selfLinks

# deduplicate while preserving order
seen_list = []
seen_set = set()
for link in all_links_found:
    if link not in seen_set:
        seen_set.add(link)
        seen_list.append(link)

base = "https://sacd.sdsu.edu"

# Step 4: Print results
print("Page title:", title)
print("Links found:")
for link in seen_list:
    fullLink = link if link.startswith("http") else urljoin(base, link)
    print(fullLink)
