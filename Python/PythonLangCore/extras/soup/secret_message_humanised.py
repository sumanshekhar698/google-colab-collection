import requests
from bs4 import BeautifulSoup

def generate_secret_message(url):
    res = requests.get(url)
    if res.status_code != 200:
        return
    
    soup = BeautifulSoup(res.text, 'html.parser')
    table = soup.find('table')
    if not table:
        return

    coords = {}
    max_x = max_y = 0
    
    # Skip header row and extract grid coordinates
    rows = table.find_all('tr')[1:]
    for row in rows:
        cols = row.find_all(['td', 'th'])
        if len(cols) < 3:
            continue
            
        try:
            x = int(cols[0].text.strip())
            char = cols[1].text
            y = int(cols[2].text.strip())
            
            coords[(x, y)] = char
            
            if x > max_x: max_x = x
            if y > max_y: max_y = y
        except ValueError:
            continue

    # Render grid from top-left down to bottom-right
    for y in range(max_y, -1, -1):
        print(''.join(coords.get((x, y), ' ') for x in range(max_x + 1)))


if __name__ == "__main__":
    doc_url = "https://docs.google.com/document/d/e/2PACX-1vTMOmshQe8YvaRXi6gEPKKlsC6UpFJSMAk4mQjLm_u1gmHdVVTaeh7nBNFBRlui0sTZ-snGwZM4DBCT/pub"
    doc_url_2 = "https://docs.google.com/document/d/e/2PACX-1vSvM5gDlNvt7npYHhp_XfsJvuntUhq184By5xO_pA4b_gCWeXb6dM6ZxwN8rE6S4ghUsCj2VKR21oEP/pub"
    # generate_secret_message(doc_url)
    generate_secret_message(doc_url_2)