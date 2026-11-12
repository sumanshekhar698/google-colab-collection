import requests
from bs4 import BeautifulSoup

# Dependencies: Requires 'requests' and 'beautifulsoup4' libraries installed

def generate_secret_message(url):
    # Fetch Google Doc content
    response = requests.get(url)
    if response.status_code != 200:
        print("Error: Unable to fetch the document.")
        return
    
    # Parse HTML table data
    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find('table')
    if not table:
        print("Error: No table found in the document.")
        return
    
    grid_data = {}
    max_x = 0
    max_y = 0
    
    # Skip the header row and iterate through data rows
    rows = table.find_all('tr')[1:]
    for row in rows:
        cols = row.find_all(['td', 'th'])
        if len(cols) >= 3:
            # Safely extract text and convert coordinates to integers
            try:
                x = int(cols[0].get_text(strip=True))
                char = cols[1].get_text() # Preserve the character as-is
                y = int(cols[2].get_text(strip=True))
                
                # Store character using coordinate tuple as the key
                grid_data[(x, y)] = char
                
                # Track grid boundaries
                if x > max_x: max_x = x
                if y > max_y: max_y = y
            except ValueError:
                # Skip rows that don't contain valid numerical coordinates (e.g., header fragments)
                continue

    # 3. Print the grid from top to bottom (y decreases) and left to right (x increases)
    # Note: Based on standard Google Doc coordinate logic for this problem, 
    # y=0 is typically the bottom row, and max_y is the top row.
    for y in range(max_y, -1, -1):
        row_chars = []
        for x in range(max_x + 1):
            # Fill empty spaces with a space character
            row_chars.append(grid_data.get((x, y), ' '))
        print("".join(row_chars))


doc_url = "https://docs.google.com/document/d/e/2PACX-1vTMOmshQe8YvaRXi6gEPKKlsC6UpFJSMAk4mQjLm_u1gmHdVVTaeh7nBNFBRlui0sTZ-snGwZM4DBCT/pub"
generate_secret_message(doc_url)