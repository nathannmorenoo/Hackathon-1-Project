# ==========================================================
# # resourceLinks.py
# # Script to scrape counseling service links from SDSU Counseling and Psychological Services webpage.
# ==========================================================

# Imports
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# Fetch the page
url = "https://sacd.sdsu.edu/cps/our-services-and-programs/counseling-individual"
response = requests.get(url)
response.raise_for_status()

# Parse with BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")

# Extract elements
title = soup.title.string if soup.title else ""

# collect all anchor hrefs and filter by the path fragments
anchors = soup.find_all('a', href=True)
serviceLinks = [a['href'] for a in anchors if '/cps/our-services-and-programs' in a['href']]
therapyLinks = [a['href'] for a in anchors if '/cps/talk-with-a-therapist' in a['href']]
selfLinks = [a['href'] for a in anchors if '/cps/self-care' in a['href']]

# Get link names
link_Names = [a.get_text(strip=True) for a in anchors if a['href'] in serviceLinks + therapyLinks + selfLinks]

all_links_found = serviceLinks + therapyLinks + selfLinks

# deduplicate while preserving order
seen_list = []
seen_set = set()
for link in all_links_found:
    if link not in seen_set:
        seen_set.add(link)
        seen_list.append(link)

base = "https://sacd.sdsu.edu"

# Construct full URLs
for link in seen_list:
    fullLink = link if link.startswith("http") else urljoin(base, link)

# Create final lists of names and links
final_links = []
final_names = []
seen = set()

for a in anchors:
    href = a.get('href')
    if not href:
        continue
    if any(fragment in href for fragment in ('/cps/our-services-and-programs', '/cps/talk-with-a-therapist', '/cps/self-care')):
        full = href if href.startswith("http") else urljoin(base, href)
        if full in seen:
            continue
        seen.add(full)
        name = a.get_text(strip=True) or full
        final_names.append(name)
        final_links.append(full)

# Print results [Output: name - link]
print("Page title:", title)
print("Links found:")
for name, link in zip(final_names, final_links):
    print(f"{name} - {link}")

